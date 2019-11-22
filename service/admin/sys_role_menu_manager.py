# -*- coding: utf-8 -*-
# @Time    : 18-10-31 下午3:38
# @Author  : Redtree
# @File    : sys_role_menu_manager.py
# @Desc :  角色菜单关联管理

from __init__ import DBSession_xxcxb
from database.sqlalchemy.orm_models.zf_sys_role_menu import Zf_sys_role_menu
from utils.http import responser
import json

#创建新的关联关系
def add_role_menu(user_id,role_code,menu_code):
    try:
        if not user_id == 'zfadmin':
            return responser.send(30001)  # 操作非法，只有管理员有权限
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_role_menu).filter(Zf_sys_role_menu.role_code == role_code,
                                                          Zf_sys_role_menu.menu_code == menu_code).one()
            return responser.send(10006)

        except:
            info = session.add(Zf_sys_role_menu(role_code=str(role_code), menu_code=str(menu_code)))
            if not info == 0 and not info == '':
                session.commit()
                session.close()

                return responser.send(10000, 'success')
            session.close()
            return responser.send(40002)
    except:
        return responser.send(50007)


#根据id批量删除角色菜单关联
def del_role_menus(user_id,role_code,menu_code):
    try:
        if not user_id == 'zfadmin':
            return responser.send(30001)  # 操作非法，只有管理员有权限
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_role_menu).filter(Zf_sys_role_menu.role_code==role_code,Zf_sys_role_menu.menu_code==menu_code).delete(
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


#通过角色代码获取菜单关联列表

def get_menucode_by_rolecode(userid,role_code):
    try:

        if not userid == 'zfadmin':
            return responser.send(30001)  # 操作非法，只有管理员有权限
        session = DBSession_xxcxb()

        info = session.query(Zf_sys_role_menu).filter(
            Zf_sys_role_menu.role_code == role_code).all()

        if not info == 0 and not info == '':
            DB_data = json.loads(str(info))  # 需要强转字符串才能序列化
            session.close()
            return responser.send(10000, DB_data)
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#通过用户ID获取所有关联列表
#获取菜单列表

def get_menucode_by_userid(userid,code_search):
    try:
        if not userid == 'zfadmin':
            return responser.send(30001)  # 操作非法，只有管理员有权限
        session = DBSession_xxcxb()

        code_search = '%' + code_search + '%'

        info = session.query(Zf_sys_role_menu).filter(
            Zf_sys_role_menu.menu_code.like(code_search) or Zf_sys_role_menu.role_code.like(code_search)).all()

        if not info == 0 and not info == '':
            DB_data = json.loads(str(info))  # 需要强转字符串才能序列化
            session.close()
            return responser.send(10000, DB_data)
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)

