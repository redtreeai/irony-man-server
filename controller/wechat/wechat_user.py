# -*- coding: utf-8 -*-
# @Time    : 19-11-28 下午5:49
# @Author  : Redtree
# @File    : wechat_user.py
# @Desc :


from __init__ import app
from __init__ import  request
from service.wechat import wechat_user_manager
from utils.http import responser


@app.route('/update_userinfo', endpoint='update_userinfo',methods=['POST'])
def update_userinfo():
    """
    @api {post} /update_userinfo 更新用户数据到服务端(首次登录或过期后登录调用)
    @apiName wechat.update_userinfo
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid
    @apiParam {string} nickname 昵称
    @apiParam {string} avatar 头像
    @apiParam {int} gender 性别 0:保密，1：男，2：女
    @apiParam {string} province 省
    @apiParam {string} city 市
    @apiParam {string} country 国

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
        }
    }
    """
    res_status,rjson = responser.post_param_check(request,['openid','nickname','avatar','gender','province','city','country'])
    if res_status == 'success':
        return wechat_user_manager.update_userinfo(rjson['openid'],rjson['nickname'],rjson['avatar'],rjson['gender'],rjson['province'],rjson['city'],rjson['country'])
    else:
        return rjson



@app.route('/get_user_data', endpoint='get_user_data',methods=['POST'])
def get_user_data():
    """
    @api {post} /wechat_checklogin 获取服务端的用户信息
    @apiName wechat.wechat_checklogin
    @apiGroup wechat
    @apiVersion 1.0.0

    @apiParam {string} openid

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
         openid = Column(String(50))  # 用户openid
        nickname = Column(String(50))  # 用户昵称
        avatar = Column(Text)  # 头像
        gender = Column(Integer)  # 0:保密，1：男，2：女
        province = Column(String(50))  # 省份
        city = Column(String(50))  # 市区
        country = Column(String(50))  # 国
        is_vip = Column(Integer)  # 0不是1是
        vip_time = Column(Integer)  # vip到期时间
        created_time Column(Integer) #纪录创建时间
        updated_time = Column(Integer)  # 纪录更新时间
        }
    }
    """
    res_status,rjson = responser.post_param_check(request,['openid'])
    if res_status == 'success':
        return wechat_user_manager.get_user_data(rjson['openid'])
    else:
        return rjson




