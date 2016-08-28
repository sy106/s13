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



t1=['Taro', 2.5, 12]
t2=['Taro', 2.5, 22]
old_set=set(t1)
new_set=set(t2)
test_set1=new_set.difference(old_set)
test_set2=old_set.difference(new_set)
test_set3=old_set.intersection(new_set)
test_set4=new_set.intersection(old_set)
test_set5=old_set.update(new_set)
print('test set:',old_set,new_set,test_set1,test_set2,test_set3,test_set4,test_set5)





# print (product_list[0])