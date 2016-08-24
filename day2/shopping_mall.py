#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Author: Sy106

salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
else:
    exit("Invaild data type...")

welcome_msg = 'Welcome to Sy106 Shopping mall'.center(50,'-')
print(welcome_msg)

exit_flag = False
product_dict = {
'car':{
	    'p_name':['BMW','Audi','Pasate','Tesla Model_3'],
        'num':[10,10,10,10],
        'price':[33333,34567,35678,888888]
	},
'food':{
        'p_name':['tomato','cucumber','Carrot','Taro'],
        'num':[100,100,100,100],
        'price':[2,3,4,5]
	},
'mible':{
	    'p_name':['xiaomi','huawei','apple','nokia'],
        'num':[100,100,100,100],
        'price':[1000,2000,5000,500]
	}

}

user_list=[['admin',123],['sy106',234],['leo',456]]


shop_car = []
while  exit_flag is not True:
    #for product_item in product_list:
    #    p_name,p_price = product_item
    print("product list".center(50,'-'))
    for item in enumerate(product_list):
        index = item[0]
        p_name = item[1][0]
        p_price = item[1][1]
        print(index,'.',p_name,p_price)

    user_choice = input("[q=quit,c=check]What do you want to buy?:")
    if user_choice.isdigit():#鑲畾鏄€夋嫨shangpin
        user_choice = int(user_choice)
        if user_choice < len(product_list):
            p_item = product_list[user_choice]
            if p_item[1] <= salary: #涔扮殑璧?
                shop_car.append(p_item) #鏀惧叆璐墿杞?
                salary -= p_item[1] #鍑忛挶
                print("Added [%s] into shop car,you current balance is \033[31;1m[%s]\033[0m" %
                      (p_item,salary))
            else:
                print("Your balance is [%s],cannot afford this.." % salary)
    else:
        if user_choice == 'q' or user_choice =='quit':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:
                print(item)
            print("END".center(40,'*'))
            print("Your balance is [%s]" % salary)
            print("Bye")
            exit_flag = True
        elif  user_choice == 'c' or user_choice =='check':
            print("purchased products as below".center(40,'*'))
            for item in shop_car:
                print(item)
            print("END".center(40,'*'))
            print("Your balance is \033[41;1m[%s]\033[0m" % salary)

