# -*- coding: utf-8 -*-
# @Time    : 19-12-20 下午5:06
# @Author  : Redtree
# @File    : ttt.py
# @Desc :



import time
from random import Random

def random_str(randomlength=32):  #随机字符串生成算法
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]

    return str
a = '6W7MmVLXCrPkyxfTUwelOKj3NQhSR9os'
b= a[0:10]
c = str(int(time.time()))
d = random_str(8)
e = (b+c+d)

print(e)
print(len(e))