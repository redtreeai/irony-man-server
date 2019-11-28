# -*- coding: utf-8 -*-
# @Time    : 18-11-7 下午3:56
# @Author  : Redtree
# @File    : orm_tool.py
# @Desc :  ORM 文件编写辅助工具，有空再升级


def var2json ():
    var_data = '''
    
 zfid = Column(Integer, primary_key=True)
    uid = Column(String(50))  #用户unionid
    nickname = Column(String(50))  #用户昵称
    avatar = Column(Text)  #头像
    gender = Column(Integer) #0:保密，1：男，2：女
    province = Column(String(50)) #省份
    city = Column(String(50)) #省份
    country = Column(String(50)) #省份
    is_vip = Column(Integer) #0不是1是
    vip_time = Column(Integer) #vip到期时间
    updated_time = Column(Integer) #纪录更新时间
    '''

    lines = var_data.split('\n')
    for l in lines:
        if l.__contains__('='):
            name = l.split('=')[0].replace(' ','')
            print('\"'+name+'\"'+' : '+'self.'+name+',')

#var2json()
