# -*- coding: utf-8 -*-
# @Time    : 19-12-20 下午3:27
# @Author  : Redtree
# @File    : wechat_pay.py
# @Desc :

from __init__ import make_response,request
from __init__ import app
import xml.etree.ElementTree as ET   #xml解码器
from service.wechat import wechat_vippay_manager
from utils.http import responser


@app.route('/wechat_buy_vip', endpoint='wechat_buy_vip',methods=['POST'])
def wechat_buy_vip():
    """
    @api {post} /wechat_buy_vip 下单支付vip年费
    @apiName wechat.wechat_buy_vip
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
        }
    }
    """
    res_status,rjson = responser.post_param_check(request,['openid'])
    if res_status == 'success':
        return wechat_vippay_manager.payment(rjson['openid'])
    else:
        return rjson


@app.route('/payaccept', methods=['GET','POST'])
def pay_accept():  # 导入:
    try:
        if request.method == 'POST':
            xml_recv = ET.fromstring(request.data)
            return_code = xml_recv.find("return_code").text

            # openid=xml_recv.find("openid").text
            # total_fee=xml_recv.find("total_fee").text
            # out_trade_no = xml_recv.find("out_trade_no").text
            if return_code == 'SUCCESS':
                reply = "<xml><return_code><![CDATA[SUCCESS]]></return_code><return_msg><![CDATA[OK]]></return_msg></xml>"
                response = make_response(reply)
                response.content_type = 'application/xml'
                res = '订单信息支付完成，调用更新数据的方法'
                if res == 'success':
                    return response
                else:
                    return 'error'
        else:
            return 'whoareyou'
    except:
        return 'who are you!'
