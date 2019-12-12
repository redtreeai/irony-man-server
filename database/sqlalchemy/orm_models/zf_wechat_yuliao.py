# -*- coding: utf-8 -*-
# @Time    : 19-12-12 下午4:02
# @Author  : Redtree
# @File    : zf_wechat_yuliao.py
# @Desc : 用户语料上传


import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_wechat_yuliao(Base_xxcxb):
    __tablename__ = 'zf_wechat_yuliao'

    zfid = Column(Integer, primary_key=True)
    openid = Column(String(50))  # 用户unionid
    nickname = Column(String(50))  # 用户unionid
    input_text = Column(Text)  # 头像
    output_text = Column(Text)  # 头像
    created_time = Column(Integer)
    updated_time = Column(Integer)  # 纪录更新时间

    def __repr__(self):
        get_data = {"zfid": self.zfid,
                    "openid": self.openid,
                    "nickname": self.nickname,
                    "input_text": self.input_text,
                    "output_text": self.output_text,
                    "created_time": self.created_time,
                    "updated_time": self.updated_time
                    }
        get_data = json.dumps(get_data)
        return get_data