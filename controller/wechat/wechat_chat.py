# -*- coding: utf-8 -*-
# @Time    : 19-11-29 上午10:51
# @Author  : Redtree
# @File    : wechat_chat.py
# @Desc :



from __init__ import app
from __init__ import  request
from service.wechat import wechat_chat_manager
from utils.http import responser


@app.route('/wechat_chat', endpoint='wechat_chat',methods=['POST'])
def wechat_chat():
    """
    @api {post} /wechat_chat 用户聊天
    @apiName wechat.wechat_chat
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid
    @apiParam {string} input_text 用户输入的聊天内容

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
        }
    }
    """
    res_status,rjson = responser.post_param_check(request,['openid','input_text'])
    if res_status == 'success':
        return wechat_chat_manager.chat(rjson['openid'],rjson['input_text'])
    else:
        return rjson



@app.route('/wechat_chat_welcome', endpoint='wechat_chat_welcome',methods=['POST'])
def wechat_chat_welcome():
    """
    @api {post} /wechat_chat_welcome 机器人欢迎消息
    @apiName wechat.wechat_chat
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
           'text':'我劝你商量',
           'img':'表情包图片地址'  #先图片后文字的顺序，空的就不发
        }
    }
    """
    res_status,rjson = responser.post_param_check(request,['openid'])
    if res_status == 'success':
        return wechat_chat_manager.get_welcome(rjson['openid'])
    else:
        return rjson



@app.route('/wechat_chat_autofuck', endpoint='wechat_chat_autofuck',methods=['GET'])
def wechat_chat_autofuck():
    """
    @api {get} /wechat_chat_autofuck 获取内容，自动开骂
    @apiName wechat.wechat_chat
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
           'text':'我劝你商量',
           'img':'表情包图片地址'  #先图片后文字的顺序，空的就不发
        }
    }
    """
    res_status,rjson = responser.get_param_check(request,['openid'])
    if res_status == 'success':
        return wechat_chat_manager.auto_fuck(rjson['openid'])
    else:
        return rjson