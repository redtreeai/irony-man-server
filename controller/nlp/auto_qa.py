# -*- coding: utf-8 -*-
# @Time    : 19-3-27 上午11:12
# @Author  : Redtree
# @File    : auto_qa.py
# @Desc :  自动QA相关接口

from __init__ import app
from __init__ import request
from service.nlp import auto_qa_manager
from utils.http import responser


@app.route('/auto_qa', endpoint='auto_qa', methods=['POST'])
def auto_qa():
    """
        @api {POST} /auto_qa 自动问答
        @apiName nlp_auto_qa.auto_qa
        @apiGroup auto_qa
        @apiVersion 1.0.0

        @apiParam {string} qa_code 关联应用代码 *
        @apiParam {string} input_text 提问内容 (开头若为'#TR#',则进行语言自动检测和翻译)*
        @apiParam {string} signature 签名，需要传参，值可以暂时为空串 *
        @apiParam {string} extra_data 额外数据

        @apiParamExample {json} 获取dashboard统计数据,填写对应的code到qa_code的参数中(具体以平台录入数据为标准，下表知识参考) :
        关于input_text 和 qa_code:
        1 通常情况下,input_text为自动问答内容，此时qa_code指代语料集
        比如:
        亿学介绍	yxinfo
        其余见数据库

        2  当input_text 为 #TR# 开头的时候, 则为翻译，此时qa_code为任意字符串

        3  当input_text 为 #TESTCN# 或 #TESTEN#开头时 ，qa_code对应xue_sys_pro的product_code
        比如:
        商务英语练考赛一体化平台	busengcontestt
        其余见数据库

        @apiSuccessExample Example data on success:
        {
         "code": 10000,
         "msg": "操作成功",
         "data": "回答内容"
        }
    """

    res_status, rjson = responser.post_param_check(request, ['qa_code', 'input_text', 'signature','extra_data'])

    if res_status == 'success':
        return auto_qa_manager.auto_qa(rjson['qa_code'], rjson['input_text'], rjson['signature'])
    else:
        return rjson


@app.route('/train_qa_model', endpoint='train_qa_model', methods=['GET'])
def train_qa_model():
    """
        @api {get} /train_qa_model 重新训练QA模型(此接口由管理人员调用，调试模型请勿使用)
        @apiName nlp_auto_qa.train_qa_model
        @apiGroup auto_qa
        @apiVersion 1.0.0

        @apiParam {string} qa_code 关联应用代码 *
        @apiParam {string} secret 训练密钥 zfkj123 *

        @apiParamExample {json} 获取dashboard统计数据,填写对应的code到app_code的参数中 :
        RULES = [
            {'qa_code': 'aicloud', 'name': 'AI实训云平台', 'description': '人工智能知识问答'},
            {'qa_code': 'busengdocu', 'name': '商务英语单证实训系统', 'description': ''},
            {'qa_code': 'busenglett', 'name': '商务英语函电实训系统', 'description': ''},
            {'qa_code': 'busengcbec', 'name': '跨境电商实战平台', 'description': ''},
            {'qa_code': 'busengint', 'name': '国际商务英语综合', 'description': ''},
            {'qa_code': 'busengvls', 'name': '商务英语视听说实训系统', 'description': ''},
            {'qa_code': 'busengexp', 'name': '体验职场商务英语实训系统', 'description': ''},
            {'qa_code': 'busengtra', 'name': '国际贸易实务实训系统', 'description': ''},
            {'qa_code': 'busengcontestt', 'name': '商务英语练考赛一体化平台', 'description': ''},
            {'qa_code': 'busengcontest', 'name': '商务英语实践技能竞赛平台', 'description': ''},
            {'qa_code': 'busengcommu', 'name': '国际商务沟通实训系统', 'description': ''},
            {'qa_code': 'busengcross', 'name': '跨文化交际实训系统', 'description': ''},
            {'qa_code': 'busengetiq', 'name': '国际商务礼仪实训系统', 'description': ''},
            {'qa_code': 'busengnego', 'name': '商务谈判教学实训平台', 'description': ''},
            {'qa_code': 'busengmark', 'name': '国际市场营销实训系统', 'description': ''},
            {'qa_code': 'buseng', 'name': '3D仿真商务英语综合实训系统', 'description': ''},
            {'qa_code': 'busengsce3d', 'name': '商务英语3D情景口语实训系统', 'description': ''},
            {'qa_code': 'esandtable', 'name': '商业沙盘实战平台-E沙盘', 'description': ''},
            {'qa_code': 'mshopcategory', 'name': '品类管理实战平台', 'description': ''},
            {'qa_code': 'mshopdisplayr', 'name': '3D仿真连锁门店商品陈列与空间设计实训竞赛系统', 'description': ''},
            {'qa_code': 'mshoploop', 'name': '连锁经营管理专业综合实训闭环平台', 'description': ''},
            {'qa_code': 'mshopn', 'name': '连锁门店运营实训系统', 'description': ''},
            {'qa_code': 'mshopsupert', 'name': '连锁经营创新创业实践教学平台', 'description': ''},
            {'qa_code': 'msuper3dn', 'name': '连锁企业王牌店长实务实训系统', 'description': ''},
            {'qa_code': 'busjap', 'name': '商务日语综合', 'description': ''},
            {'qa_code': 'busjapspe', 'name': '日语情景口语平台实训系统', 'description': ''},
            {'qa_code': 'busjaptes', 'name': '日语练考赛一体化平台', 'description': ''}
        ]

        @apiSuccessExample Example data on success:
        {
         "code": 10000,
         "msg": "操作成功",
         "data": "success"
        }
    """

    res_status, rjson = responser.get_param_check(request, ['qa_code', 'secret'])

    if res_status == 'success':
        if rjson['secret'] == 'zfkj123':
            # return 'unsupported'
            return auto_qa_manager.train_qa_model(rjson['qa_code'])
        else:
            return 'secret error'
    else:
        return rjson


@app.route('/train_all_model', endpoint='train_all_model', methods=['GET'])
def train_all_model():
    """
         @api {get} /train_all_model 重新训练所有QA模型(此接口由管理人员调用，调试模型请勿使用,接口停用)
         @apiName nlp_auto_qa.train_all_model
         @apiGroup auto_qa
         @apiVersion 1.0.0

         @apiParam {string} secret 训练密钥 zfkj123 *

         @apiSuccessExample Example data on success:
         {
             "code": 10000,
             "msg": "操作成功",
             "data": "success"
         }
     """

    res_status, rjson = responser.get_param_check(request, ['secret'])
    if res_status == 'success':
        if rjson['secret'] == 'zfkj123':
            # return 'unsupported'
            return '接口停用'
        else:
            return 'secret error'
    else:
        return rjson
