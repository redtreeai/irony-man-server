# -*- coding: utf-8 -*-
# @Time    : 19-12-12 下午5:16
# @Author  : Redtree
# @File    : wechat_advice_manager.py
# @Desc :  建议管理器


from __init__ import DBSession_xxcxb,PAGE_LIMIT,USER_SALT_LENGTH
from database.sqlalchemy.orm_models.zf_wechat_yuliao import Zf_wechat_yuliao
from database.sqlalchemy.orm_models.zf_wechat_jianyi import Zf_wechat_jianyi
import time
from utils.http import responser
import json

#上传语料
def upload_yuliao(openid,nickname,input_text,output_text):

    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())

        try:
            info = session.add(Zf_wechat_yuliao(openid=str(openid), nickname=str(nickname),input_text=str(input_text),output_text=str(output_text),
                                                   created_time=int(ctime),
                                                   updated_time=int(ctime)))

            if not info == 0 and not info == '':
                    session.commit()
                    session.close()
                    return responser.send(10000, 'success')

            session.close()
            return responser.send(40002)

        except:
            session.rollback() #回滚
            session.close()
    except:
        return responser.send(50007)


#上传建议
def upload_jianyi(openid, nickname, jianyi):
    try:
        session = DBSession_xxcxb()
        ctime = int(time.time())

        try:
            info = session.add(Zf_wechat_jianyi(openid=str(openid), nickname=str(nickname), jianyi=str(jianyi),
                                                created_time=int(ctime),
                                                updated_time=int(ctime)))

            if not info == 0 and not info == '':
                session.commit()
                session.close()
                return responser.send(10000, 'success')

            session.close()
            return responser.send(40002)

        except:
            session.rollback()  # 回滚
            session.close()
    except:
        return responser.send(50007)


def about_me():
    res= '致力于维护世界和平的嘴强码农'
    return responser.send(10000,res)


