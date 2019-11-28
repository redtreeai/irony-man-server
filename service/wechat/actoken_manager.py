# -*- coding: utf-8 -*-
# @Time    : 19-11-28 下午4:31
# @Author  : Redtree
# @File    : actoken_manager.py
# @Desc :    AccessToken 校验及获取


from __init__ import ROOT_PATH
from __init__ import WECHAT_APPSECRET,WECHAT_APPID
import requests
import json
import time


def get_token():

    f=open(ROOT_PATH+'/token.txt', 'r')
    data = f.readlines()
    f.close()

    url = 'https://api.weixin.qq.com/cgi-bin/token?' \
          'grant_type=client_credential&appid=' + WECHAT_APPID + '&secret=' + WECHAT_APPSECRET

    if not data:  #当没有token时候

        r = requests.get(url)
        token = json.loads(r.text)['access_token']

        f = open(ROOT_PATH+'/token.txt', 'w')
        f.write(token+'\n'+str(int(time.time())))

        return token

    elif (int(time.time())-int(data[1])) >=7200:  #超过时间 重新获取

        url = 'https://api.weixin.qq.com/cgi-bin/token?' \
              'grant_type=client_credential&appid=' + WECHAT_APPID + '&secret=' + WECHAT_APPSECRET

        r = requests.get(url)
        token = json.loads(r.text)['access_token']

        f = open(ROOT_PATH+'/token.txt', 'w')
        f.write(token + '\n' + str(int(time.time())))


        return token


    else:
        return str(data[0]).replace('\n','')