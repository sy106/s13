#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import logging
import time
import json

from day4.Atm.config import settings
from day4.Atm.src.backend import logger


CURRENT_USER_INFO = {}



def dump_current_user_info():

    json.dump(CURRENT_USER_INFO, open(os.path.join(settings.USER_DIR_FOLDER, CURRENT_USER_INFO['card'], "basic_info.json"), 'w'))

def dump_transfer_user_info():

    json.dump(TRANSFER_USER_INFO, open(os.path.join(settings.USER_DIR_FOLDER, TRANSFER_USER_INFO['card'], "basic_info.json"), 'w'))

def write_record(message):
    """
    账户记录
    :param message:
    :return:
    """
    struct_time = time.localtime()
    logger_obj = logger.get_logger(CURRENT_USER_INFO['card'], struct_time)
    logger_obj.info(message)


def account_info():
    """
    账户信息
    :return:
    """
    dump_current_user_info()
    msg = """
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
    print(msg % (CURRENT_USER_INFO['username'], CURRENT_USER_INFO['card'], CURRENT_USER_INFO['credit'], CURRENT_USER_INFO['balance'],
                 CURRENT_USER_INFO['saving'], CURRENT_USER_INFO['enroll_date'], CURRENT_USER_INFO['expire_date'],
                 CURRENT_USER_INFO['status'], CURRENT_USER_INFO['debt']))


def repay():
    """
    还款
    :return:
    """
    num = float(input('请输入还款金额').strip())
    write_record('%s - 储蓄账户：%f；信用卡账户：%f；' % ("还款",CURRENT_USER_INFO['saving'],num))
    CURRENT_USER_INFO['balance'] += num
    dump_current_user_info()



def withdraw():
    """
    提现
    提现时，优先从自己余额中拿，如果余额不足，则使用信用卡（额度限制），提现需要手续费10%
    :return:
    """
    num = float(input('请输入提现金额').strip())
    if CURRENT_USER_INFO['saving'] >= num:
        CURRENT_USER_INFO['saving'] -= num

        write_record('%s - 储蓄账户：%d' % ("提现", num))
        dump_current_user_info()
    else:
        temp = num - CURRENT_USER_INFO['saving']
        CURRENT_USER_INFO['balance']=float(CURRENT_USER_INFO['balance'])
        if CURRENT_USER_INFO['balance'] > (temp + temp * 0.05):
            CURRENT_USER_INFO['balance'] -= temp
            CURRENT_USER_INFO['balance'] -= temp * 0.05

            write_record('%s - 储蓄账户：%f；信用卡账户：%f；手续费：%f' % ("提现", CURRENT_USER_INFO['saving'], temp, temp * 0.05))
            dump_current_user_info()
        else:
            print('账户余额不足，无法完成提现')


def transfer():
    """
    转账
    :return:
    """
    card_num=input("请输入对方卡号：例如：6222020409028811\n>>>").strip()
    if card_num==CURRENT_USER_INFO['card']:
        print("不能给自己转账！")

    elif os.path.exists(os.path.join(settings.USER_DIR_FOLDER, card_num)):#转账优先从储蓄账户转
        tansfer_info = json.load(open(os.path.join(settings.USER_DIR_FOLDER, card_num, "basic_info.json")))
        num = float(input('请输入转账金额\n>>>').strip())
        if CURRENT_USER_INFO['saving'] >= num:
            CURRENT_USER_INFO['saving'] -= num

            write_record('%s - 储蓄账户：%d;-对方账号：%s' % ("转账", num,tansfer_info['card']))
            dump_current_user_info()
            tansfer_info['saving']+=num
            json.dump(tansfer_info,
                      open(os.path.join(settings.USER_DIR_FOLDER, tansfer_info['card'], "basic_info.json"), 'w'))
            struct_time = time.localtime()
            logger_obj = logger.get_logger(tansfer_info['card'], struct_time)
            logger_obj.info('%s - 储蓄账户：%d -对方账号:%s' % ("到账", num, CURRENT_USER_INFO['card']))

        else:
            temp = num - CURRENT_USER_INFO['saving']
            CURRENT_USER_INFO['balance'] = float(CURRENT_USER_INFO['balance'])
            if CURRENT_USER_INFO['balance'] > (temp + temp * 0.05):
                CURRENT_USER_INFO['balance'] -= temps
                CURRENT_USER_INFO['balance'] -= temp * 0.05

                write_record('%s - 储蓄账户：%f；信用卡账户：%f；手续费：%f；对方账号：%s' % ("转账", CURRENT_USER_INFO['saving'], temp, temp * 0.05,tansfer_info['card']))
                dump_current_user_info()
                tansfer_info['saving'] += num
                json.dump(tansfer_info,
                          open(os.path.join(settings.USER_DIR_FOLDER, tansfer_info['card'], "basic_info.json"), 'w'))
                struct_time = time.localtime()
                logger_obj = logger.get_logger(tansfer_info['card'], struct_time)
                logger_obj.info('%s - 储蓄账户：%d -对方账号:%s' % ("到账", num,CURRENT_USER_INFO['card']))
            else:
                print('账户余额不足，无法完成转账')
    else:
        print("请输入合法的信用卡号！")


def pay_check():
    """
       查账
       :return:
       """
    CURRENT_USER_INFO['debt']='{:.2f}'.format(float(CURRENT_USER_INFO['credit'])-float(CURRENT_USER_INFO['balance']))
    dump_current_user_info()
    print("目前的信用卡账单为%s；-储蓄账户余额为%s"%(CURRENT_USER_INFO['debt'],CURRENT_USER_INFO['saving']))

def main():
    menu = '''
    1.  账户信息
    2.  还款
    3.  取款
    4.  转账
    5.  账单
    '''
    menu_dic = {
        '1': account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
    }
    while True:
        print(menu)
        user_option = input(">>:").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()

        else:
            print("选项不存在")


def init(card):

    basic_info = json.load(open(os.path.join(settings.USER_DIR_FOLDER, card, "basic_info.json")))
    if basic_info['status']==1:
        print("该账户%s被冻结!请联系银行客服！"%card)
        exit("请重新选择合法的信用卡！")
    elif basic_info['status']==0:
        CURRENT_USER_INFO.update(basic_info)
    else:
        print("该卡%s不可用！请联系银行客服！"%card)
        exit("请重新选择合法的信用卡！")



def login():
    """
    登陆
    :return:
    """
    card_num = input("请输入信用卡卡号：例如：6222020409028810\n>>>").strip()#"6222020409028810"
    if os.path.exists(os.path.join(settings.USER_DIR_FOLDER, card_num)):
        init(card_num)
    return True


def run():
    ret = login()
    if ret:
        main()
