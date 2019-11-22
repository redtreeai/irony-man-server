# -*- coding: utf-8 -*-
# @Time    : 18-10-31 下午4:03
# @Author  : Redtree
# @File    : sys_role_menu.py
# @Desc :

from __init__ import app
from __init__ import  request
from service.admin import sys_role_menu_manager
from utils.http import responser
from utils.decorator.token_maneger import auth_check

@app.route('/add_role_menu', endpoint='add_role_menu',methods=['POST'])
@auth_check
def add_role_menu():
    """
       @api {post} /add_role_menu 创建角色菜单关联
       @apiName sys_role_menu.add_role_menu
       @apiGroup sys_role_menu
       @apiVersion 1.0.0

        @apiParam {user_id} user_id 角色帐号    *
        @apiParam {string} role_code 角色代码    *
       @apiParam {string} menu_code 菜单代码      *



       @apiSuccessExample Example data on success:
       {
           "code": 10000,
           "msg": "操作成功",
           "data": "success"
       }
       """

    res_status,rjson = responser.post_param_check(request, ['user_id','role_code', 'menu_code'])
    if res_status == 'success':
        return sys_role_menu_manager.add_role_menu(rjson['user_id'],rjson['role_code'], rjson['menu_code'])
    else:
        return rjson


@app.route('/del_role_menus', endpoint='del_role_menus',methods=['POST'])
@auth_check
def del_role_menu():
    """
          @api {post} /del_role_menus 删除角色菜单关联
          @apiName sys_role_menu.del_role_menus
          @apiGroup sys_role_menu
          @apiVersion 1.0.0

          @apiParam {string} user_id 当前登录角色帐号    *
         @apiParam {string} role_code 当前操作角色代码  *
        @apiParam {string} menu_code 当前操作菜单代码  *


          @apiSuccessExample Example data on success:
          {
              "code": 10000,
              "msg": "操作成功",
              "data": "success"
          }
          """

    res_status,rjson = responser.post_param_check(request, ['user_id','role_code','menu_code'])
    if res_status == 'success':
        return sys_role_menu_manager.del_role_menus(rjson['user_id'],rjson['role_code'],rjson['menu_code'])
    else:
        return rjson



@app.route('/get_role_menu_by_role_code', endpoint='get_role_menu_by_role_code',methods=['POST'])
@auth_check
def get_role_menu_by_role_code():
    """
                 @api {post} /get_role_menu_by_role_code 根据角色代码获取关联菜单
                 @apiName sys_role_menu.get_role_menu_by_role_code
                 @apiGroup sys_role_menu
                 @apiVersion 1.0.0

                 @apiParam {string} user_id 当前登录帐号  *
                 @apiParam {string} role_code 角色代码  *

                @apiSuccessExample Example data on success:
                 {
                     "code": 10000,
                     "msg": "操作成功",
                     "data": "success"
                 }
                 """

    res_status,rjson = responser.post_param_check(request, ['user_id','role_code','page'])
    if res_status == 'success':
        return sys_role_menu_manager.get_menucode_by_rolecode(rjson['user_id'], rjson['role_code'])
    else:
        return rjson

@app.route('/get_role_menu_by_user_id', endpoint='get_role_menu_by_user_id',methods=['POST'])
@auth_check
def get_role_menu_by_user_id():
    """
                 @api {post} /get_role_menu_by_user_id 根据用户id获取关联菜单
                 @apiName sys_role_menu.get_role_menu_by_user_id
                 @apiGroup sys_role_menu
                 @apiVersion 1.0.0

                 @apiParam {string} user_id 当前登录帐号  *
                 @apiParam {string} code_search 代码搜索  *


                 @apiSuccessExample Example data on success:
                 {
                     "code": 10000,
                     "msg": "操作成功",
                     "data": "success"
                 }
                 """
    res_status,rjson = responser.post_param_check(request, ['user_id', 'code_search'])
    if res_status == 'success':
        return sys_role_menu_manager.get_menucode_by_userid(rjson['user_id'], rjson['code_search'])
    else:
        return rjson



