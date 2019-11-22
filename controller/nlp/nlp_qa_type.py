# -*- coding: utf-8 -*-
# @Time    : 19-4-9 下午4:39
# @Author  : Redtree
# @File    : nlp_qa_type.py
# @Desc : nlp语料集合管理接口

from __init__ import app
from __init__ import  request
from service.nlp import nlp_qa_type_manager
from utils.http import responser

@app.route('/add_nlp_qa_type', endpoint='add_nlp_qa_type',methods=['POST'])
def add_nlp_qa_type():
    """
       @api {post} /add_nlp_qa_type 添加语料集
       @apiName sys_nlp_qa_type.add_nlp_qa_type
       @apiGroup nlp_qa_type
       @apiVersion 1.0.0

       @apiParam {string} user_id 当前用户id       *
       @apiParam {string} qa_code 语料集代码 *
       @apiParam {string} qa_name 语料集名称  *
       @apiParam {string} qa_welcome 欢迎语     *
       @apiParam {string} description 适用场景描述     *


       @apiSuccessExample Example data on success:
       {
           "code": 10000,
           "msg": "操作成功",
           "data": "success"
       }
       """
    res_status, rjson = responser.post_param_check(request, ['user_id', 'qa_code', 'qa_name','qa_welcome','description'])
    if res_status == 'success':
        return nlp_qa_type_manager.add_nlp_qa_type(rjson['user_id'], rjson['qa_code'], rjson['qa_name'],rjson['qa_welcome'],rjson['description'])
    else:
        return rjson



@app.route('/del_nlp_qa_type', endpoint='del_nlp_qa_type',methods=['POST'])
def del_nlp_qa_type():
    """
          @api {post} /del_nlp_qa_type 删除语料集
          @apiName sys_nlp_qa_type.del_nlp_qa_type
          @apiGroup nlp_qa_type
          @apiVersion 1.0.0

          @apiParam {list(string)} qa_code_list 语料集代号组  *

          @apiSuccessExample Example data on success:
          {
              "code": 10000,
              "msg": "操作成功",
              "data": "success"
          }
          """

    res_status, rjson = responser.post_param_check(request, ['qa_code_list'])
    if res_status == 'success':
        return nlp_qa_type_manager.del_nlp_qa_type(rjson['qa_code_list'])
    else:
        return rjson


@app.route('/get_nlp_qa_type', endpoint='get_nlp_qa_type',methods=['POST'])
def get_nlp_qa_type():
    """
                 @api {post} /get_nlp_qa_type 获取语料集列表 (新 get_role_nlp_qa_type)
                 @apiName sys_nlp_qa_type.get_nlp_qa_type
                 @apiGroup nlp_qa_type
                 @apiVersion 1.0.0

                 @apiParam {string} user_id 当前登录帐号   *
                 @apiParam {string} search 关键词搜错  *
                 @apiParam {string} page 页码     *

       @apiSuccessExample Example data on success:
       {
         "code": 10000,
         "msg": "操作成功",
         "data": "success"
       }
    """
    res_status, rjson = responser.post_param_check(request, ['user_id','search','page'])
    if res_status == 'success':
        return nlp_qa_type_manager.get_nlp_qa_type(rjson['user_id'],rjson['search'],rjson['page'])
    else:
        return rjson

@app.route('/update_nlp_qa_type', endpoint='update_nlp_qa_type',methods=['POST'])
def update_nlp_qa_type():
    """
                 @api {post} /update_nlp_qa_type 更新语料集基础信息
                 @apiName sys_nlp_qa_type.update_nlp_qa_type
                 @apiGroup nlp_qa_type
                 @apiVersion 1.0.0

                 @apiParam {string} user_id 当前用户id       *
                 @apiParam {string} qa_code 语料集代码 *
                 @apiParam {string} qa_name 语料集名称  *
                 @apiParam {string} qa_welcome 欢迎语     *
                 @apiParam {string} description 适用场景描述     *

                 @apiSuccessExample Example data on success:
                 {
                     "code": 10000,
                     "msg": "操作成功",
                     "data": "success"
                 }
                 """
    res_status, rjson = responser.post_param_check(request,
                                                   ['user_id', 'qa_code', 'qa_name', 'qa_welcome', 'description'])
    if res_status == 'success':
        return nlp_qa_type_manager.update_nlp_qa_type(rjson['user_id'], rjson['qa_code'], rjson['qa_name'],
                                                   rjson['qa_welcome'], rjson['description'])
    else:
        return rjson