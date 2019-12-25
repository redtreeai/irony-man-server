# -*- coding: utf-8 -*-
# @Time    : 19-12-25 上午10:18
# @Author  : Redtree
# @File    : wechat_index_manager.py
# @Desc :


from __init__ import app
from __init__ import  request
from service.wechat import wechat_index_manager
from utils.http import responser


@app.route('/wechat_chat_index_bannar', endpoint='wechat_chat_index_bannar',methods=['GET'])
def wechat_chat_index_bannar():
    """
    @api {post} /wechat_chat_index_bannar 获取首页bannar信息
    @apiName wechat.wechat_chat
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": [
        {'code':'fuck_robot','img':'https://robotapi.chenhongshu.com/bqb/bannar1.jpg'},
        {'code':'wait','img':'https://robotapi.chenhongshu.com/bqb/bannar2.jpg'},
        {'code':'wait','img':'https://robotapi.chenhongshu.com/bqb/bannar3.jpg'}
        ]
    }
    #这个接口返回的是数组，即首页的三张图，其中code为fuck_robot的时候跳转到吵架之神，其他先不跳转
    """
    res_status,rjson = responser.get_param_check(request,['openid'])
    if res_status == 'success':
        return wechat_index_manager.get_bannars(rjson['openid'])
    else:
        return rjson

