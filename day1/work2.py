#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import os

dict={
'mobile':{
            'cellphone':
                            {'xiaomi':'xiaomi5'},
            'interphone':
                            {'baofeng':'baofeng1'}
            },
'computer':{
             'notebook':
                            {'dell':'dell550'},
             'PC':
                            {'samsung':'ot350'}
           },
'food':{
            'vegetables':
                            {'tomato':'big_tomato'},
            'meat':
                            {'beef':'little_beef'}
        }
}

f=file('dic.txt','w')
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

for a in range(len(key1)):
    inputKey1 = raw_input("please input your first choose:").strip()
    if dict.has_key(inputKey1):
        print 'the choose is ', dict[inputKey1].keys()
        inputKey2=raw_input("please input your second choose:").strip()
        if inputKey2 in dict[inputKey1]:
            print 'the choose is ', dict[inputKey1][inputKey2].keys()
            inputKey3= raw_input("please input your third choose:").strip()
            if inputKey3 in dict[inputKey1][inputKey2]:
                print 'the result is ', dict[inputKey1][inputKey2].values()
                break








