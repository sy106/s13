#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import os

dict={
'mobile':{
            'cellphone':
                            {'xiaomi':'xiaomi5',
                              'huawei':'rongyao'},
            'interphone':
                            {'baofeng':'baofeng1',
                              'huasuo':'dt210'}
            },
'computer':{
             'notebook':
                            {'dell':'dell550',
                             'apple':'mac1'},
             'PC':
                            {'samsung':'ot350',
                             'micsoft':'m535'}
           },
'food':{
            'vegetables':
                            {'tomato':'big_tomato',
                             'onion':'red_onion'},
            'meat':
                            {'beef':'little_beef',
                             'pork':'black_pork'}
        }
}

f=file('dic.txt','w')#read the dict to file
for key in dict:
    f.write(key)
    f.write('\t\n')
    for key2 in dict[key]:
        f.write('\t')
        f.write(key2+'\t\n')

        for key3 in dict[key][key2]:
            f.write('\t')
            f.write(key3 + '\t')
            f.write(''.join(dict[key][key2][key3]))
            f.write('\n')

        f.write('\n')
f.close()
os.system("more dic.txt")


key1=dict.keys()

print 'the dictionary are:',dict
print'------------------------------------'
print 'the key valuse are:',key1

for i in range(10):#give the user 10 times to choose right

    inputKey1 = raw_input("please input your first choose:").strip()#input the first choose
    if dict.has_key(inputKey1):
        print 'the choose is ', dict[inputKey1].keys()
        inputKey2=raw_input("please input your second choose:").strip()#if the first is right ,input the second choose
        if inputKey2 in dict[inputKey1]:
            print 'the choose is ', dict[inputKey1][inputKey2].keys()
            inputKey3= raw_input("please input your third choose:").strip()#if the second is right ,input the third choose
            if inputKey3 in dict[inputKey1][inputKey2]:
                print 'the result is ', dict[inputKey1][inputKey2][inputKey3]#if all the choose are right,print the result
                break
            else :#if the third choose is wrong,give the user one chance to input the right choose,otherwise ,return to first choose
                print 'please input the correct choose,if not,you will return to choose the first choose ', dict[inputKey1][inputKey2].keys()
                inputKey3 = raw_input("please input your third choose:").strip()
                continue








