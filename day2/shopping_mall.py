#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Author: Sy106

import os
import json

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

user_list=[['admin','123'],['sy106','234'],['leo','456']]
shop_car = []
buy_time=0
salary=0


for buy_time in range(10)  :
    username=input('please input your login name[q=quit]:').strip()
    new_list = [username, shop_car, salary]
    print (new_list)

    hisory= 'record_list.txt'#从购物历史中读取购物清单
    f = open(hisory)
    record_list=[]
    record_name = []
    name_list=[]
    record_salary=[]

    # for record in f.readlines():
    #     if record !=[]:
    #         record = record.strip().split()
    #         print('test',record)
    #         record_list.append(record[3])
    #         record_name.append(record[1])
    #         record_salary.append(record[4])
    #     else:
    #         break
    # print(record)

    f.close()
    # set(record_list)
    # print(record_list,record_name,record_salary)

    for line in user_list:
        if username==line[0]:#if the name is right ,input the passwd
            passwd = input('please input your password:').strip()
            if passwd == line[1]:
                print("Welcome %s login the system!" % username)  # login success
                if username in record_name:
                    salary=record_list[username]
                else:
                    salary = input("Input your salary:")
                    if salary.isdigit():
                        salary = int(salary)
                    else:
                        exit("Invaild data type...")

                Login = True


                if username == 'sy106' and salary == 0:
                    salary = input("Input your salary:")
                    if salary.isdigit():
                        salary = int(salary)
                    else:
                        exit("Invaild data type...")
                if username == 'leo' and salary == 0:
                    salary = input("Input your salary:")
                    if salary.isdigit():
                        salary = int(salary)
                    else:
                        exit("Invaild data type...")
                welcome_msg = 'Welcome to Sy106 Shopping mall'.center(50, '-')
                print(welcome_msg)
                usr_msg="""
                username:   %s
                password:   %s
                salary:     %d """
                print(usr_msg%(username,passwd,salary))
                user_info=[username,passwd,salary]
                print(user_info)
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

                    if user_choice1.isdigit():  # 肯定是选择shangpin
                        user_choice1 = int(user_choice1)
                        if user_choice1 <= len(product_list):
                            title="""index   p_name       p_price    p_number"""
                            print(title)
                            for item in enumerate(product_list[user_choice1 - 1][1]):  # print the second product list
                                index = item[0] + 1
                                p_list = item[1][0]
                                p_price=item[1][1]
                                p_num=item[1][2]
                                list_msg = """%s.      %s        %s        %s"""
                                print(list_msg % (index, p_list, p_price, p_num))
                            user_choice2 = input("Which one do you want to buy?(must be digit)")
                            if user_choice2.isdigit():  # 肯定是选择shangpin
                                user_choice2 = int(user_choice2)
                                p_item = product_list[user_choice1 - 1][1][user_choice2 - 1]
                                print("test pitem",p_item)
                                choose_num=user_choice2 = input("How many do you want to buy?(must be digit)")
                                if choose_num.isdigit():
                                    choose_num = int(choose_num)

                                    if int(p_item[1]) <= salary:  # 买的起
                                        salary -= p_item[1] * choose_num  # 余额
                                        if shop_car!=[]:
                                            # for list in shop_car:
                                            #     if p_item[0] in shop_car:
                                            #         # location=list.index(p_item[0])
                                            #         shop_car.remove(list)
                                            #         choose_num+=list[2]
                                            #         shop_car.append([p_item[0], p_item[1], choose_num])
                                            #     else:
                                            #         shop_car.append([p_item[0], p_item[1], choose_num])
                                            if p_item[0] in shop_car:
                                                for list in shop_car:
                                                    if list[0]==p_item[0]:
                                                        shop_car.remove(list)
                                                        choose_num += list[2]
                                                        shop_car.append([p_item[0], p_item[1], choose_num]) 
                                        else:
                                            shop_car.append([p_item[0], p_item[1], choose_num])  # 放入购物车,名称，价格，数量
                                        # shop_car.append([p_item[0], p_item[1], choose_num])
                                        print('test shopcar:', shop_car)
                                        record_list = [username, shop_car, salary]#为用户该次购物信息
                                        print("test user info:",record_list)

                                        f = open(hisory, 'a+')#history里面记录用户购物历史清单
                                        for user in f.readlines():
                                            print('test user:',user)
                                            if username == user[0]:
                                                print("the same user login")
                                        f.write('\n')
                                        f.close()

                                        # for data in record_list:
                                        #     f.writelines(str(data))


                                            # f.write(repr(line))
                                            # f.write(' ')




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

                    else:
                        if user_choice1 == 'q' or user_choice1 == 'quit':
                            print("%s purchased products as below".center(40, '*') % username)
                            title = """index   p_name       p_price    p_number"""
                            print(title)
                            for item in enumerate(shop_car):
                                index = item[0] + 1
                                p_name = item[1][0]
                                p_price = item[1][1]
                                p_num = item[1][2]
                                list_msg = """%s.      %s        %s        %s"""
                                print(list_msg % (index, p_name, p_price, p_num))
                            print("END".center(40, '*'))
                            print("Your balance is [%s]" % salary)
                            print("Bye")

                            # record_list=[]

                            exit_flag = True
                            break
                        elif user_choice1 == 'c' or user_choice1 == 'check':
                            print("%s purchased products as below".center(40, '*')%username)
                            title = """index   p_name       p_price    p_number"""
                            print(title)
                            for item in enumerate(shop_car):
                                index = item[0] + 1
                                p_name = item[1][0]
                                p_price = item[1][1]
                                p_num = item[1][2]
                                list_msg = """%s.      %s        %s        %s"""
                                print(list_msg % (index, p_name, p_price, p_num))
                            print("END".center(40, '*'))
                            print("Your balance is \033[41;1m[%s]\033[0m" % salary)

            else:
                print('please input the right passwd ,retry!')
        elif username == 'q' or username == 'quit':#allow user quit
            exit("Bye!")

