#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import os

dict={
'mobile':{
            'cellphone':['xiaomi','huawei','zte'],
            'interphone':['baofeng','wanhua','motorola']},
'computer':{
             'notebook':['dell','lenovo','hp'],
             'PC':['samsung','asus','apple']
           },
'food':{
            'vegetables':['melon','mushroom','ginger'],
            'meat':['beef','pork','mutton']
        }
}

f=file('dic.txt','w')
for key in dict:
    f.write(key)
    f.write('\t')
    for key2 in dict[key]:
        f.write('\t')
        f.write(key2+'\t')
        f.write('\t'.join(dict[key][key2]))
        f.write('\n')
f.close()
os.system("more dic.txt")


key1=dict.keys()
print k,v in dict

print 'the dictionary are:',dict
print'------------------------------------'
print 'the key valuse are:',key1

for a in range(len(key1)):
    inputKey1 = raw_input("please input your first choose:").strip()
    if dict.has_key(inputKey1):
        inputKey2=raw_input("please input your second choose:").strip()









