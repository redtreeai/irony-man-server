# -*- coding: utf-8 -*-
# @Time    : 19-4-9 下午5:22
# @Author  : Redtree
# @File    : nlp_qa.py
# @Desc : 语料问答操作接口

from __init__ import app
from __init__ import  request
from service.nlp import nlp_qa_manager
from utils.http import responser
from utils.decorator.token_maneger import auth_check

@app.route('/add_nlp_qa', endpoint='add_nlp_qa',methods=['POST'])
@auth_check
def add_nlp_qa():
    """
       @api {post} /add_nlp_qa 添加语料问答
       @apiName sys_nlp_qa.add_nlp_qa
       @apiGroup nlp_qa
       @apiVersion 1.0.0

       @apiParam {string} user_id 当前用户id       *
       @apiParam {string} qa_code 语料问答代码 *
       @apiParam {string} question 提问内容  *
       @apiParam {string} answer 回答内容     *


       @apiSuccessExample Example data on success:
       {
           "code": 10000,
           "msg": "操作成功",
           "data": "success"
       }
    """
    res_status, rjson = responser.post_param_check(request, ['user_id', 'qa_code', 'question','answer'])
    if res_status == 'success':
        return nlp_qa_manager.add_nlp_qa(rjson['user_id'], rjson['qa_code'], rjson['question'],rjson['answer'])
    else:
        return rjson



@app.route('/del_nlp_qa', endpoint='del_nlp_qa',methods=['POST'])
@auth_check
def del_nlp_qa():
    """
        @api {post} /del_nlp_qa 删除语料问答
        @apiName sys_nlp_qa.del_nlp_qa
        @apiGroup nlp_qa
        @apiVersion 1.0.0

        @apiParam {list(int)} zfid_list 语料问答id组  *

        @apiSuccessExample Example data on success:
        {
              "code": 10000,
              "msg": "操作成功",
              "data": "success"
        }
    """

    res_status, rjson = responser.post_param_check(request, ['zfid_list'])
    if res_status == 'success':
        return nlp_qa_manager.del_nlp_qa(rjson['zfid_list'])
    else:
        return rjson


@app.route('/get_nlp_qa', endpoint='get_nlp_qa',methods=['POST'])
@auth_check
def get_nlp_qa():
    """
       @api {post} /get_nlp_qa 获取语料问答列表
       @apiName sys_nlp_qa.get_nlp_qa
       @apiGroup nlp_qa
       @apiVersion 1.0.0

       @apiParam {string} qa_code 语料问答代码 *
       @apiParam {string} search 关键词搜错  *
       @apiParam {string} page 页码     *

       @apiSuccessExample Example data on success:
       {
         "code": 10000,
         "msg": "操作成功",
         "data": "success"
       }
    """
    res_status, rjson = responser.post_param_check(request, ['qa_code','search','page'])
    if res_status == 'success':
        return nlp_qa_manager.get_nlp_qa(rjson['qa_code'],rjson['search'],rjson['page'])
    else:
        return rjson


@app.route('/get_nlp_qa_count', endpoint='get_nlp_qa_count',methods=['POST'])
@auth_check
def get_nlp_qa_count():
    """
       @api {post} /get_nlp_qa_count 获取指定语料数量统计
       @apiName sys_nlp_qa.get_nlp_qa_count
       @apiGroup nlp_qa
       @apiVersion 1.0.0

       @apiParam {string} qa_code 语料问答代码 *

       @apiSuccessExample Example data on success:
       {
         "code": 10000,
         "msg": "操作成功",
         "data": "success"
       }
    """
    res_status, rjson = responser.post_param_check(request, ['qa_code'])
    if res_status == 'success':
        return nlp_qa_manager.get_nlp_qa_count(rjson['qa_code'])
    else:
        return rjson


@app.route('/update_nlp_qa', endpoint='update_nlp_qa',methods=['POST'])
@auth_check
def update_nlp_qa():
    """
         @api {post} /update_nlp_qa 更新语料问答基础信息
         @apiName sys_nlp_qa.update_nlp_qa
         @apiGroup nlp_qa
         @apiVersion 1.0.0

         @apiParam {string} user_id 当前用户id       *
         @apiParam {int} zfid 语料问答id *
         @apiParam {string} question 提问内容  *
         @apiParam {string} answer 回答内容     *

         @apiSuccessExample Example data on success:
         {
             "code": 10000,
             "msg": "操作成功",
             "data": "success"
         }
    """
    res_status, rjson = responser.post_param_check(request,
                                                   ['user_id', 'zfid', 'question', 'answer'])
    if res_status == 'success':
        return nlp_qa_manager.update_nlp_qa(rjson['user_id'], rjson['zfid'], rjson['question'],
                                                   rjson['answer'])
    else:
        return rjson

@app.route('/add_nlp_qa_excel', endpoint='add_nlp_qa_excel',methods=['POST'])
def add_nlp_qa_excel():
    """
       @api {post} /add_nlp_qa_excel 添加语料问答(excel)
       @apiName sys_nlp_qa.add_nlp_qa_excel
       @apiGroup nlp_qa
       @apiVersion 1.0.0

       @apiParam {string} user_id:  上传用户 *
       @apiParam {file} file_stream:  上传文件流 *
       @apiParam {string} file_name: 文件名 规范待定 *
       @apiParam {string} file_type: 文件类型 xlsx/docx *
       @apiParam {string} directory:  文件目录(本接口写qa_xlsx) *


       @apiSuccessExample Example data on success:
       {
           "code": 10000,
           "msg": "操作成功",
           "data": "success"
       }
    """
    try:
        file_stream = request.files['file_stream']  # 未限制文件大小
        user_id = str(request.form.get("user_id"))
        file_name = str(request.form.get("file_name"))
        file_type = str(request.form.get("file_type"))
        directory = str(request.form.get("directory"))

        return nlp_qa_manager.xlsx2sql(user_id,file_stream,file_name,file_type,directory)

    except:
        return responser.send(20005)
