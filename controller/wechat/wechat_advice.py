# -*- coding: utf-8 -*-
# @Time    : 19-12-12 下午5:31
# @Author  : Redtree
# @File    : wechat_advice.py
# @Desc :

from __init__ import app
from __init__ import  request
from service.wechat import wechat_advice_manager
from utils.http import responser


@app.route('/wechat_upload_yuliao', endpoint='wechat_upload_yuliao',methods=['POST'])
def wechat_upload_yuliao():
    """
    @api {post} /wechat_upload_yuliao 用户上传贡献语料理
    @apiName wechat.wechat_upload_yuliao
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid
    @apiParam {string} nickname 昵称
    @apiParam {string} input_text 输入内容
    @apiParam {string} output_text 输出内容


    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
        }
    }
    """

    res_status,rjson = responser.post_param_check(request,['openid','nickname','input_text','output_text'])
    if res_status == 'success':
        return wechat_advice_manager.upload_yuliao(rjson['openid'],rjson['nickname'],rjson['input_text'],rjson['output_text'])
    else:
        return rjson


@app.route('/wechat_upload_jianyi', endpoint='wechat_upload_jianyi', methods=['POST'])
def wechat_upload_jianyi():
    """
    @api {post} /wechat_upload_jianyi 用户提交建议
    @apiName wechat.wechat_upload_jianyi
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid
    @apiParam {string} nickname 昵称
    @apiParam {string} jianyi 建议内容


    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
        }
    }
    """

    res_status, rjson = responser.post_param_check(request, ['openid', 'nickname', 'jianyi'])
    if res_status == 'success':
        return wechat_advice_manager.upload_yuliao(rjson['openid'], rjson['nickname'], rjson['jianyi'])
    else:
        return rjson



@app.route('/wechat_about_me', endpoint='wechat_about_me', methods=['GET'])
def wechat_about_me():
    """
    @api {get} /wechat_about_me 用户提交建议
    @apiName wechat.wechat_about_me
    @apiGroup wechat
    @apiVersion 1.0.0

    不用传


    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
        }
    }
    """

    return wechat_advice_manager.about_me()
