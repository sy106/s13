#!user/bin/env python
#-*- coding:utf-8 -*-
# Author: Sy106

age =22
counter = 0
for i in range(10):
    if counter<3:
        print("---counter2--", counter)
        guessnum=int(input("please input your guess num!"))
        if guessnum == age:
            print ("your are right!")
            break
        elif guessnum<age:
            print ("smaller!")
        else:
            print ("bigger!")
    else:
        continue_confirm=input("Do you want to continue,beacuse you are stupid")
        if continue_confirm=="y":
            counter=0
            print("---counter--",counter)
            continue
        else:
            print("bye!")
            break

    counter +=1
            
