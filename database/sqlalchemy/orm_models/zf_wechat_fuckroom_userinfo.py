# -*- coding: utf-8 -*-
# @Time    : 19-12-27 下午4:00
# @Author  : Redtree
# @File    : zf_wechat_fuckroom_userinfo.py
# @Desc :


import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_wechat_jianyi(Base_xxcxb):
    __tablename__ = 'zf_wechat_fuckroom_userinfo'

    zfid = Column(Integer, primary_key=True)
    openid = Column(String(50))  # 用户unionid
    win_times = Column(Integer)
    lose_times = Column(Integer)
    updated_time = Column(Integer)  # 纪录更新时间

    def __repr__(self):
        get_data = {"zfid": self.zfid,
                    "openid": self.openid,
                    "win_times": self.win_times,
                    "lose_times": self.lose_times,
                    "updated_time": self.updated_time
                    }
        get_data = json.dumps(get_data)
        return get_data