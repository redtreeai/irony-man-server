# -*- coding: utf-8 -*-
# @Time    : 19-4-9 下午2:20
# @Author  : Redtree
# @File    : zf_nlp_qa_type.py
# @Desc :  自动问答语聊库基础信息表

import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_nlp_qa_type(Base_xxcxb):
    __tablename__ = 'zf_nlp_qa_type'

    zfid = Column(Integer, primary_key=True)
    qa_code = Column(String(50))  # 语料代码
    qa_name = Column(String(50))  # 语料名称
    qa_welcome = Column(Text) #欢迎语
    description = Column(Text) #详细介绍
    created_time = Column(Integer)
    updated_time = Column(Integer)
    updated_user_id = Column(String(20)) #更新信息的用户id

    def __repr__(self):
        get_data = {
            "zfid": self.zfid,
            "qa_code": self.qa_code,
            "qa_name": self.qa_name,
            "qa_welcome": self.qa_welcome,
            "description": self.description,
            "created_time": self.created_time,
            "updated_time": self.updated_time,
            "updated_user_id": self.updated_user_id
        }
        get_data = json.dumps(get_data)
        return get_data
