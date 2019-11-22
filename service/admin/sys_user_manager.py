# -*- coding: utf-8 -*-
# @Time    : 18-7-12 下午2:51
# @Author  : Redtree
# @File    : sys_user_manager.py
# @Desc :

import random
import string
import hashlib
from __init__ import DBSession_xxcxb,PAGE_LIMIT,USER_SALT_LENGTH
from sqlalchemy import func,or_
from database.sqlalchemy.orm_models.zf_sys_user import Zf_sys_user
from database.sqlalchemy.orm_models.zf_sys_role import Zf_sys_role
from database.sqlalchemy.orm_models.zf_sys_role_menu import Zf_sys_role_menu
from utils.http import responser
from utils.common import regex_matcher
import json
import time

# 获取由4位随机大小写字母、数字组成的salt值
def create_salt():
    salt = ''.join(random.sample(string.ascii_letters + string.digits, USER_SALT_LENGTH))
    return salt

# 获取原始密码+salt的md5值
def md5_password(password,salt):
    trans_str = password+salt
    md = hashlib.md5()
    md.update(trans_str.encode('utf-8'))
    return md.hexdigest()

#创建平台新用户
def add_sys_user(user_id,password,nickname,role_code,created_user_id,gender,phone,email,remark,is_active,org_code):

    try:
        if role_code == 'superadmin':
            return responser.send(30001)
        if regex_matcher.match_user_id(user_id) ==False:
            return responser.send(10010)

        if regex_matcher.match_email(email)==False and email != '':
            return responser.send(10008)
        if regex_matcher.match_phone_number(phone)==False and phone != '':
            return responser.send(10009)

        session = DBSession_xxcxb()

        #创建者只能为superadmin
        try:
            info =session.query(Zf_sys_user).filter(or_(Zf_sys_user.role_code=='superadmin'),Zf_sys_user.user_id==created_user_id).one()
        except:
            session.close()
            return responser.send(30001)

        salt = create_salt()  # 盐值
        db_password = md5_password(password, salt)  # 入库密码
        created_time = int(time.time())
        # 校验新创用户的建角色类型是否合法
        try:
            check_role = session.query(Zf_sys_role).filter(Zf_sys_role.role_code == role_code).one()
        except:
            session.close()
            return responser.send(30004)
        try:
            info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id == user_id).one()
            session.close()
            return responser.send(10006)
        except:
            #执行事务创建机构管理用户并关联，若失败则回滚
            try:
                info = session.add(Zf_sys_user(user_id=str(user_id), nickname=str(nickname), salt=str(salt),
                                               password=str(db_password), phone=str(phone), gender=int(gender),
                                               email=str(email),org_code=str(org_code),
                                               created_time=int(created_time), updated_time=int(created_time),
                                               remark=str(remark),
                                               del_flag=0, role_code=str(role_code),
                                               created_user_id=str(created_user_id),
                                               is_active=int(is_active)))

                if not info == 0 and not info == '':

                        session.commit()
                        session.close()

                        return responser.send(10000, user_id)


                session.close()
                return responser.send(40002)

            except:
                session.rollback() #回滚
                session.close()

    except:
        return responser.send(50007)


#创建平台新用户
def sign_in(user_id,password,nickname,gender):

    try:
        if regex_matcher.match_user_id(user_id) ==False:
            return responser.send(10010)

        session = DBSession_xxcxb()

        salt = create_salt()  # 盐值
        db_password = md5_password(password, salt)  # 入库密码
        created_time = int(time.time())

        try:
            info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id == user_id).one()
            session.close()
            return responser.send(10006)
        except:
            #执行事务创建机构管理用户并关联，若失败则回滚
            try:
                info = session.add(Zf_sys_user(user_id=str(user_id), nickname=str(nickname), salt=str(salt),
                                               password=str(db_password), phone='', gender=int(gender),
                                               email='',org_code='',
                                               created_time=int(created_time), updated_time=int(created_time),
                                               remark='',
                                               del_flag=0, role_code='gxz',
                                               created_user_id='zfadmin',
                                               is_active=1))

                if not info == 0 and not info == '':
                        session.commit()
                        session.close()
                        return responser.send(10000, user_id)

                session.close()
                return responser.send(40002)

            except:
                session.rollback() #回滚
                session.close()
    except:
        return responser.send(50007)


