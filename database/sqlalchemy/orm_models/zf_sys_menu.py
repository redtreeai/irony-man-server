# -*- coding: utf-8 -*-
# @Time    : 18-10-29 上午11:57
# @Author  : Redtree
# @File    : zf_sys_menu.py
# @Desc : 菜单表

import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer,Text)

class Zf_sys_menu(Base_xxcxb):
    __tablename__ = 'zf_sys_menu'

    zfid = Column(Integer, primary_key=True)
    menu_code = Column(String(50))  #菜单代码
    comment = Column(String(100)) #描述
    parent_code = Column(String(50)) #关联父级菜单id
    created_time = Column(Integer)
    updated_time = Column(Integer)
    is_admin = Column(Integer) #是否后台菜单 0否1是

    def __repr__(self):
        get_data = {
            "zfid":self.zfid,
            "menu_code":self.menu_code,
            "comment":self.comment,
            "parent_code":self.parent_code,
            "created_time":self.created_time,
            "updated_time":self.updated_time,
            "is_admin":self.is_admin
        }
        get_data = json.dumps(get_data)
        return get_data