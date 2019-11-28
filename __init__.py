# -*- coding: utf-8 -*-
'''
 Flask 初始化配置文件,包含基本配置，ORM，数据缓存，模型预加载，控制器注册等，注意业务逻辑顺序
'''
from flask_cors import CORS  #添加CORS组件 允许跨域访问
from flask import Flask, request,make_response,send_from_directory
import os
import yaml
import redis

'''
Flask基础配置部分
'''
print('正在初始化Flask基础服务')
# 初始化Flask对象
app = Flask(__name__)
# 初始化session 会话  需要配置key
app.secret_key = '\xca\x0c\x86\x04\x98@\x02b\x1b7\x8c\x88]\x1b\xd7"+\xe6px@\xc3#\\'
#实例化 cors
CORS(app, supports_credentials=True)
#其他组件注册
request = request
make_response = make_response
send_from_directory = send_from_directory

'''
适应性配置，方便本地调试和部署线上
'''

print('正在读取适应性配置')
#获取服务器基本配置信息
setting = yaml.load(open('setting.yaml'))
#项目版本
VERSION = setting['VERSION']
SERVER_IP = setting['SERVER_IP']

#小程序信息配置
WECHAT_APPID = setting['WECHAT_APPID']
WECHAT_APPSECRET = setting['WECHAT_APPSECRET']

# 数据库常量配置
PAGE_LIMIT = int(setting['PAGE_LIMIT'])
DEFAULT_PAGE = int(setting['DEFAULT_PAGE'])
USER_SALT_LENGTH = int(setting['USER_SALT_LENGTH'])
#字符串编码格式
STRING_CODE = setting['STRING_CODE']
#加密方式名
ENCRYPTION_SHA1 =setting['ENCRYPTION_SHA1']
#token过期时间配置
TOKEN_EXPIRE = int(setting['TOKEN_EXPIRE'])
#token提前校验时间配置
TOKEN_AHEAD = int(setting['TOKEN_AHEAD'])

#获取部署目录,ROOT_PATH即可作为工程中的绝对路径根目录，方便业务逻辑调用
ROOT_PATH = os.popen('pwd','r',1).read()
ROOT_PATH = str(ROOT_PATH).replace('\n','')

'''
数据库对象的创建和预加载,包含Redis/MongoDB等皆应在此提前实例化，如果需要从resource预先缓存数据，
例如读取txt/csv等文件，也可以在此处预先加载，以供全局调用。
'''

#加载redis
print('正在加载redis客户端')
redis_client = redis.Redis(host='localhost', port=6379, decode_responses=True)
print('成功')

print('正在链接mysql数据库')
from sqlalchemy import create_engine  #加载配置文件内容
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database.sqlalchemy import xxcxb  # 连接数据库的数据

engine_xxcxb = create_engine(xxcxb.DB_URI, echo=False, pool_recycle=3600) # 创建引擎
Base_xxcxb = declarative_base(engine_xxcxb)
DBSession_xxcxb = sessionmaker(bind=engine_xxcxb) # sessionmaker生成一个session类 此后DBSession_xxcxb将可在全局作为一个数据库会话对象持续服务,不用重复创建
print('ok')


'''
所有的控制器在此处注册方可生效
'''
#注册控制器
from controller import apis

from controller.nlp import nlp_qa_type
from controller.nlp import nlp_qa
from controller.nlp import auto_qa

from controller.admin import role_nlp_qa_type
from controller.admin import sys_role
from controller.admin import sys_menu
from controller.admin import sys_user
from controller.admin import sys_role_menu

from controller.wechat import wechat_user
from controller.wechat import check_login

