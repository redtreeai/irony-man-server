# -*- coding: utf-8 -*-
# @Time    : 18-7-12 下午4:17
# @Author  : Redtree
# @File    : sys_user.py
# @Desc : 用户行为操作

from __init__ import app
from __init__ import  request
from __init__ import make_response
from __init__ import TOKEN_AHEAD
import datetime
from service.admin import sys_user_manager
from utils.decorator import token_maneger
from utils.decorator.token_maneger import auth_check
from utils.http import responser

@app.route('/getsession',endpoint='getsession',methods=['POST'])
def getsession():
    """
            @api {post} /getsession 用户登录后获取session
            @apiName sys_user.getsession
            @apiGroup sys_user
            @apiVersion 1.0.0

            @apiParam {string} user_id 用户名   *

            @apiSuccessExample Example data on success:
            {

            }
    """
    try:
          outdate = datetime.datetime.today() + datetime.timedelta(days=1)
          res_status, rjson = responser.post_param_check(request, ['user_id'])
          if res_status == 'success':
              response = make_response(str(TOKEN_AHEAD))
              response.set_cookie('key', rjson['user_id'], expires=outdate)
              response.set_cookie('token', token_maneger.generate_token(rjson['user_id']), expires=outdate)
              return response
          else:
              return 'error'
    except Exception as err:
          print('session刷新失败'+str(err))
          return 'error'

@app.route('/check_login', endpoint='check_login',methods=['POST'])
def check_login():
    """
    @api {post} /check_login 用户登录
    @apiName sys_user.checklogin
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {string} user_id 用户名   *
    @apiParam {string} password 登录密码      *

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {
            "user_id":"zfadmin"   #用户id
            "nickname": 掌飞小智, #用户昵称
            "role_name": "超级管理员", #用户角色名
            "menu_code": [sysinfo], #菜单列表
        }
    }
    """
    res_status,rjson = responser.post_param_check(request,['user_id','password'])
    if res_status == 'success':
        return sys_user_manager.check_login(rjson['user_id'], rjson['password'])
    else:
        return rjson

@app.route('/add_user', endpoint='add_user',methods=['POST'])
@auth_check
def add_user():
    """
    @api {post} /add_user 创建用户
    @apiName sys_user.add_user
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {string} user_id 用户名 (20位以内 英文+数字)       *
    @apiParam {string} password 登录密码      *
    @apiParam {string} nickname 昵称       *
    @apiParam {int} role_code 角色代码      *  (puser/editor)
    @apiParam {string} created_user_id 创建者user_id,默认为当前操作用户      *
    @apiParam {int} gender 性别   0其他，1男，2女，3保密   *
    @apiParam {string} phone 电话号码      *
    @apiParam {string} email 邮箱      *
    @apiParam {string} remark 备注      *
    @apiParam {int} is_active 是否激活 1激活 0封禁      *
    @apiParam {string} org_code 机构代码      *


    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": "user_id"
    }
    """

    res_status, rjson = responser.post_param_check(request,['user_id', 'password','nickname','role_code','created_user_id','gender','phone','email','remark','is_active','org_code'])
    if res_status == 'success':
        return sys_user_manager.add_sys_user(rjson['user_id'], rjson['password'], rjson['nickname'], rjson['role_code'], rjson['created_user_id'],rjson['gender'],
                                             rjson['phone'], rjson['email'], rjson['remark'], rjson['is_active'],rjson['org_code'])
    else:
        return rjson



@app.route('/del_user', endpoint='del_user',methods=['POST'])
@auth_check
def del_user():
    """
    @api {post} /del_user 删除用户
    @apiName sys_user.del_user
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {list(string)} id_list 用户user_id列表   *

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {

        }
    }
    """

    res_status, rjson = responser.post_param_check(request, ['id_list'])
    if res_status == 'success':
        return sys_user_manager.del_sys_user(rjson['id_list'])
    else:
        return rjson


