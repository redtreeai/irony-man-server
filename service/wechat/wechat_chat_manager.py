# -*- coding: utf-8 -*-
# @Time    : 19-11-29 上午9:59
# @Author  : Redtree
# @File    : wechat_chat_manager.py
# @Desc :


from __init__ import ROOT_PATH
from __init__ import DBSession_xxcxb,PAGE_LIMIT
from __init__ import redis_client
from utils.nlp import docsim
from utils.common import redisor
from database.sqlalchemy.orm_models.zf_nlp_qa import Zf_nlp_qa
from utils.http import responser
import random
import json

#登录后更新数据
'''
 zfid = Column(Integer, primary_key=True)
    openid = Column(String(50))  # 用户openid
    chat_t
    chat_a
    created_time Column(Integer) #纪录创建时间
    updated_time = Column(Integer)  # 纪录更新时间

'''

def get_qa_dict(qa_code):
    #by mysql
    try:
        session = DBSession_xxcxb()
        info = session.query(Zf_nlp_qa).filter(Zf_nlp_qa.qa_code == str(qa_code)).all()
        if not info == 0 and not info == '':
            session.close()
            c_list = []
            for inf in info:
                c_obj = (inf.question, inf.answer)
                c_list.append(c_obj)
            return c_list
    except Exception as err:
        print(err)
        session.close()
        return []

#基于语料库的问答
def mvp_auto_qa(input_text):
    try:
        qa_code = 'mvp'
        Dictionary_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Dictionary'
        Similarity_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Similarity'
        res = docsim.response(input_text, get_qa_dict(qa_code), Dictionary_path, Similarity_path)
        if res =='error':
            return nice_responese()
        else:
            return res
    except Exception as err :
        return nice_responese()

#和谐回复
def nice_responese():

    res_list = ['懒得理你','你牙齿上有韭菜']
    return random.choice(res_list)


#机器人交互
'''
链接redis校验会员状态，若不存在则通过mysql校验，再写入redis.
如果检验身份是会员，则直接返回答案。
若不是会员，则累计请求次数，每5次请求返回一次广告
'''
def chat(openid,input_text):

    try:
        #第一个版本不做限制
        res = mvp_auto_qa(input_text)
        return responser.send(10000, res)

        # #获取会员状态
        # rkey = 'wx_'+openid
        # gr = redisor.get_redis_value_by_key(redis_client, rkey)
        # #纪录异常，随便回复
        # if gr ==False:
        #     return responser.send(10000, nice_responese())
        # else:
        #     gr = json.loads(gr)
        #     is_mvp = int(gr['is_mvp'])
        #     times = int(gr['times'])
        #     #是会员直接返回
        #     if is_mvp==1:
        #         res = mvp_auto_qa(input_text)
        #         return responser.send(10000,res)
        #     else:
        #         if times>=5:
        #             #放广告,异步重置redis
        #             robj = {'is_mvp':is_mvp,'times':0}
        #             redisor.update_redis_kv(redis_client,rkey,robj)
        #             return responser.send(10000,'放广告')
        #         else:
        #             res = mvp_auto_qa(input_text)
        #             #异步更新次数
        #             robj = {'is_mvp':is_mvp,'times':times+1}
        #             redisor.update_redis_kv(redis_client,rkey,robj)
        #             return responser.send(10000, res)
    except:
        return responser.send(10000, nice_responese())


#使用redis操作交流状态