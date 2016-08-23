#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import os

# #write userinfo into local file
# f=file('userinfo.txt','a')
# f.write('sy106 123\n')
# f.write('admin admin\n')
# f.write('alex 123\n')
# f.close()

#read userinfo
account='user.txt'
f=file(account)
accountName=f.readlines()
print 'the Auth Names are:',accountName

for i in range(5):
    Login=False
    #read lock name into local file
    username=raw_input('please input your login name:').strip()
    lock='lock.txt'
    f=file(lock)
    lockName_list=[]
    for lockName in f.readlines():
        lockName=lockName.strip('\n')
        lockName_list.append(lockName)
    f.close()
    print 'lockName_list are:',lockName_list
    if username in lockName_list:
        print'The user %s has been lock!please use another username!'%username
        break
    for line in accountName:
        line=line.split()
        if username==line[0]:#if the name is right ,input the passwd
            for i in range(3):
                passwd = raw_input('please input your password:').strip()
                if passwd==line[1]:
                    print "Welcome %s login the system!"%username#login success
                    Login = True
                    break
            else:
                f=file(lock,'a')
                f.write('%s\n'%username)
                f.close()
                print 'Enter 3 times wrong password,the name %s is locked'%username
            if Login is True:break#jump out of for loop
    else:
        print 'please input the right name ,retry!'
    if  Login is True:
        break#jump out of top for loop





