# -*- coding: utf-8 -*-
# @Time    : 19-4-17 下午1:59
# @Author  : Redtree
# @File    : role_nlp_qa_type_manager.py
# @Desc :   角色语料权限管理


from __init__ import DBSession_xxcxb,PAGE_LIMIT
from database.sqlalchemy.orm_models.zf_role_nlp_qa_type import Zf_role_nlp_qa_type
from database.sqlalchemy.orm_models.zf_nlp_qa_type import Zf_nlp_qa_type
from database.sqlalchemy.orm_models.zf_nlp_qa import Zf_nlp_qa
from sqlalchemy import func,or_
from utils.http import responser
import time
import json


#新增角色语料权限
def add_role_nlp_qa_type(role_code,qa_code):

     try:
         session = DBSession_xxcxb()
         ctime = int(time.time())
         info = session.add(
             Zf_role_nlp_qa_type(role_code=str(role_code), qa_code=str(qa_code),created_time=int(ctime),updated_time=int(ctime),auth_type=1))
         if not info == 0 and not info == '':
             session.commit()
             session.close()

             return responser.send(10000, '角色语料模块新增成功')
     except:
         return responser.send(40002)

#修改角色语料权限类型
def update_role_nlp_qa_type(id,auth_type):
    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())
        info = session.query(Zf_role_nlp_qa_type).filter(Zf_role_nlp_qa_type.zfid == str(id)).update(
            {Zf_role_nlp_qa_type.updated_time: ctime, Zf_role_nlp_qa_type.auth_type: auth_type})
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#获取角色语料表
def get_role_nlp_qa_type(role_code,search,page):
    try:
        session = DBSession_xxcxb()
        sum = session.query(func.count(Zf_nlp_qa.zfid)).scalar()
        d1 = session.query(Zf_role_nlp_qa_type.qa_code).filter(Zf_role_nlp_qa_type.role_code == role_code).all()
        search = '%' + search + '%'

        if not d1 == 0 and not d1 == '':
            codes = []
            for xcode in d1:
                codes.append(xcode[0])

            all_len = session.query(func.count(Zf_nlp_qa_type.zfid)).filter(Zf_nlp_qa_type.qa_code.in_(codes),
                Zf_nlp_qa_type.qa_name.like(search)).scalar()
            d2 = session.query(Zf_nlp_qa_type).filter(Zf_nlp_qa_type.qa_code.in_(codes), Zf_nlp_qa_type.qa_name.like(search)).order_by(
            Zf_nlp_qa_type.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

            if not d2 == 0 and not d2 == '':
                DB_data = json.loads(str(d2))

                session.close()
                res = {"qa_sum":sum,"total": all_len, "data": DB_data}
                return responser.send(10000, res)

        session.close()
        return responser.send(40002)
    except Exception as err:
        print(err)
        return responser.send(50007)


#删除角色语料理关联
def del_role_nlp_qa_type(role_code,qa_code_list):
    try:

        session = DBSession_xxcxb()

        info = session.query(Zf_role_nlp_qa_type).filter(Zf_role_nlp_qa_type.qa_code.in_(qa_code_list),Zf_role_nlp_qa_type.role_code==role_code).delete(
                synchronize_session=False)
        if info >= 0:
          session.commit()
          session.close()
        return responser.send(10000, 'successs')

    except:
        return responser.send(40002)


#获取角色语料表(新版)
def get_role_all_nlp_qa_type(role_code):
    try:
        session = DBSession_xxcxb()
        info = session.query(Zf_nlp_qa_type).order_by(
            Zf_nlp_qa_type.updated_time.desc()).all()
        lef_list = []
        for x in info:
            x_obj = {'key':x.qa_code,'label':x.qa_name}
            lef_list.append(x_obj)

        info2 = session.query(Zf_role_nlp_qa_type).filter(Zf_role_nlp_qa_type.role_code==role_code).all()
        rig_list = []
        for y in info2:
            for ll in lef_list:
                if y.qa_code==ll['key']:
                    c_label =ll['label']
                    c_obj = {'key':y.qa_code,'label':c_label}
                    rig_list.append(c_obj)

        res_list = [lef_list,rig_list]

        if not info == 0 and not info == '':
            session.close()
            return responser.send(10000, res_list)
        session.close()
        return responser.send(40002)
    except Exception as err:
        print(err)
        return responser.send(50007)