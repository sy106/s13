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
# print(product_list[2][1][3])



t1=[['Taro', 12],['Taro', 22]]
t2=['Taro', 2.5, 22]
# old_set=set(t1)
# new_set=set(t2)
# test_set1=new_set.difference(old_set)
# test_set2=old_set.difference(new_set)
# test_set3=old_set.intersection(new_set)
# test_set4=new_set.intersection(old_set)
# test_set5=old_set.update(new_set)
# print('test set:',old_set,new_set,test_set1,test_set2,test_set3,test_set4,test_set5)
# record= open('record_list.txt')

# for element in record.readlines():
#     element=element.split()
#     element[1]=element[1].strip(']')#去掉前后的[]
#     element[1]=element[1].strip('[')
#     str=element[1].split('],[')#根据],[把购物车信息取出来
#     length=len(str)
#     for num in range(length):
#         str2=str[num]
#         print(str2)

f = open('record_list.txt', 'r+')#record_list.txt里面记录用户购物历史清单
username=input("username:").strip()
for user in f.readlines():
    user=user.split()
    print('test user:',user[0])
    if username == user[0]:
        print("the %s has old shop car"%username)
        salary
f.write('\n')
f.close()





# print (product_list[0])