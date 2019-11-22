# -*- coding: utf-8 -*-
# @Time    : 19-4-17 下午2:22
# @Author  : Redtree
# @File    : role_nlp_qa_type.py
# @Desc : 角色语料权限管理

from __init__ import app
from __init__ import  request
from service.admin import role_nlp_qa_type_manager
from utils.http import responser
from utils.decorator.token_maneger import auth_check

@app.route('/add_role_nlp_qa_type', endpoint='add_role_nlp_qa_type',methods=['POST'])
@auth_check
def add_role_nlp_qa_type():
    """
       @api {post} /add_role_nlp_qa_type 新增角色语料权限
       @apiName sys_user_app.add_role_nlp_qa_type
       @apiGroup role_nlp_qa_type
       @apiVersion 1.0.0

       @apiParam {string} role_code 角色代码         *
       @apiParam {string} qa_code 语料代码       *

       @apiSuccessExample Example data on success:
       {
           "code": 10000,
           "msg": "操作成功",
           "data": "success"
       }
       """
    res_status, rjson = responser.post_param_check(request, ['role_code', 'qa_code'])
    if res_status == 'success':
        return role_nlp_qa_type_manager.add_role_nlp_qa_type(rjson['role_code'], rjson['qa_code'])
    else:
        return rjson



@app.route('/del_role_nlp_qa_type', endpoint='del_role_nlp_qa_type',methods=['POST'])
@auth_check
def del_user_app():
    """
          @api {post} /del_role_nlp_qa_type 删除角色语料理关联
          @apiName sys_user_app.del_role_nlp_qa_type
          @apiGroup role_nlp_qa_type
          @apiVersion 1.0.0

          @apiParam {string} role_code 角色代码   *
          @apiParam {list(string)} qa_code_list 关联语料代码组  *

          @apiSuccessExample Example data on success:
          {
              "code": 10000,
              "msg": "操作成功",
              "data": "success"
          }
          """

    res_status, rjson = responser.post_param_check(request, ['role_code','qa_code_list'])
    if res_status == 'success':
        return role_nlp_qa_type_manager.del_role_nlp_qa_type(rjson['role_code'],rjson['qa_code_list'])
    else:
        return rjson


@app.route('/get_role_nlp_qa_type', endpoint='get_role_nlp_qa_type',methods=['POST'])
@auth_check
def get_role_nlp_qa_type():
    """
                 @api {post} /get_role_nlp_qa_type 获取角色语料表  (旧 get_nlp_qa_type)
                 @apiName sys_user_app.get_role_nlp_qa_type
                 @apiGroup role_nlp_qa_type
                 @apiVersion 1.0.0

                 @apiParam {string} role_code 角色代码   *
                 @apiParam {string} search 关键词搜错  *
                 @apiParam {string} page 页码     *

                 @apiSuccessExample Example data on success:
                 {
                     "code": 10000,
                     "msg": "操作成功",
                     "data": "success"
                 }
                 """
    res_status, rjson = responser.post_param_check(request, ['role_code','search','page'])
    if res_status == 'success':
        return role_nlp_qa_type_manager.get_role_nlp_qa_type(rjson['role_code'],rjson['search'],rjson['page'])
    else:
        return rjson


@app.route('/update_role_nlp_qa_type', endpoint='update_role_nlp_qa_type',methods=['POST'])
@auth_check
def update_role_nlp_qa_type():
    """
                 @api {post} /update_role_nlp_qa_type 修改角色语料权限类型
                 @apiName sys_user_app.update_role_nlp_qa_type
                 @apiGroup role_nlp_qa_type
                 @apiVersion 1.0.0

                 @apiParam {int} id 关系id (不可改)  *
                 @apiParam {int} auth_type 1读写 0只读，默认1   *

                 @apiSuccessExample Example data on success:
                 {
                     "code": 10000,
                     "msg": "操作成功",
                     "data": "success"
                 }
                 """
    res_status, rjson = responser.post_param_check(request, ['id','auth_type'])
    if res_status == 'success':
        return role_nlp_qa_type_manager.update_role_nlp_qa_type(rjson['id'],rjson['auth_type'])
    else:
        return rjson

@app.route('/getall_role_nlp_qa_type', endpoint='getall_role_nlp_qa_type',methods=['POST'])
@auth_check
def getall_role_nlp_qa_type():
    """
                 @api {post} /getall_role_nlp_qa_type 获取角色语料表(包含已授权未授权)
                 @apiName sys_user_app.getall_role_nlp_qa_type
                 @apiGroup role_nlp_qa_type
                 @apiVersion 1.0.0

                 @apiParam {string} role_code 角色代码   *

                 @apiSuccessExample Example data on success:
                 {
                     "code": 10000,
                     "msg": "操作成功",
                     "data": "success"
                 }
                 """
    res_status, rjson = responser.post_param_check(request, ['role_code'])
    if res_status == 'success':
        return role_nlp_qa_type_manager.get_role_all_nlp_qa_type(rjson['role_code'])
    else:
        return rjson