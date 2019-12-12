# -*- coding: utf-8 -*-
# @Time    : 19-12-12 下午4:02
# @Author  : Redtree
# @File    : zf_wechat_jianyi.py
# @Desc :


import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_wechat_jianyi(Base_xxcxb):
    __tablename__ = 'zf_wechat_jianyi'

    zfid = Column(Integer, primary_key=True)
    openid = Column(String(50))  # 用户unionid
    nickname = Column(String(50))  # 用户unionid
    jianyi = Column(Text)  # 头像
    created_time = Column(Integer)
    updated_time = Column(Integer)  # 纪录更新时间

    def __repr__(self):
        get_data = {"zfid": self.zfid,
                    "openid": self.openid,
                    "nickname": self.nickname,
                    "jianyi": self.jianyi,
                    "created_time": self.created_time,
                    "updated_time": self.updated_time
                    }
        get_data = json.dumps(get_data)
        return get_data