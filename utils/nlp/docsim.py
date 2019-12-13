# -*- coding: utf-8 -*-
# @Time    : 19-1-24 上午9:45
# @Author  : Redtree
# @File    : docsim.py
# @Desc :

from gensim import corpora
from gensim.similarities import Similarity
import jieba
import random

# 模型训练
def train(qa_dict, train_Dictionary_path, train_Similarity_path):
    try:
        print('正在读取训练材料')
        #qa_dict = get_corpora(train_File_path)
        print('正在重新训练模型')
        # 生成单词向量
        corpora_documents = []
        for item_text in qa_dict:
            item_text = item_text[0]
            item_str = list(jieba.cut(item_text))
            corpora_documents.append(item_str)
        # 生成字典和向量语料
        dictionary = corpora.Dictionary(corpora_documents)
        # dictionary.save('docsim_corpora')
        corpus = [dictionary.doc2bow(text) for text in corpora_documents]
        similarity = Similarity(train_Similarity_path, corpus, num_features=40000)
        print('训练完毕')
        print('正在保存字典')
        dictionary.save(train_Dictionary_path)
        print('字典保存完成')
        print('正在保存模型')
        similarity.save(train_Similarity_path)
        print('模型保存完毕')
        return 'success'
    except Exception as err:
        print(err)
        print('知识点睛模型训练失败')
        return 'error'


# getcorpora需要根据不同的场景需求重写，下面是一个模板，它将读取一个语料文件并生成字典数组
def get_corpora(scene_file_path):
    f = open(scene_file_path)
    lines = f.readlines()
    clist=[]

    for line in lines:
        q_word = line.split('|')[0]
        a_word = line.split('|')[1]
        cobj = (q_word, a_word)
        clist.append(cobj)
    return clist


# 多个模型的话后面要采取预加载
def response(text,qa_dict, docsim_Dictionary, docsim_Similarity):
    #qa_dict = get_corpora(scene_file_path)
    #进入匹配前要去除非英文要素
    test_text = list(jieba.cut(text))
    dictionary = corpora.Dictionary.load(docsim_Dictionary)
    similarity = Similarity.load(docsim_Similarity)
    test_corpora = dictionary.doc2bow(test_text)
    similarity.num_best = 1
    try:
        res = similarity[test_corpora]
        #获取最相似
        similary_value = res[0][1]  # 相似度
        match_outword = str(qa_dict[int(res[0][0])][1])
        #print(similary_value, match_outword)
        if similary_value>=0.6:
            return match_outword
        else:
            return nice_responese()

    except Exception as e:
        return nice_responese()


#和谐回复
def nice_responese():

    res_list = ['懒得理你','你牙齿上有韭菜','你牙齿好黄啊','看你说的唾沫横飞的，给你个喇叭啊？','你是铅笔盒还是咋地，怎么那么能装笔啊?',' 你是在自我介绍吗',
                '说完了吗，需要给你支话筒嘛。','有种你就再吠一声','嘴巴那么毒，心里一定有很多苦吧。','我给你十秒钟的时间，立刻从我的世界里消失，否则我会让你明白我是一个文武双全的人!']
    return random.choice(res_list)