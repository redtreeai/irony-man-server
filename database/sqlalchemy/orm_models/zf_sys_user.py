# -*- coding: utf-8 -*-
# @Time    : 18-8-8 下午3:43
# @Author  : Redtree
# @File    : zf_sys_user.py
# @Desc : 用户表


import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer,Text)

class Zf_sys_user(Base_xxcxb):
    __tablename__ = 'zf_sys_user'

    zfid = Column(Integer, primary_key=True)
    user_id = Column(String(20))  #用户id
    nickname = Column(String(20))  #用户昵称
    real_name = Column(String(20))  #真实姓名
    id_card = Column(String(20)) #身份证号
    birthday = Column(Integer) #时间戳 出生日期
    salt = Column(String(4))  #盐
    password = Column(String(32)) #密码
    del_flag= Column(Integer)  #删除状态   0为可用 1为已删除
    created_time=Column(Integer)
    updated_time=Column(Integer)
    role_code = Column(String(50)) #关联角色代码
    email = Column(String(50)) #邮箱地址
    wx_id = Column(String(64)) #微信id
    head_img = Column(String(255)) #头像地址
    phone = Column(String(20)) #手机号码
    last_login = Column(Integer) #最后一次登录时间
    org_code = Column(String(50)) #学校或者机构名
    created_user_id = Column(String(20)) #创建用户id
    is_active = Column(Integer) #是否激活   1为激活 0为封禁
    gender = Column(Integer) #0:其他，1：男，2：女，3：保密
    user_code = Column(String(50)) #学号
    introduction = Column(String(255)) #简介
    remark = Column(String(255)) #备注


    def __repr__(self):
        get_data = {"zfid":self.zfid,
                    "user_id":self.user_id,
                    "nickname":self.nickname,
                    "real_name":self.real_name,
                    "id_card":self.id_card,
                    "birthday":self.birthday,
                    "salt":self.salt,
                    "password":self.password,
                    "del_flag":self.del_flag,
                    "created_time":self.created_time,
                    "updated_time":self.updated_time,
                    "role_code":self.role_code,
                    "email":self.email,
                    "user_code":self.user_code,
                    "wx_id":self.wx_id,
                    "head_img":self.head_img,
                    "phone":self.phone,
                    "last_login":self.last_login,
                    "org_code":self.org_code,
                    "created_user_id":self.created_user_id,
                    "is_active":self.is_active,
                    "gender":self.gender,
                    "introduction": self.introduction,
                    "remark": self.remark,

                    }
        get_data = json.dumps(get_data)
        return get_data