#管理后台用户登录校验
def check_login(user_id,password):
    try:
        # 获取会话对象
        session = DBSession_xxcxb()
        ctime = int(time.time())

        try:
            # 先检查用户是否被封禁或删除
            try:
                info = session.query(Zf_sys_user.salt).filter(Zf_sys_user.user_id == user_id,
                                                              Zf_sys_user.is_active == 1, Zf_sys_user.del_flag == 0).one()
            except Exception as err:
                print('帐号非法' + str(err))
                session.close()
                return responser.send(10003)

            salt = info[0]
            # 校验用户名和密码
            try:
                info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id == user_id,
                                                         Zf_sys_user.password == md5_password(password, salt)).one()
            except Exception as err:
                session.close() #帐号或者密码错误
                return responser.send(10002)

            # 校验角色及相关权限模块
            try:
                info2 = session.query(Zf_sys_role.role_name).filter(Zf_sys_role.role_code == info.role_code,
                                                                    Zf_sys_role.status == 0).one()
                role_name = info2[0]
                # 通过role_code获取菜单 接口预留，现在先返回角色名和角色id,后面通过关联表获得menu后去除role_code
                info3 = session.query(Zf_sys_role_menu.menu_code).filter(
                    Zf_sys_role_menu.role_code == str(info.role_code)).all()
                if not info3 == 0 and not info3 == '':
                    t_array = []
                    for one in info3:
                        t_array.append(one[0])

                    res = {'user_id': user_id, 'nickname': info.nickname, 'role_name': role_name,'role_code': info.role_code,'menu_code': t_array}
                    # 更新登录时间
                    info4 = session.query(Zf_sys_user).filter(Zf_sys_user.user_id == str(user_id)).update(
                        {Zf_sys_user.last_login: ctime})
                    if not info4 == 0 and not info4 == '':
                        session.commit()
                        session.close()
                        return responser.send(10000, res)

                    session.close()
                    return responser.send(40002)

                session.close()
                return responser.send(40002)

            except Exception as err:
                session.close()
                print('帐号被封禁' + str(err))
                return responser.send(40002)


        except Exception as err:
            print(str(err))
            session.close()
            return responser.send(40001)
    except:
        return responser.send(50007)



#系统用户的批量删除  软删除为生效
def del_sys_user(id_list):
    try:
        if 'zfadmin' in id_list:
            return responser.send(10005)
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id.in_(id_list)).delete(synchronize_session=False)
            if info >= 0:
                session.commit()
                session.close()
                return responser.send(10000, 'success')
            else:
                session.close()
                return responser.send(10001)

        except:
            session.close()
            return responser.send(40002)

    except:
        return responser.send(50007)



#获取用户列表
#除了zfadmin 帐号可以看到所有用户和角色，其他用户仅可看到自己创建的用户和角色
def get_sys_user(user_id,is_active,id_search,name_search,phone_search,page=1,role_code=''):  #写法待优化
    try:
        if is_active=='':
            is_active=[0,1]
        else:
            c_isa = []
            c_isa.append(int(is_active))
            is_active=c_isa

        session = DBSession_xxcxb()
        if user_id == 'zfadmin':
            if role_code == '':

                id_s = '%' + id_search + '%'
                na_s = '%' + name_search + '%'
                phone_search = '%' + phone_search + '%'

                all_len = session.query(func.count(Zf_sys_user.zfid)).filter(Zf_sys_user.is_active.in_(is_active),
                                                                             Zf_sys_user.nickname.like(na_s), Zf_sys_user.phone.like(phone_search),
                                                                             Zf_sys_user.user_id.like(id_s)).scalar()
                DB_data = session.query(Zf_sys_user).filter(Zf_sys_user.is_active.in_(is_active),Zf_sys_user.phone.like(phone_search),
                                                            Zf_sys_user.nickname.like(na_s),
                                                            Zf_sys_user.user_id.like(id_s)).order_by(
                    Zf_sys_user.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

                if not DB_data == 0 and not DB_data == '':
                    # print(DB_data)
                    DB_data = json.loads(str(DB_data))  # 需要强转字符串才能序列化
                    res = {"total": all_len, "data": DB_data}
                    session.close()
                    return responser.send(10000, res)

            else:

                id_s = '%' + id_search + '%'
                na_s = '%' + name_search + '%'
                phone_search = '%' + phone_search + '%'

                all_len = session.query(func.count(Zf_sys_user.zfid)).filter(Zf_sys_user.is_active.in_(is_active),Zf_sys_user.phone.like(phone_search),
                                                                             Zf_sys_user.nickname.like(na_s),
                                                                             Zf_sys_user.user_id.like(id_s),
                                                                             Zf_sys_user.role_code == role_code
                                                                             ).scalar()

                DB_data = session.query(Zf_sys_user).filter(Zf_sys_user.is_active.in_(is_active),Zf_sys_user.phone.like(phone_search),
                                                            Zf_sys_user.nickname.like(na_s),
                                                            Zf_sys_user.user_id.like(id_s),
                                                            Zf_sys_user.role_code == role_code).order_by(
                    Zf_sys_user.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

        else:
            try:
                cuser = session.query(Zf_sys_user.org_code).filter(Zf_sys_user.user_id==user_id).one()
                cuser_org_code = cuser[0]
                pass
            except Exception as err:
                return responser.send(30001)
            if role_code == '':

                id_s = '%' + id_search + '%'
                na_s = '%' + name_search + '%'
                phone_search = '%' + phone_search + '%'

                all_len = session.query(func.count(Zf_sys_user.zfid)).filter(Zf_sys_user.is_active.in_(is_active),Zf_sys_user.phone.like(phone_search),
                                                                             Zf_sys_user.nickname.like(na_s),
                                                                             Zf_sys_user.user_id.like(id_s),
                                                                             Zf_sys_user.org_code == cuser_org_code).scalar()
                DB_data = session.query(Zf_sys_user).filter(Zf_sys_user.is_active.in_(is_active),Zf_sys_user.phone.like(phone_search),
                                                            Zf_sys_user.nickname.like(na_s),
                                                            Zf_sys_user.user_id.like(id_s),
                                                            Zf_sys_user.org_code == cuser_org_code).order_by(
                    Zf_sys_user.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

                if not DB_data == 0 and not DB_data == '':
                    DB_data = json.loads(str(DB_data))  # 需要强转字符串才能序列化
                    res = {"total": all_len, "data": DB_data}
                    session.close()
                    return responser.send(10000, res)

            else:

                id_s = '%' + id_search + '%'
                na_s = '%' + name_search + '%'
                phone_search = '%' + phone_search + '%'

                all_len = session.query(func.count(Zf_sys_user.zfid)).filter(Zf_sys_user.is_active.in_(is_active),Zf_sys_user.phone.like(phone_search),
                                                                             Zf_sys_user.nickname.like(na_s),
                                                                             Zf_sys_user.user_id.like(id_s),
                                                                             Zf_sys_user.role_code == role_code,
                                                                             Zf_sys_user.org_code == cuser_org_code).scalar()
                DB_data = session.query(Zf_sys_user).filter(Zf_sys_user.is_active.in_(is_active),Zf_sys_user.phone.like(phone_search),
                                                            Zf_sys_user.nickname.like(na_s),
                                                            Zf_sys_user.user_id.like(id_s),
                                                            Zf_sys_user.role_code == role_code,
                                                            Zf_sys_user.org_code == cuser_org_code).order_by(
                    Zf_sys_user.updated_time.desc()).limit(PAGE_LIMIT).offset((int(page) - 1) * PAGE_LIMIT).all()

        if not DB_data == 0 and not DB_data == '':
            DB_data = json.loads(str(DB_data))  # 需要强转字符串才能序列化
            res = {"total": all_len, "data": DB_data}
            session.close()
            return responser.send(10000, res)

        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)

#获取当前登录用户详细信息
def get_user_data(user_id):
    try:
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id == user_id).one()
            DB_data = json.loads(str(info))  # 需要强转字符串才能序列化

            session.close()
            return responser.send(10000, DB_data)

        except Exception as err:
            print('帐号或密码错误' + str(err))
            return responser.send(10002)
    except:
        return responser.send(50007)


#密码重置接口
def reset_password(user_id, password):
    try:
        session = DBSession_xxcxb()
        salt = create_salt()  # 盐值
        db_password = md5_password(password, salt)  # 入库密码
        ctime = int(time.time())
        info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id == str(user_id)).update(
            {Zf_sys_user.salt: salt, Zf_sys_user.updated_time: ctime, Zf_sys_user.password: db_password})
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')

        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)


