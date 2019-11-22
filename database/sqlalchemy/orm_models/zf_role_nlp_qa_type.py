# -*- coding: utf-8 -*-
# @Time    : 19-4-17 下午1:55
# @Author  : Redtree
# @File    : zf_role_nlp_qa_type.py
# @Desc : 角色语料权限表


import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_role_nlp_qa_type(Base_xxcxb):
    __tablename__ = 'zf_role_nlp_qa_type'

    zfid = Column(Integer, primary_key=True)
    qa_code = Column(String(50))  # 语料代码
    role_code = Column(String(50))  # 角色代码
    auth_type = Column(Integer)  #0为只读 1为读写
    created_time = Column(Integer)
    updated_time = Column(Integer)

    def __repr__(self):
        get_data = {
            "zfid": self.zfid,
            "qa_code": self.qa_code,
            "role_code": self.role_code,
            "auth_type": self.auth_type,
            "created_time": self.created_time,
            "updated_time": self.updated_time
        }
        get_data = json.dumps(get_data)
        return get_data
