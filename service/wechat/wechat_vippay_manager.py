# -*- coding: utf-8 -*-
# @Time    : 19-12-20 下午3:24
# @Author  : Redtree
# @File    : wechat_vippay_manager.py
# @Desc :


import hashlib
import xml.etree.ElementTree as ET   #xml解码器
import time
import requests
from random import Random
from utils.http import responser

def random_str(randomlength=32):  #随机字符串生成算法
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]

    return str

#需要获取的用户的openid才可以进行统一下单,最后让前端通过接口调用到此工具返回的数据即可调用支付服务

def payment(openid):  #统一下单

    try:
        if openid=='undefined':
            return responser.send(80002)

        appid = 'wx0e4041630f2f5e83'    #公众号id
        body = '吵架神器，一年vip特权'     #商品名
        fee = '600' #总价
        mch_id = '1501554691'      #商户号
        nonceStr = random_str(32)    #随机串
        notifyurl = 'https://robotapi.chenhongshu.com/payaccept' #支付回调链接
        #根据当前系统时间加openid加随机数生成订单号

        b = openid[0:10]
        c = str(int(time.time()))
        d = random_str(8)
        out_trade_no = (b + d + c)  #订单号
        serverIP = '122.152.232.55'    #服务器地址
        mch_key = '6W7MmVLXCrPkyxfTUwelOKj3NQhSR9os'  #支付密钥

        all_pay_url = 'https://api.mch.weixin.qq.com/pay/unifiedorder'   #统一下单api地址

        stringA = "appid="+appid+"&body="+body+"&mch_id="+mch_id+"&nonce_str="+nonceStr+"&notify_url="+notifyurl+"&openid="+openid+"&out_trade_no="+out_trade_no+"&spbill_create_ip="+serverIP+"&total_fee="+fee+"&trade_type=JSAPI"
        stringSignTemp = stringA + "&key="+mch_key
        paysign = hashlib.md5(stringSignTemp.encode('utf-8')).hexdigest().upper()


        pay_xml = "<xml><appid>" + appid + "</appid><body>" + body + "</body><mch_id>" + mch_id + "</mch_id><nonce_str>" + nonceStr + "</nonce_str><notify_url>" + notifyurl + "</notify_url><openid>" + openid + "</openid><out_trade_no>" + out_trade_no + "</out_trade_no><spbill_create_ip>" + serverIP + "</spbill_create_ip><total_fee>" + fee + "</total_fee><trade_type>JSAPI</trade_type><sign>" + paysign + "</sign></xml> "

        headers = {'Content-Type': 'application/xml'}
        # 访问支付接口
        r = requests.post(all_pay_url, data=pay_xml.encode('utf-8'),
                           headers=headers)

        print(r.text)
        xml_recv = ET.fromstring(r.text)
        print(xml_recv)
        wxre_sign = xml_recv.find('sign').text  #用来校验签名认证
        print(wxre_sign)
        print('w')

        prepay_id = xml_recv.find('prepay_id').text
        package = "prepay_id=" + prepay_id

        ctime = str(int(time.time()))

        stringB = "appId="+appid+"&nonceStr="+nonceStr+"&package="+package+"&signType=MD5&timeStamp="+ctime
        stringBSignTemp = stringB + "&key=???" #这里三个问号替换成商户密钥,不是公众号密钥
        paysign = hashlib.md5(stringBSignTemp.encode('utf-8')).hexdigest().upper()

        res = {'package': package, 'paysign': paysign, 'timestamp': ctime,
                               'nonceStr': nonceStr, 'appId': appid}

        #后面记得补上,保存订单和更新用户vip信息
        # order_res = '这里调用数据库订单创建的逻辑'
        #
        # if not order_res == 'success':
        #     return json.dumps({'rcode': 400, 'msg': '订单创建失败'})

        return responser.send(10000,res)

    except Exception as err:
        print(str(err) + '下单异常')
        return responser.send(80002)

