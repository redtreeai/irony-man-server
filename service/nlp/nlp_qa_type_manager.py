# -*- coding: utf-8 -*-
# @Time    : 19-4-9 下午4:29
# @Author  : Redtree
# @File    : nlp_qa_type_manager.py
# @Desc :  语料集基础信息管理服务

from __init__ import DBSession_xxcxb,PAGE_LIMIT
from database.sqlalchemy.orm_models.zf_nlp_qa_type import Zf_nlp_qa_type
from sqlalchemy import func,or_
from utils.http import responser
import time
import json

#新增语料集
def add_nlp_qa_type(user_id,qa_code,qa_name,qa_welcome,description):
     if not user_id=='zfadmin':
         return responser.send(10000,'没有创建权限')

     try:
         session = DBSession_xxcxb()
         ctime = int(time.time())
         info = session.add(Zf_nlp_qa_type(qa_code=str(qa_code), qa_name=str(qa_name), qa_welcome=str(qa_welcome), description=str(description),
                        updated_user_id=str(user_id),created_time=int(ctime),updated_time=int(ctime)))
         if not info == 0 and not info == '':
             session.commit()
             session.close()

             return responser.send(10000, '语料集创建成功')
     except:
         return responser.send(40002)

#修改应用基础信息
def update_nlp_qa_type(user_id,qa_code,qa_name,qa_welcome,description):
    if not user_id == 'zfadmin':
        return responser.send(10000, '没有修改权限')
    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())
        info = session.query(Zf_nlp_qa_type).filter(Zf_nlp_qa_type.qa_code == str(qa_code)).update(
            {Zf_nlp_qa_type.updated_time: ctime, Zf_nlp_qa_type.qa_name: qa_name,
             Zf_nlp_qa_type.qa_welcome: qa_welcome,Zf_nlp_qa_type.description: description,Zf_nlp_qa_type.updated_user_id: user_id})
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#获取语料列表
def get_nlp_qa_type(user_id,search,page):
    try:
        session = DBSession_xxcxb()
        search = '%' + search + '%'

        all_len = session.query(func.count(Zf_nlp_qa_type.zfid)).filter(Zf_nlp_qa_type.qa_name.like(search)).scalar()
        info = session.query(Zf_nlp_qa_type).filter(Zf_nlp_qa_type.qa_name.like(search)).order_by(
            Zf_nlp_qa_type.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

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


#删除语料集
def del_nlp_qa_type(qa_code_list):

    return responser.send(10000, '没有删除权限')
    try:
        session = DBSession_xxcxb()

        info = session.query(Zf_nlp_qa_type).filter(Zf_nlp_qa_type.qa_code.in_(qa_code_list)).delete(
                synchronize_session=False)
        if info >= 0:
          session.commit()
          session.close()
        return responser.send(10000, 'successs')

    except:
        return responser.send(40002)