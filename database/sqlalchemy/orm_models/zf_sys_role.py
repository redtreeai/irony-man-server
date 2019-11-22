# -*- coding: utf-8 -*-
# @Time    : 18-10-29 上午11:51
# @Author  : Redtree
# @File    : zf_sys_role.py
# @Desc :  角色表


import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_sys_role(Base_xxcxb):
    __tablename__ = 'zf_sys_role'

    zfid = Column(Integer, primary_key=True)
    role_name = Column(String(20))  # 角色名
    created_user_id = Column(String(20))  # 创建用户id
    created_time = Column(Integer)
    updated_time = Column(Integer)
    status = Column(Integer)  # 状态名 0为可用 1为禁止
    role_code = Column(String(50))  # 角色代码

    def __repr__(self):
        get_data = {
            "zfid": self.zfid,
            "role_name": self.role_name,
            "created_user_id": self.created_user_id,
            "created_time": self.created_time,
            "updated_time": self.updated_time,
            "status": self.status,
            "role_code": self.role_code
        }
        get_data = json.dumps(get_data)
        return get_data
