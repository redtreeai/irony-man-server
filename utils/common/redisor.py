# -*- coding: utf-8 -*-
# @Time    : 19-5-5 下午2:59
# @Author  : Redtree
# @File    : redisor.py
# @Desc :  基于redis的数据操控工具
from utils.decorator.dasyncio import async_call

#redis更新操作
@async_call
def update_redis_kv(redis_obj, r_key, r_value):
    try:
        redis_obj.set(r_key, r_value)
        return True
    except Exception as err:
        return False


#redis取值操作
def get_redis_value_by_key(redis_obj, r_key):
    try:
        return redis_obj[r_key]
    except Exception as err:
        return False


#redis删除操作
def delete_redis_key(redis_obj, r_key):
    try:
        redis_obj.delete(r_key)
        return True
    except Exception as err:
        return False