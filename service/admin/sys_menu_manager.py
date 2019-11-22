# -*- coding: utf-8 -*-
# @Time    : 18-10-31 上午11:20
# @Author  : Redtree
# @File    : sys_menu_manager.py
# @Desc :   系统菜单管理服务

from __init__ import DBSession_xxcxb,PAGE_LIMIT
from database.sqlalchemy.orm_models.zf_sys_menu import Zf_sys_menu
from database.sqlalchemy.orm_models.zf_sys_role_menu import Zf_sys_role_menu
from sqlalchemy import func,or_
from utils.http import responser
import time
import json

#创建新的菜单
def add_menu(code,comment,parent_code,is_admin):
    try:
        session = DBSession_xxcxb()
        created_time = int(time.time())
        try:
            info = session.query(Zf_sys_menu).filter(Zf_sys_menu.menu_code == code).one()
            session.close()
            return responser.send(10006)

        except:
            info = session.add(
                Zf_sys_menu(menu_code=str(code), created_time=int(created_time), updated_time=int(created_time),
                            comment=str(comment), parent_code=str(parent_code), is_admin=is_admin))
            if not info == 0 and not info == '':
                session.commit()
                session.close()

                return responser.send(10000, 'success')
            session.close()
            return responser.send(40002)

    except:
        return responser.send(50007)

#修改菜单信息
def update_menu(code,comment,parent_code =None):
    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())
        info = session.query(Zf_sys_menu).filter(Zf_sys_menu.menu_code == str(code)).update(
            {Zf_sys_menu.updated_time: ctime, Zf_sys_menu.comment: comment, Zf_sys_menu.parent_code: parent_code})
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#获取菜单列表
def get_menus(userid,code_search,is_top,page):
    try:
        if not userid == 'zfadmin':
            return responser.send(30001)  # 操作非法，只有管理员有权限
        session = DBSession_xxcxb()
        code_search = '%' + code_search + '%'
        if is_top == 1:
            all_len = session.query(func.count(Zf_sys_menu.zfid)).filter(Zf_sys_menu.menu_code.like(code_search),Zf_sys_menu.parent_code=='',Zf_sys_menu.is_admin==1).scalar()
            info = session.query(Zf_sys_menu).filter(Zf_sys_menu.menu_code.like(code_search),Zf_sys_menu.parent_code=='',Zf_sys_menu.is_admin==1).order_by(
                Zf_sys_menu.updated_time.desc()).all()
        else:
            all_len = session.query(func.count(Zf_sys_menu.zfid)).filter(or_(Zf_sys_menu.menu_code.like(code_search), Zf_sys_menu.parent_code.like(code_search),Zf_sys_menu.is_admin==1)
                ).scalar()
            info = session.query(Zf_sys_menu).filter(or_(Zf_sys_menu.menu_code.like(code_search), Zf_sys_menu.parent_code.like(code_search),Zf_sys_menu.is_admin==1)
                ).order_by(
                Zf_sys_menu.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

        if not info == 0 and not info == '':
            DB_data = json.loads(str(info))  # 需要强转字符串才能序列化
            session.close()
            res = {"total": all_len, "data": DB_data}
            return responser.send(10000, res)
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)

#获取菜单列表
def get_role_all_menus(role_code,admin_user_id):
    try:
        if not admin_user_id == 'zfadmin':
            return responser.send(30001)  # 操作非法，只有管理员有权限
        session = DBSession_xxcxb()

        info = session.query(Zf_sys_menu).order_by(
                Zf_sys_menu.updated_time.desc()).all()

        lef_list = []
        for x in info:
            x_obj = {'key':x.menu_code,'label':x.comment}
            lef_list.append(x_obj)

        info2 = session.query(Zf_sys_role_menu).filter(Zf_sys_role_menu.role_code==role_code).all()
        rig_list = []
        for y in info2:
            for ll in lef_list:
                if y.menu_code==ll['key']:
                    c_label =ll['label']
                    c_obj = {'key':y.menu_code,'label':c_label}
                    rig_list.append(c_obj)

        res_list = [lef_list,rig_list]

        if not info == 0 and not info == '':
            session.close()
            return responser.send(10000, res_list)
        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)



#删除菜单列表
def del_menus(menu_codelist):
    try:
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_menu).filter(Zf_sys_menu.menu_code.in_(menu_codelist)).delete(
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

