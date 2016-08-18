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
        f = file(account)
        loginOK = False#login 标志位
        Names=f.readlines()#读出有效用户名和密码
        for Auth in Names:
            Auth=Auth.split()

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
                     print WrongName
                     a = file("lock.txt",'w')
                     a.write(username)+('\n')
                     a.close()
                     os.system("more lock.txt")
                 break


        if loginOK==True:
            print "the login status2 is:",loginOK
            break

    else :
        continue






