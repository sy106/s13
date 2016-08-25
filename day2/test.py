#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

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
print(product_list[2][1][3])



# # p_list = []
# user_choice1= input("[q=quit,c=check]Which kind do you want to buy?(must be digit)")
# user_choice1 = int(user_choice1)
# print(product_list[user_choice1-1])
# for item in enumerate(product_list[user_choice1-1][1]):
#     index = item[0] + 1
#     p_list = item[1][0]
#     print(index, '.', p_list)
#
#     # user_choice2 = input("[q=quit,c=check]Which kind do you want to buy?(must be digit)")
#     # user_choice2= int(user_choice1)
#     # for item2 in enumerate(p_list):
#     #     index2 = item2[0] + 1
#     #     p_name = item2[1][0]
#     #     # p_price = item2[1][1]
#     #     # p_num = item2[1][2]
#     #
#     #     print(index2, '.', p_name)





# print (product_list[0])