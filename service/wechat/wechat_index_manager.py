# -*- coding: utf-8 -*-
# @Time    : 19-12-25 上午10:12
# @Author  : Redtree
# @File    : wechat_index_manager.py
# @Desc :  小程序首页相关的接口

from utils.http import responser


def get_bannars(open_id):
    try:
        standar_url = 'https://robotapi.chenhongshu.com/bqb/'
        r1 = {'code': 'fuck_robot', 'img': standar_url + 'bannar1.jpg'}
        r2 = {'code': 'wait', 'img': standar_url + 'bannar2.jpg'}
        r3 = {'code': 'wait', 'img': standar_url + 'bannar3.jpg'}
        resl = [r1, r2, r3]
        return responser.send(10000, resl)
    except:
        return responser.send(10000,[])



def get_gonggao(open_id):
    try:
        standar_url = 'https://robotapi.chenhongshu.com/bqb/'
        img = standar_url + 'gonggao.jpg'
        res =  {'gonggao_tag':1,'img':img}
        return responser.send(10000, res)
    except:
        res =  {'gonggao_tag':1,'img':''}
        return responser.send(10000, res)