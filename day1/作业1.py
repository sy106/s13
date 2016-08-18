#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import  os

f = file('userinfo.txt','w')
#a = file("lock.txt")
f.write("sy106 123\n")
f.write('admin admin\n')
f.write('Alex 123')
f.close()
os.system("more user.txt")
account="user.txt"
lock="lock.txt"


for i in range(3):
    username=raw_input("please input your username:").strip()
    password=raw_input("please input your password:").strip()
    if len(username)!=0 and len(password)!=0:
        f=file(account)
        loginOK = False
        for line in f.readlines():
            line=line.split()
            if username==line[0] and password==line[1]:#username and password are correct
                print "Wlcome %s login my system!" %username
                loginOK =True
                break
        print loginOK
        break

        if loginOK==True:
            break
    else:
        continue






