# -*- coding: utf-8 -*-
# @Time    : 19-11-28 下午5:23
# @Author  : Redtree
# @File    : wechat_user_manager.py
# @Desc :   用户信息操作

from __init__ import DBSession_xxcxb,PAGE_LIMIT,USER_SALT_LENGTH
from __init__ import redis_client
from utils.common import redisor
from database.sqlalchemy.orm_models.zf_wechat_userinfo import Zf_wechat_userinfo
import time
from utils.http import responser
import json


#登录后更新数据
'''
 zfid = Column(Integer, primary_key=True)
    openid = Column(String(50))  # 用户openid
    nickname = Column(String(50))  # 用户昵称
    avatar = Column(Text)  # 头像
    gender = Column(Integer)  # 0:保密，1：男，2：女
    province = Column(String(50))  # 省份
    city = Column(String(50))  # 市区
    country = Column(String(50))  # 国
    is_vip = Column(Integer)  # 0不是1是
    vip_time = Column(Integer)  # vip到期时间
    created_time Column(Integer) #纪录创建时间
    updated_time = Column(Integer)  # 纪录更新时间

'''


def update_userinfo(openid,nickname,avatar,gender,province,city,country):

    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())
        try:
            info = session.query(Zf_wechat_userinfo).filter(Zf_wechat_userinfo.openid == openid).one()
            #记录已存在则更新
            info = session.query(Zf_wechat_userinfo).filter(Zf_wechat_userinfo.openid == openid).update(
                {Zf_wechat_userinfo.nickname: nickname, Zf_wechat_userinfo.avatar: avatar, Zf_wechat_userinfo.gender: gender,
                 Zf_wechat_userinfo.province: province, Zf_wechat_userinfo.city: city, Zf_wechat_userinfo.country: country,
                 Zf_wechat_userinfo.updated_time:ctime})
            if not info == 0 and not info == '':
                session.commit()
                session.close()
                return responser.send(10000, 'success')
            session.close()
            return responser.send(400002)
        except:
            #否则创建
            try:
                info = session.add(Zf_wechat_userinfo(openid=str(openid), nickname=str(nickname), avatar=str(avatar),
                                                       gender=int(gender),province=str(province),city=str(city),country=str(country),
                                                       is_vip=0,vip_time=0,
                                                       created_time=int(ctime),
                                                       updated_time=int(ctime),))

                if not info == 0 and not info == '':
                        session.commit()
                        session.close()
                        # 异步更新redis会员状态
                        rkey = 'wx_'+openid
                        robj = {'is_vip':0,'times':0}
                        redisor.update_redis_kv(redis_client,rkey,json.dumps(robj))
                        return responser.send(10000, 'success')

                session.close()
                return responser.send(40002)

            except:
                session.rollback() #回滚
                session.close()
    except:
        return responser.send(50007)



#获取当前登录用户详细信息
def get_user_data(openid):
    try:
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_wechat_userinfo).filter(Zf_wechat_userinfo.openid == openid).one()
            DB_data = json.loads(str(info))  # 需要强转字符串才能序列化

            session.close()
            return responser.send(10000, DB_data)

        except Exception as err:
            return responser.send(40002)
    except:
        return responser.send(40002)


