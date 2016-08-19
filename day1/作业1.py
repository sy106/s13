#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import  os

f = file('user.txt','w')
#a = file("lock.txt")
f.write("sy106 123\n")
f.write('admin admin\n')
f.write('Alex 123')
f.close()
os.system("more user.txt")
account="user.txt"
lock="lock.txt"

WrongTime=0
WrongName=[ ]
for i in range(3):
    username = raw_input("please input your username:").strip()
    password = raw_input("please input your password:").strip()
    if len(username)!=0 and len(password)!=0:
        f1 = file(account)
        loginOK = False#login 标志位
        Names=f1.readlines()#读出有效用户名和密码
        print 'the Auth Names are:',Names
        for Auth in Names:
            Auth=Auth.split()
        #     print'Auth',Auth
        # f2 = file(lock)
        # lockNames = f2.readlines()#读出锁定的用户名
        # Len = len(lockNames)
        # print 'the lock names are:', lockNames
        # print 'the lock len are:', Len
        # print 'the type of lockNames:',type(lockNames)
        # print 'the type of username:', type(username)
        # Name=username+'\n'
        # print 'Name:', Name
        # for x in range(Len):
        #     if lockNames[x]==Name:
        #     # print 'Lock:', lockName
        #     # if username==lockName[0]:
        #         print 'the %s is lock,please exchage another name!' % username
        #         break

            if username==Auth[0] and password==Auth[1]:#username and password are correct
                print "Welcome %s login my system!" %username
                loginOK =True
                break
                print "the login status1 is:",loginOK
                break
            if username==Auth[0] and password!=Auth[1] :#password is wrong
                print 'Wrong password! please retry!'
                break
            if username!=Auth[0] :  #username is wrong
                 WrongName.append(username)
                 WrongTime = WrongTime + 1
                 print 'wrong name is:',WrongName
                 print 'wrong time is:', WrongTime
                 print WrongName.count(username)

                 if WrongName.count(username)==3:
                     print  'the lock name is',WrongName
                     a = file("lock.txt",'a')

                     a.write('%s\n'%username)
                     f.close()
                     print 'tpye of name',type(username)
                     os.system("more lock.txt")


                 break


        if loginOK==True:
            print "the login status2 is:",loginOK
            break

    else :
        continue






