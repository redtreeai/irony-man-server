# -*- coding: utf-8 -*-
# @Time    : 18-10-29 下午2:55
# @Author  : Redtree
# @File    : zf_sys_role_menu.py
# @Desc : 角色菜单关联表

import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer)

class Zf_sys_role_menu(Base_xxcxb):
    __tablename__ = 'zf_sys_role_menu'

    zfid = Column(Integer, primary_key=True)
    role_code = Column(String(50))  #角色代码
    menu_code = Column(String(50)) #菜单代码


    def __repr__(self):
        get_data = {
            "zfid":self.zfid,
            "role_code":self.role_code,
            "menu_id":self.menu_code
        }
        get_data = json.dumps(get_data)
        return get_data