# -*- coding: utf-8 -*-
# @Time    : 19-3-13 下午1:42
# @Author  : Redtree
# @File    : main.py
# @Desc :

from gensim import corpora
from gensim.similarities import Similarity
import jieba

#模型训练
def train(scene_file_path):
    try:
        print('正在读取训练材料')
        qa_dict = get_corpora(scene_file_path)
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
        similarity = Similarity('data/Similarity', corpus, num_features=40000)
        print('训练完毕')
        print('正在保存字典')
        dictionary.save('data/Dictionary')
        print('字典保存完成')
        print('正在保存模型')
        similarity.save('data/Similarity')
        print('模型保存完毕')
        return 'success'
    except:
        print('模型训练失败')
        return 'error'

# getcorpora需要根据不同的场景需求重写，下面是一个模板，它将读取一个语料文件并生成字典数组
def get_corpora(scene_file_path):
   f = open(scene_file_path)
   lines = f.readlines()
   clist=[]
   for line in lines:
       q_word = line.split('|')[0]
       a_word = line.split('|')[1]
       cobj=(q_word,a_word)
       clist.append(cobj)
   return clist


#多个模型的话后面要采取预加载
def response(text,scene_file_path,docsim_Dictionary,docsim_Similarity):
    qa_dict =get_corpora(scene_file_path)
    test_text = list(jieba.cut(text))
    dictionary = corpora.Dictionary.load(docsim_Dictionary)
    similarity = Similarity.load(docsim_Similarity)
    test_corpora = dictionary.doc2bow(test_text)
    similarity.num_best = 1
    try:
        res = similarity[test_corpora]
        #获取最相似
        similary_value = res[0][1]  # 相似度
        # print(similary_value)
        # if similary_value<=0.8:
        #     return '你牙齿里有根青菜'
        match_outword = str(qa_dict[int(res[0][0])][1])  # 匹配输出/home/chs/project/ai_project/yixue_aiem/
        #print(similary_value, match_outword)
        return match_outword

    except :
        return '你牙齿里有根青菜！'

if __name__ == '__main__':
    #重新训练语料
    train('data/speech.txt')
    chat_flag = True
    print('开始嘲讽我吧，哼哼，我会反击你的哟'+'\n')
    while chat_flag==True:
        ip = input('\n')
        r = response(ip, 'data/speech.txt', 'data/Dictionary', 'data/Similarity')
        print(r)