#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import os

dic="dictionary"

line = file(dic)#print the first choose
line = line.readlines()
for i in line:
    key = i.strip().split()
    print'the first choose have:', key[0]

for i in range(5):
    choose_lable=False
    inputKey1 = raw_input("please input your first choose:").strip()  # input the first choose
    # if len(inputKey1)==0:continue
    for key in line:
        key=key.strip().split()

        while inputKey1==key[0]:
            print'the choose is ', key[1]
            inputKey2 = raw_input("please input your second choose:").strip()  # if the first is right ,input the second choose

            if inputKey2 == key[1] :
                print'the choose is ', key[2]
                inputKey3 = raw_input("please input your third choose:").strip()  # if the second is right ,input the third choose
                if inputKey3 == key[2] :
                    print'the result is ',key[3]  # if all the choose are right,print the result
                    choose_lable=True
                    break
                else:
                    print'please input the right name ,retry!'
                    inputKey3 = raw_input("please input your third choose:").strip()  # if the second is right ,input the third choose
                    if inputKey3 == key[2]:
                        print'the result is ', key[3]  # if all the choose are right,print the result
                        choose_lable = True
                        break
            else:
                print'please input the right name ,retry!'
        if choose_lable is True: break  # jump out of for while
    else:
        print'please input the right name ,retry!'

    if choose_lable is True: break  # jump out of for loop


