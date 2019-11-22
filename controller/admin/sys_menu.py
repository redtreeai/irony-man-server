# -*- coding: utf-8 -*-
# @Time    : 18-10-31 下午4:03
# @Author  : Redtree
# @File    : sys_menu.py
# @Desc :

from __init__ import app
from __init__ import  request
from service.admin import sys_menu_manager
from utils.http import responser
from utils.decorator.token_maneger import auth_check

@app.route('/add_menu',endpoint='add_menu', methods=['POST'])
@auth_check
def add_menu():
    """
       @api {post} /add_menu 新建菜单
       @apiName sys_menu.add_menu
       @apiGroup sys_menu
       @apiVersion 1.0.0

       @apiParam {string} code 菜单代码    *
       @apiParam {string} comment 菜单描述      *
       @apiParam {int} parent_code 父级菜单代码    *
       @apiParam {int} is_admin 是否是后台菜单 0为否 1为是     *

       @apiSuccessExample Example data on success:
       {
           "code": 10000,
           "msg": "操作成功",
           "data": "success"
       }
    """

    res_status, rjson = responser.post_param_check(request, ['code', 'comment', 'parent_code', 'is_admin'])
    if res_status == 'success':
        return sys_menu_manager.add_menu(rjson['code'], rjson['comment'], rjson['parent_code'], rjson['is_admin'])
    else:
        return rjson

@app.route('/del_menu', endpoint='del_menu',methods=['POST'])
@auth_check
def del_menu():
    """
        @api {post} /del_menu 删除菜单
        @apiName sys_menu.del_menu
        @apiGroup sys_menu
        @apiVersion 1.0.0

        @apiParam {list(string)} menu_code_list 菜单代码组  *

        @apiSuccessExample Example data on success:
        {
              "code": 10000,
              "msg": "操作成功",
              "data": "success"
        }
    """
    res_status, rjson = responser.post_param_check(request, ['menu_code_list'])
    if res_status == 'success':
        return sys_menu_manager.del_menus(rjson['menu_code_list'])
    else:
        return rjson


@app.route('/get_menus', endpoint='get_menus',methods=['POST'])
@auth_check
def get_menus():
    """
        @api {post} /get_menus 获取菜单列表
        @apiName sys_menu.get_menus
        @apiGroup sys_menu
        @apiVersion 1.0.0

        @apiParam {string} user_id 当前登录帐号  *
        @apiParam {string} code_search 代码搜索  *
        @apiParam {int} is_top 1 顶级菜单 *
        @apiParam {int} page 页码  *


        @apiSuccessExample Example data on success:
         {
             "code": 10000,
             "msg": "操作成功",
             "data": "success"
         }
    """
    res_status, rjson = responser.post_param_check(request, ['user_id', 'code_search', 'is_top','page'])
    if res_status == 'success':
        return sys_menu_manager.get_menus(rjson['user_id'], rjson['code_search'], rjson['is_top'],rjson['page'])
    else:
        return rjson

@app.route('/get_role_all_menus', endpoint='get_role_all_menus',methods=['POST'])
@auth_check
def get_role_all_menus():
    """
        @api {post} /get_role_all_menus 获取所有菜单列表
        @apiName sys_menu.get_all_menus
        @apiGroup sys_menu
        @apiVersion 1.0.0

        @apiParam {string} role_code 当前操作关联角色代码  *
        @apiParam {string} admin_user_id 当前登录帐号  *


        @apiSuccessExample Example data on success:
         {
             "code": 10000,
             "msg": "操作成功",
             "data": "success"
         }
    """
    res_status, rjson = responser.post_param_check(request, ['role_code','admin_user_id'])
    if res_status == 'success':
        return sys_menu_manager.get_role_all_menus(rjson['role_code'],rjson['admin_user_id'])
    else:
        return rjson

@app.route('/update_menu', endpoint='update_menu',methods=['POST'])
@auth_check
def update_menu():
    """
        @api {post} /update_menu 更新菜单信息
        @apiName sys_menu.update_menu
        @apiGroup sys_menu
        @apiVersion 1.0.0

        @apiParam {string} code 菜单代码
        @apiParam {string} comment 菜单描述
        @apiParam {string} parent_code 父级菜单代码


        @apiSuccessExample Example data on success:
        {
            "code": 10000,
            "msg": "操作成功",
            "data": {

            }
        }
    """
    res_status, rjson = responser.post_param_check(request, ['code', 'comment', 'parent_code'])
    if res_status == 'success':
        return sys_menu_manager.update_menu(rjson['code'], rjson['comment'], rjson['parent_code'])
    else:
        return rjson



