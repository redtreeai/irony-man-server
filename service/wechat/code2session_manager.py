# -*- coding: utf-8 -*-
# @Time    : 19-11-28 下午5:04
# @Author  : Redtree
# @File    : code2session_manager.py
# @Desc : 登录凭证校验


from __init__ import WECHAT_APPID
from __init__ import WECHAT_APPSECRET
import requests
import json
from utils.http import responser


def check_login(code):
    #WECHAT_APPID='wx0e4041630f2f5e83'
    #WECHAT_APPSECRET= 'ccab6c1b52643354323e763f60f8a869'
    try:
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + WECHAT_APPID + '&secret=' + WECHAT_APPSECRET + '&js_code=' + code + '&grant_type=authorization_code'
        r = requests.get(url)
        res = json.loads(r.text)
        try:
            # 捕捉到异常则打印错误信息
            errcode = res['errcode']
            print(res)
            return responser.send(80001)
        except:
            #无异常则解析
            openid = res['openid']
            session_key = res['session_key']
            res = {'openid':openid,'session_key':session_key}
            return responser.send(10000, '登录成功')
    except:
        return responser.send(80001)


