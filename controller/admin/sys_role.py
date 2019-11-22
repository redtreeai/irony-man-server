# -*- coding: utf-8 -*-
# @Time    : 18-7-12 下午4:17
# @Author  : Redtree
# @File    : sys_user.py
# @Desc : 角色行为操作

from __init__ import app
from __init__ import  request
from service.admin import sys_role_manager
from utils.http import responser
from utils.decorator.token_maneger import auth_check

@app.route('/add_role', endpoint='add_role',methods=['POST'])
@auth_check
def add_role():
    """
       @api {post} /add_role 添加角色
       @apiName sys_role.add_role
       @apiGroup sys_role
       @apiVersion 1.0.0

        @apiParam {string} code 角色代号         *
        @apiParam {string} name 角色名称         *
       @apiParam {string} user_id 创建用户帐号     *

       @apiSuccessExample Example data on success:
       {
           "code": 10000,
           "msg": "操作成功",
           "data": "success"
       }
       """
    res_status, rjson = responser.post_param_check(request, ['code', 'name', 'user_id'])
    if res_status == 'success':
        return sys_role_manager.add_role(rjson['code'], rjson['name'], rjson['user_id'])
    else:
        return rjson



@app.route('/del_role', endpoint='del_role',methods=['POST'])
@auth_check
def del_role():
    """
          @api {post} /del_role 删除角色
          @apiName sys_role.del_role
          @apiGroup sys_role
          @apiVersion 1.0.0

          @apiParam {list(string)} role_code_list 角色代号组  *

          @apiSuccessExample Example data on success:
          {
              "code": 10000,
              "msg": "操作成功",
              "data": "success"
          }
          """

    res_status, rjson = responser.post_param_check(request, ['role_code_list'])
    if res_status == 'success':
        return sys_role_manager.del_role(rjson['role_code_list'])
    else:
        return rjson

@app.route('/ban_role',endpoint='ban_role', methods=['POST'])
@auth_check
def ban_role():
    """
              @api {post} /ban_role 禁用角色
              @apiName sys_role.ban_role
              @apiGroup sys_role
              @apiVersion 1.0.0

              @apiParam {list} role_code_list 角色代号组   *
              @apiParam {int} status 禁用符号 0为通过 1为禁止

              @apiSuccessExample Example data on success:
              {
                  "code": 10000,
                  "msg": "操作成功",
                  "data": "success"
              }
              """

    res_status, rjson = responser.post_param_check(request, ['role_code_list','status'])
    if res_status == 'success':
        return sys_role_manager.ban_role(rjson['role_code_list'],rjson['status'])
    else:
        return rjson



@app.route('/get_role_list', endpoint='get_role_list',methods=['POST'])
@auth_check
def get_role_list():
    """
                 @api {post} /get_role_list 获取角色列表
                 @apiName sys_role.get_role_list
                 @apiGroup sys_role
                 @apiVersion 1.0.0

                 @apiParam {string} user_id 当前登录帐号   *

                 @apiSuccessExample Example data on success:
                 {
                     "code": 10000,
                     "msg": "操作成功",
                     "data": "success"
                 }
                 """
    res_status, rjson = responser.post_param_check(request, ['user_id'])
    if res_status == 'success':
        return sys_role_manager.get_role_list(rjson['user_id'])
    else:
        return rjson

