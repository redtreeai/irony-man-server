# -*- coding: utf-8 -*-
# @Time    : 19-4-9 下午2:24
# @Author  : Redtree
# @File    : zf_nlp_qa.py
# @Desc : 语料详细信息表


import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_nlp_qa(Base_xxcxb):
    __tablename__ = 'zf_nlp_qa'

    zfid = Column(Integer, primary_key=True)
    qa_code = Column(String(50))  # 语料代码
    question = Column(Text) #输入
    answer = Column(Text) #输出
    created_time = Column(Integer)
    updated_time = Column(Integer)
    updated_user_id = Column(String(20)) #更新信息的用户id


    def __repr__(self):
        get_data = {
            "zfid": self.zfid,
            "qa_code": self.qa_code,
            "question": self.question,
            "answer": self.answer,
            "created_time": self.created_time,
            "updated_time": self.updated_time,
            "updated_user_id": self.updated_user_id
        }
        get_data = json.dumps(get_data)
        return get_data