#用户信息更新，信息待补全
def update_user(user_id, role_code,nickname,real_name,id_card,birthday,email,head_img,phone,gender,introduction,is_active):
    try:
        if regex_matcher.match_email(email)==False and email != '':
            return responser.send(10008)
        if regex_matcher.match_phone_number(phone)==False and phone != '':
            return responser.send(10009)
        session = DBSession_xxcxb()
        ctime = int(time.time())
        # 校验用户的建角色类型是否合法
        try:
            check_role = session.query(Zf_sys_role).filter(Zf_sys_role.role_code == role_code).one()
        except:
            session.close()

            return responser.send(30004)

        info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id == str(user_id)).update(
            {Zf_sys_user.role_code:role_code,Zf_sys_user.nickname: nickname, Zf_sys_user.real_name: real_name, Zf_sys_user.updated_time: ctime
                , Zf_sys_user.id_card: id_card, Zf_sys_user.birthday: birthday, Zf_sys_user.email: email
                , Zf_sys_user.head_img: head_img, Zf_sys_user.phone: phone, Zf_sys_user.gender: gender,Zf_sys_user.is_active:is_active,
             Zf_sys_user.introduction: introduction})
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')

        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)




def get_nickname(user_id):
    try:
        session = DBSession_xxcxb()
        try:
            info = session.query(Zf_sys_user.nickname).filter(Zf_sys_user.user_id == str(user_id)).one()
            nickname = info[0]
            session.close()

            return nickname
        except:
            session.close()

            return 'error'
    except:
        return responser.send(50007)



#用户禁用、启用
def ban_user(id_list,is_active):
    try:
        if 'zfadmin' in id_list:
            return responser.send(10005)

        session = DBSession_xxcxb()
        ctime = int(time.time())

        info = session.query(Zf_sys_user).filter(Zf_sys_user.user_id.in_(id_list)).update(
            {Zf_sys_user.is_active: is_active, Zf_sys_user.updated_time: ctime}, synchronize_session=False)
        if not info == 0 and not info == '':
            session.commit()
            session.close()
            return responser.send(10000, 'success')

        session.close()
        return responser.send(40002)
    except:
        return responser.send(50007)



#批量新增加用户
# for x in range(2,200):
#     print(x)
#     print(add_sys_user('t'+str(x),'测试'+str(x),'123','亿学测试','yxtea'))

#print(add_sys_user('zfchs','掌飞君','admin123',1,''))
