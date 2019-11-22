# -*- coding: utf-8 -*-
# @Time    : 18-10-31 上午9:19
# @Author  : Redtree
# @File    : zf_sys_org.py
# @Desc :

import json
from __init__ import Base_xxcxb
from sqlalchemy import (Column, String, Integer,Text)

class Zf_sys_org(Base_xxcxb):
    __tablename__ = 'zf_sys_org'

    zfid = Column(Integer, primary_key=True)
    org_name = Column(String(50))  #机构名
    addr = Column(String(100)) #地址
    type = Column(Integer) #机构类型
    created_time = Column(Integer)
    updated_time = Column(Integer)
    members = Column(Integer) #规模
    status = Column(Integer) #状态
    org_code = Column(String(50)) #机构代号
    introduction = Column(Text) #详细介绍
    logo_img = Column(String(255)) #logourl
    created_user_id = Column(String(20)) #创建者帐号
    slogan = Column(String(200)) #口号
    description = Column(String(200)) #简介
    admin_user_id = Column(String(20)) #机构管理员id


    def __repr__(self):
        get_data = {"zfid":self.zfid,
                    "org_name":self.org_name,
                    "addr":self.addr,
                    "type":self.type,
                    "created_time":self.created_time,
                    "updated_time":self.updated_time,
                    "members":self.members ,
                    "status": self.status,
                    "org_code":self.org_code,
                    "introduction":self.introduction,
                    "logo_img":self.logo_img,
                    "created_user_id":self.created_user_id,
                    "slogan":self.slogan,
                    "description":self.description,
                    "admin_user_id":self.admin_user_id
                    }
        get_data = json.dumps(get_data)
        return get_data