#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Author: Sy106

product_list =[
['car', [
    ('BMW',588888,10),
    ('Audi',380000,10),
    ('Pasate',290000,10),
    ('Tesla Model_3',800000,10)
    ]],
['moble', [
    ('Iphone',5888,50),
    ('xiaomi5',800,50),
    ('huawei5',900,50),
    ('nokia3',599,50)
    ]],
['food', [
    ('tomato',1,100),
    ('cucumber',2,100),
    ('Carrot',3,100),
    ('Taro',2.5,100)
    ]]]

STARTING = 0
LOGINED = 1
CHECK = 2
QUITING = 3



state = STARTING

user_list=[['admin','123'],['sy106','234'],['leo','456']]
userName = ''
balance = -1
shop_car=[]
record= open('record_list.txt')

while True:
    if state == STARTING:

        inputedName = input('please input your login name[q=quit]:').strip()
        if inputedName == 'q' or inputedName == 'quit':
            state = QUITING
            continue

        else:
            userName = inputedName
            for line in user_list:
                if userName == line[0]:  # if the name is right ,input the passwd
                    for passwd_retry_time in range(3):
                        passwd = input('please input your password:').strip()
                        if passwd == line[1]:
                            print("Welcome %s login the system!" % userName)  # login success
                            print('Welcome %s login to Sy106 Shopping mall'.center(50, '-')% userName)

                            #read balance
                            #init here, read the salary, carton and other item information

                            for record_line in record.readlines():
                                record_line = record_line.split()
                                if userName==record_line[0]:
                                        print("welcome %s login again!"%userName)
                                        salary = int(record_line[2])
                                        old_shop_list=record_line[1]
                                        # for shop_item in old_shop_list:#print last time buyed list
                                        #     shop_item

                                        break
                            else:
                                salary = input("Input your salary:")
                                if salary.isdigit():
                                    salary = int(salary)
                                else:
                                    exit("Invaild data type...")
                            usr_msg = """
                                            username:   %s
                                            password:   %s
                                            salary:     %d """
                            print(usr_msg % (userName, passwd, salary))
                            state = LOGINED
                            break
                        else:
                            #wrong password
                            print("wrong password,please retry!")
                    else:
                        print("you try too many times!...")
                        break

            else:
                if state != LOGINED:
                    #retry
                    print("username is not exist, retry!")

    elif state == LOGINED:
        exit_flag = False
        while exit_flag is False:
            # for product_item in product_list:
            #    p_name,p_price ,p_num= product_item

            print("product list".center(50, '-'))
            for item in enumerate(product_list):
                index = item[0] + 1
                category = item[1][0]
                print(index, '.', category)

            user_choice1 = input("[q=quit,c=check]Which kind do you want to buy?(must be digit)")
            if user_choice1 == 'c' or user_choice1 == 'check':
                state= CHECK
                break
            if user_choice1 == 'q' or user_choice1 == 'quit':
                state = QUITING
                break
            if user_choice1.isdigit():  # 肯定是选择shangpin
                user_choice1 = int(user_choice1)
                if user_choice1 <= len(product_list):
                    title = """index   p_name       p_price    p_number"""
                    print(title)
                    for item in enumerate(product_list[user_choice1 - 1][1]):  # print the second product list
                        index = item[0] + 1
                        p_name = item[1][0]
                        p_price = item[1][1]
                        p_num = item[1][2]
                        list_msg = """%s.      %s        %s        %s"""
                        print(list_msg % (index, p_name, p_price, p_num))
                    user_choice2 = input("Which one do you want to buy?(must be digit)")
                    if user_choice2.isdigit():  # 肯定是选择shangpin
                        user_choice2 = int(user_choice2)
                        p_item = product_list[user_choice1 - 1][1][user_choice2 - 1]
                        print("test pitem", p_item)
                        choose_num =  input("How many do you want to buy?(must be digit)")
                        if choose_num.isdigit():
                            choose_num = int(choose_num)
                            if int(p_item[1]) <= salary:  # 买的起
                                salary -= p_item[1] * choose_num  # 余额
                                if shop_car != []:#prepare add buy  produc into shop_car
                                    if p_item[0] in shop_car:
                                        for list in shop_car:
                                            if list[0] == p_item[0]:
                                                shop_car.remove(list)
                                                choose_num += list[1]
                                                shop_car.append([p_item[0],choose_num])  # 放入购物车,名称，数量

                                else:
                                    shop_car.append([p_item[0], choose_num])# 放入购物车,名称，数量

                                print("Added [%s] into shop car,you current balance is \033[31;1m[%s]\033[0m" %
                                      (p_item[0], salary))
                            else:
                                print("Your balance is [%s],cannot afford this，do your want to recharge?" % salary)
                                recharge_lable = input("[y or n?]:")  # 提醒用户是否需要充值
                                if recharge_lable == 'y':
                                    recharge = input("Input your recharge:")
                                    if recharge.isdigit():
                                        recharge = int(recharge)
                                        salary = salary + recharge
                                        print("Now you recharge is %d,and your salary is %d" % (recharge, salary))
                                    else:
                                        exit("Invaild data type...")
                                elif recharge_lable == 'n':
                                    print("Your balance is [%s],you can buy something you can afford" % salary)
        continue

    elif state == CHECK:

            print("%s purchased products as below".center(40, '*') % userName)
            title = """index   p_name      p_number"""
            print(title)
            for item in enumerate(shop_car):
                index = item[0] + 1
                p_name = item[1][0]
                p_num = item[1][1]
                list_msg = """%s.      %s        %s"""
                print(list_msg % (index, p_name,p_num))
            print("END".center(40, '*'))
            print("Your balance is \033[41;1m[%s]\033[0m" % salary)
            continue
    elif state == QUITING:
        #do someting for quit, save the carting and account information
            print("%s purchased products as below".center(40, '*') % userName)
            title = """index   p_name     p_number"""
            print(title)
            for item in enumerate(shop_car):
                index = item[0] + 1
                p_name = item[1][0]
                p_num = item[1][1]
                list_msg = """%s.      %s        %s"""
                print(list_msg % (index, p_name,p_num))
            print("END".center(40, '*'))
            print("Your balance is [%s]" % salary)
            exit("Bye!")
    else:
        break
