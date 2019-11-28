# -*- coding: utf-8 -*-
# @Time    : 19-11-28 下午5:47
# @Author  : Redtree
# @File    : check_login.py
# @Desc :


from __init__ import app
from __init__ import  request
from service.wechat import code2session_manager
from utils.http import responser


@app.route('/wechat_checklogin', endpoint='wechat_checklogin',methods=['POST'])
def wechat_checklogin():
    """
    @api {post} /wechat_checklogin 微信登录校验
    @apiName wechat.wechat_checklogin
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} code 通过wx.login获得的登录凭证 *

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
        }
    }
    """
    res_status,rjson = responser.post_param_check(request,['code'])
    if res_status == 'success':
        return code2session_manager.check_login(rjson['code'])
    else:
        return rjson