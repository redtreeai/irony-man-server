# -*- coding: utf-8 -*-
# @Time    : 18-11-7 下午3:56
# @Author  : Redtree
# @File    : orm_tool.py
# @Desc :  ORM 文件编写辅助工具，有空再升级


def var2json ():
    var_data = '''
    
zfid = Column(Integer, primary_key=True)
    app_code = Column(String(50))  # app代码
    qa_code = Column(String(50))  # 语料代码
    question = Column(Text)  # 输入
    answer = Column(Text)  # 输出
    created_time = Column(Integer)
    updated_time = Column(Integer)
    updated_user_id = Column(String(20))  # 更新信息的用户id
    org_code = Column(String(50))  # 机构代码
    org_name = Column(String(50))  # 机构名称
    app_user_id = Column(String(50))
    app_user_sex = Column(String(10))
    app_user_name = Column(String(50))
    app_user_phone = Column(String(50))


    '''

    lines = var_data.split('\n')
    for l in lines:
        if l.__contains__('='):
            name = l.split('=')[0].replace(' ','')
            print('\"'+name+'\"'+' : '+'self.'+name+',')

#var2json()
