# -*- coding: utf-8 -*-
# @Time    : 18-8-8 下午3:51
# @Author  : Redtree
# @File    : sys_role_manager.py
# @Desc :

from __init__ import DBSession_xxcxb,PAGE_LIMIT
from database.sqlalchemy.orm_models.zf_sys_user import Zf_sys_user
from database.sqlalchemy.orm_models.zf_sys_role import Zf_sys_role
from database.sqlalchemy.orm_models.zf_sys_role_menu import Zf_sys_role_menu
from utils.http import responser
import json
import time

#创建新角色类型
def add_role(code,name,created_user_id):
    try:
        session = DBSession_xxcxb()
        created_time = int(time.time())
        try:
            info = session.query(Zf_sys_role).filter(Zf_sys_role.role_code == code).one()
            session.close()
            return responser.send(10006)

        except Exception as err:
            print(err)
            info = session.add(Zf_sys_role(role_code=str(code), role_name=str(name), created_time=int(created_time),
                                           updated_time=int(created_time),
                                           created_user_id=str(created_user_id), status=0))
            if not info == 0 and not info == '':
                session.commit()
                session.close()

                return responser.send(10000, 'success')
            session.close()
            return responser.send(40002)
    except:
        return responser.send(50007)


#修改角色名
def update_role_name(code,name):
    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())
        info = session.query(Zf_sys_role).filter(Zf_sys_role.role_code == str(code)).update(
            {Zf_sys_role.updated_time: ctime, Zf_sys_role.role_name: name})
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#获取角色列表 因为角色不多，先不分页
def get_role_list(userid):
    try:
        session = DBSession_xxcxb()
        if not userid == 'zfadmin':
            DB_data = session.query(Zf_sys_role).filter(Zf_sys_role.created_user_id == userid).all()
        else:
            DB_data = session.query(Zf_sys_role).all()

        if not DB_data == 0 and not DB_data == '':
            DB_data = json.loads(str(DB_data))  # 需要强转字符串才能序列化

            session.commit()
            session.close()
            return responser.send(10000, DB_data)

        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#删除角色
def del_role(role_codelist):
    try:
        if 'superadmin' in role_codelist:
            return responser.send(10005)
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_role).filter(Zf_sys_role.role_code.in_(role_codelist)).delete(
                synchronize_session=False)
            if info >= 0:  # 关联用户删除
                info = session.query(Zf_sys_user).filter(Zf_sys_user.role_code.in_(role_codelist)).delete(
                    synchronize_session=False)
                if info >= 0:
                    session.commit()
                    session.close()
                    return responser.send(10000, 'success')
            session.commit()
            session.close()
            return responser.send(10000, 'successs')

        except:
            session.close()
            return responser.send(40002)
    except:
        return responser.send(50007)



#角色状态变更
def ban_role(role_codelist,status):
    try:
        if 'superadmin' in role_codelist:
            return responser.send(10005)

        session = DBSession_xxcxb()
        ctime = int(time.time())

        info = session.query(Zf_sys_role).filter(Zf_sys_role.role_code.in_(role_codelist)).update(
            {Zf_sys_role.status: status, Zf_sys_role.updated_time: ctime}, synchronize_session=False)
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#获取角色权限菜单(通过关联表实现)

def get_rtom(role_code):
    try:
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_role_menu.menu_code).filter(Zf_sys_role_menu.role_code == str(role_code)).all()
            if not info == 0 and not info == '':
                session.close()

                t_array = []
                for one in info:
                    t_array.append(one[0])

                return responser.send(10000, t_array)
            session.close()

            return responser.send(40002)
        except:
            session.close()

            return responser.send(40002)
    except:
        return responser.send(50007)








