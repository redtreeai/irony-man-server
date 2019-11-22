# -*- coding: utf-8 -*-
# @Time    : 19-3-27 上午10:32
# @Author  : Redtree
# @File    : auto_qa_manager.py
# @Desc :   自动QA服务

from __init__ import ROOT_PATH
from __init__ import DBSession_xxcxb,PAGE_LIMIT
from utils.nlp import docsim
from database.sqlalchemy.orm_models.zf_nlp_qa import Zf_nlp_qa
from utils.http import responser
import random

# 模型训练，一般需要在服务启动前训练
def train_qa_model(qa_code):
    try:
        #train_File_path = ''
        train_Dictionary_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Dictionary'
        train_Similarity_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Similarity'

        res = docsim.train(get_qa_dict(qa_code), train_Dictionary_path, train_Similarity_path)
        if res == 'success':
            return responser.send(10000, qa_code)
        else:
            return responser.send(60001)

    except Exception as e:
        return responser.send(60001)


def get_qa_dict(qa_code):
    #by mysql
    try:
        session = DBSession_xxcxb()
        info = session.query(Zf_nlp_qa).filter(Zf_nlp_qa.qa_code == str(qa_code)).all()
        if not info == 0 and not info == '':
            session.close()
            c_list = []
            for inf in info:
                c_obj = (inf.question, inf.answer)
                c_list.append(c_obj)
            return c_list
    except Exception as err:
        print(err)
        session.close()
        return []


def auto_qa(qa_code, input_text, signature):
    try:

        Dictionary_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Dictionary'
        Similarity_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Similarity'
        res = docsim.response(input_text, get_qa_dict(qa_code), Dictionary_path, Similarity_path)

        return responser.send(10000, res)
    except Exception as err :
        print(err)
        return responser.send(60003)


#基于语料库的问答
def keeppet_auto_qa(input_text):
    try:
        qa_code = 'keeppet'
        Dictionary_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Dictionary'
        Similarity_path = ROOT_PATH + '/resource/nlp/auto_qa/model/' + qa_code + '_Similarity'
        res = docsim.response(input_text, get_qa_dict(qa_code), Dictionary_path, Similarity_path)
        if res =='error':
            return keeppet_nice_responese()
        else:
            return res
    except Exception as err :
        return keeppet_nice_responese

#和谐回复
def keeppet_nice_responese():

    res_list = ['懒得理你','你牙齿上有韭菜']
    return random.choice(res_list)