@app.route('/get_user', endpoint='get_user',methods=['POST'])
@auth_check
def get_user():
    """
    @api {post} /get_user 查询用户
    @apiName sys_user.get_user
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {string} user_id 用户名   *
    @apiParam {int} page 页数        *     1
    @apiParam {string} id_search 用户账号  *  ''
    @apiParam {string} name_search 用户名  *   ''
    @apiParam {string} phone_search 号码查询  *   ''
    @apiParam {string} role_code 角色  *     schooladmin
    @apiParam {int} is_active 激活状态  *     1 或0 默认1

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {

        }
    }
    """

    res_status, rjson = responser.post_param_check(request, ['user_id','is_active','id_search','name_search','phone_search','page','role_code'])
    if res_status == 'success':
        return sys_user_manager.get_sys_user(rjson['user_id'], rjson['is_active'], rjson['id_search'], rjson['name_search'],rjson['phone_search'],  rjson['page'], rjson['role_code'])
    else:
        return rjson


@app.route('/update_user', endpoint='update_user',methods=['POST'])
@auth_check
def update_user():
    """
    @api {post} /update_user 更新用户
    @apiName sys_user.update_user
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {string} user_id 用户账号   *
    @apiParam {string} role_code 角色代码   (必须是已有角色类型)
    @apiParam {string} nickname 昵称 *
    @apiParam {string} real_name  真实姓名*
    @apiParam {string} id_card  身份证号码*
    @apiParam {int} birthday  生日*
    @apiParam {string} email  邮箱*
    @apiParam {string} head_img  头像*
    @apiParam {String} phone  电话号码 不能超过15位*
    @apiParam {int} gender  0其他 1男 2 女 3 保密*
    @apiParam {string} introduction 个人简介*
    @apiParam {int} is_active  1 激活 2 禁用

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {

        }
    }
    """

    res_status, rjson = responser.post_param_check(request,
                                                   ['user_id','role_code', 'nickname', 'real_name', 'id_card', 'birthday', 'email',
                                                    'head_img', 'phone', 'gender', 'introduction','is_active'])
    if res_status == 'success':
        return sys_user_manager.update_user(rjson['user_id'], rjson['role_code'],rjson['nickname'], rjson['real_name'], rjson['id_card'],
                                            rjson['birthday']
                                            , rjson['email'], rjson['head_img'], rjson['phone'], rjson['gender'],
                                            rjson['introduction'],rjson['is_active'])
    else:
        return rjson



@app.route('/reset_pwd', endpoint='reset_pwd',methods=['POST'])
@auth_check
def reset_pwd():
    """
    @api {post} /reset_pwd 重置密码
    @apiName sys_user.reset_pwd
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {string} user_id 用户账号   *
    @apiParam {string} password 新密码    *

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {

        }
    }
    """

    res_status, rjson = responser.post_param_check(request, ['user_id', 'password'])
    if res_status == 'success':
        return sys_user_manager.reset_password(rjson['user_id'], rjson['password'])
    else:
        return rjson


@app.route('/ban_user',endpoint='ban_user', methods=['POST'])
@auth_check
def ban_user():
    """
    @api {post} /ban_user 禁止用户
    @apiName sys_user.ban_user
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {list} id_list 用户账号列表    *
    @apiParam {int} ban_flag 禁止状态值    *

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {

        }
    }
    """

    res_status, rjson = responser.post_param_check(request, ['id_list', 'ban_flag'])
    if res_status == 'success':
        return sys_user_manager.reset_password(rjson['id_list'], rjson['ban_flag'])
    else:
        return rjson

@app.route('/get_user_data', endpoint='get_user_data',methods=['POST'])
@auth_check
def get_user_by_id():
    """
    @api {POST} /get_user_data 查询指定用户
    @apiName sys_user.get_user_data
    @apiGroup sys_user
    @apiVersion 1.0.0

    @apiParam {string} user_id 操作用户名   *

    @apiSuccessExample Example data on success:
    {
        "code": 10000,
        "msg": "操作成功",
        "data": {

        }
    }
    """

    res_status, rjson = responser.post_param_check(request, ['user_id'])
    if res_status == 'success':
        return sys_user_manager.get_user_data(rjson['user_id'])
    else:
        return rjson