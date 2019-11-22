# -*- coding: utf-8 -*-
# @Time    : 19-4-9 下午4:29
# @Author  : Redtree
# @File    : nlp_qa_manager.py
# @Desc :  语料问答信息管理服务

from __init__ import DBSession_xxcxb,PAGE_LIMIT
from __init__ import ROOT_PATH
from database.sqlalchemy.orm_models.zf_nlp_qa import Zf_nlp_qa
from utils.http import responser
from utils.common import xls_tool
from sqlalchemy import func,or_
import time
import json
import os
from utils.decorator.dasyncio import async_call

#新增语料问答
def add_nlp_qa(user_id,qa_code,question,answer):
     if len(str(question).strip())<1:
        return responser.send(10000, '问题不能为空')

     try:
         session = DBSession_xxcxb()
         ctime = int(time.time())

         info = session.add(Zf_nlp_qa(qa_code=str(qa_code), question=str(question), answer=str(answer),created_time=int(ctime),updated_time=int(ctime),updated_user_id=str(user_id)))
         if not info == 0 and not info == '':
             session.commit()
             session.close()

             return responser.send(10000, '语料问答创建成功')
     except:
         return responser.send(40002)

#修改问答
def update_nlp_qa(user_id,zfid,question,answer):
    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())
        info = session.query(Zf_nlp_qa).filter(Zf_nlp_qa.zfid == int(zfid)).update(
            {Zf_nlp_qa.updated_time: ctime, Zf_nlp_qa.question: question,
             Zf_nlp_qa.answer: answer,Zf_nlp_qa.updated_user_id: user_id})
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#获取问答列表
def get_nlp_qa(qa_code,search,page):
    try:
        session = DBSession_xxcxb()
        search = '%' + search + '%'

        all_len = session.query(func.count(Zf_nlp_qa.zfid)).filter(Zf_nlp_qa.qa_code==str(qa_code),or_(Zf_nlp_qa.question.like(search), Zf_nlp_qa.answer.like(search))).scalar()
        info = session.query(Zf_nlp_qa).filter(Zf_nlp_qa.qa_code==str(qa_code),or_(Zf_nlp_qa.question.like(search), Zf_nlp_qa.answer.like(search))).order_by(
                Zf_nlp_qa.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

        if not info == 0 and not info == '':
            DB_data = json.loads(str(info))  # 需要强转字符串才能序列化
            session.close()
            res = {"total": all_len, "data": DB_data}
            return responser.send(10000, res)

        session.close()
        return responser.send(10000, {"total": 0, "data": []})
    except Exception as err:
        print(err)
        return responser.send(10000, {"total": 0, "data": []})



#删除问答
def del_nlp_qa(zfid_list):
    try:
        session = DBSession_xxcxb()

        info = session.query(Zf_nlp_qa).filter(Zf_nlp_qa.zfid.in_(zfid_list)).delete(
                synchronize_session=False)
        if info >= 0:
          session.commit()
          session.close()
        return responser.send(10000, 'successs')

    except:
        return responser.send(40002)


#excel表格转sql数据
def xlsx2sql(user_id,file_stream,file_name,file_type,directory):

    try:
        SAVE_DIR_PATH = ROOT_PATH + '/upload/' + directory
        SAVE_FILE_PATH = SAVE_DIR_PATH + '/' + file_name + '.' + file_type
        # 确保路径存在
        if os.path.exists(SAVE_DIR_PATH):
            pass
        else:
            os.mkdir(SAVE_DIR_PATH)

        file_stream.save(SAVE_FILE_PATH)  # 保存到本地
        #异步执行数据转存
        xlsx2sql_extra(user_id,file_name,SAVE_FILE_PATH)

        return responser.send(10000, '导入成功')
    except Exception as err:
        return responser.send(50006)



#异步执行数据转存任务
@async_call
def xlsx2sql_extra(user_id,file_name,SAVE_FILE_PATH):
    try:
        res = xls_tool.xls2list(SAVE_FILE_PATH)  # 保存成功后继续
        if res == []:
            return True
        else:
            session = DBSession_xxcxb()
            ctime = int(time.time())

            for r in res:
                info = session.add(
                    Zf_nlp_qa(qa_code=str(file_name), question=str(r[0]), answer=str(r[1]), created_time=int(ctime),
                              updated_time=int(ctime), updated_user_id=str(user_id)))
            session.commit()
            session.close()
            return True
    except:
        return True


#获取指定语料数量统计
def get_nlp_qa_count(qa_code):
    try:
        session = DBSession_xxcxb()
        all_len = session.query(func.count(Zf_nlp_qa.zfid)).filter(Zf_nlp_qa.qa_code==str(qa_code)).scalar()
        session.close()
        res = {"sum": all_len}
        return responser.send(10000, res)

    except Exception as err:
        print(err)
        return responser.send(10000, {"sum": 0})