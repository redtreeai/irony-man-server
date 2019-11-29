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
