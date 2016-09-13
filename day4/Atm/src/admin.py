#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import json
import shutil
from day4.Atm.lib import commons
from day4.Atm.config import settings



CURRENT_USER_INFO = {'is_authenticated': False, 'current_user': None}
USER_INFO = {}


def dump_user_info():

    json.dump(USER_INFO, open(os.path.join(settings.USER_DIR_FOLDER, USER_INFO['card'], "basic_info.json"), 'w'))





def init():
    """
    初始化管理员信息
    :return:
    """
    dic = {'username': 'alex', 'password': commons.md5('123')}

    json.dump(dic, open(os.path.join(settings.ADMIN_DIR_FOLDER, dic['username']), 'w'))

def create_user():
    """
    创建账户
    :return:
    """

    username=input("请输入添加的用户名：\n>>>").strip()#一卡对应一个用户
    card_num =input("请输入添加的16位卡号：例如6222020409028810\n>>>").strip() #"6222020409028810"
    card_credit=input("请输入信用卡的额度：\n>>>").strip()

    if os.path.exists(os.path.join(settings.USER_DIR_FOLDER, card_num, 'record')):
        print("the card already exit!please change the number!")
        exit()
    else:
        os.makedirs(os.path.join(settings.USER_DIR_FOLDER, card_num, 'record'))



    base_info = {'username':username,
                 'card': card_num,
                 'password': commons.md5('8888'),
                 "credit": card_credit,  # 信用卡额度
                 "balance": card_credit, # 本月可用额度
                 "saving": 0,      # 储蓄金额
                 "enroll_date": "2016-01-01",
                 'expire_date': '2021-01-01',
                 'status': 0,  # 0 = normal, 1 = locked, 2 = disabled
                 "debt": [], # 欠款记录，如：[{'date': "2015_4_10", "total_debt":80000, "balance_debt": 5000},{'date': "2015_5_10", "total":80000, "balance": 5000} ]
                 }

    json.dump(base_info, open(os.path.join(settings.USER_DIR_FOLDER, card_num, "basic_info.json"), 'w'))
    print("the user %s is created" % card_num)

def remove_user():
    """
    移除账户
    :return:
    """
    card_num=input("请输入需要删除的卡号：例如：6222020409028810\n>>>").strip()
    if os.path.exists(os.path.join(settings.USER_DIR_FOLDER, card_num)):
        shutil.rmtree(os.path.join(settings.USER_DIR_FOLDER, card_num))
        print("the user %s is deleted"%card_num)
    else:
        print("the record is not exit!")
        exit("try again!")




def locked_user():
    """
    冻结账户
    :return:
    """
    card_num=input("请输入需要冻结的卡号：例如：6222020409028810\n>>>").strip()
    if os.path.exists(os.path.join(settings.USER_DIR_FOLDER, card_num)):
        basic_info = json.load(open(os.path.join(settings.USER_DIR_FOLDER, card_num, 'basic_info.json')))
        basic_info['status']=1
        json.dump(basic_info, open(os.path.join(settings.USER_DIR_FOLDER, card_num, "basic_info.json"), 'w'))#将新的状态写入记录basic_info.json
        print("the user %s is locked"%card_num)
    else:
        print("the record is not exit!")
        exit("try again!")


def search():
    """
    搜索账户
    :return:
    """
    card_num = input("请输入需要搜索的卡号：例如：6222020409028810\n>>>").strip()
    if os.path.exists(os.path.join(settings.USER_DIR_FOLDER, card_num)):
        basic_info = json.load(open(os.path.join(settings.USER_DIR_FOLDER, card_num, 'basic_info.json')))
        msg="""
        username:       %s
        card:           %s
        credit:         %s
        balance:        %s
        saving:         %s
        enroll_date:    %s
        expire_date:    %s
        status:         %s
        debt:           %s
        """
        print(msg%(basic_info['username'],basic_info['card'],basic_info['credit'],basic_info['balance'],
                   basic_info['saving'],basic_info['enroll_date'],basic_info['expire_date'],
                   basic_info['status'],basic_info['debt']))
    else:
        print("the record is not exit!")
        exit("try again!")


def main():

    menu = """
    1、创建账户；
    2、删除账户；
    3、冻结账户；
    4、查询账户
    """
    print(menu)
    menu_dic = {
        '1': create_user,
        '2': remove_user,
        '3': locked_user,
        '4': search,
    }

    while True:
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()

        else:
            print("选项不存在")


def login():
    """
    用户登陆
    :return:
    """
    while True:
        username = input('请输入用户名：').strip()
        password = input('请输入密码：').strip()

        if not os.path.exists(os.path.join(settings.ADMIN_DIR_FOLDER, username)):
            print('用户名不存在')
        else:
            user_dict = json.load(open(os.path.join(settings.ADMIN_DIR_FOLDER, username), 'r'))
            if username == user_dict['username'] and commons.md5(password) == user_dict['password']:
                CURRENT_USER_INFO['is_authenticated'] = True
                CURRENT_USER_INFO['current_user'] = username
                return True
            else:
                print('密码错误')


def run():
    init()
    ret = login()
    if ret:
        main()



