# -*- coding: utf-8 -*-
# @Time    : 19-11-28 下午4:23
# @Author  : Redtree
# @File    : zf_wechat_userinfo.py
# @Desc :

import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer, Text)


class Zf_wechat_user_info(Base_xxcxb):
    __tablename__ = 'zf_wechat_user_info'

    zfid = Column(Integer, primary_key=True)
    openid = Column(String(50))  # 用户unionid
    nickname = Column(String(50))  # 用户昵称
    avatar = Column(Text)  # 头像
    gender = Column(Integer)  # 0:保密，1：男，2：女
    province = Column(String(50))  # 省份
    city = Column(String(50))  # 省份
    country = Column(String(50))  # 省份
    is_vip = Column(Integer)  # 0不是1是
    vip_time = Column(Integer)  # vip到期时间
    created_time = Column(Integer)
    updated_time = Column(Integer)  # 纪录更新时间

    def __repr__(self):
        get_data = {"zfid": self.zfid,
                    "openid": self.openid,
                    "nickname": self.nickname,
                    "avatar": self.avatar,
                    "gender": self.gender,
                    "province": self.province,
                    "city": self.city,
                    "country": self.country,
                    "is_vip": self.is_vip,
                    "vip_time": self.vip_time,
                    "created_time": self.created_time,
                    "updated_time": self.updated_time
                    }
        get_data = json.dumps(get_data)
        return get_data
