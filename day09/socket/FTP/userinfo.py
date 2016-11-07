#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import os,pickle
from day09.socket.FTP import commons
#If it is your first time run this programm,use DIC={}
#DIC = pickle.load(open('userdb','rb'))
DIC = {}

class userinfo(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password


    def save_user(self):
        #dic_user = {'username': self.username, 'password': commons.md5(self.password)}
        DIC[self.username] = [commons.md5(self.password)]
        if os.path.exists('user_db'):
            pickle.dump(DIC, open('user_db'), 'ab')
        else:
            pickle.dump(DIC,open('user_db'),'wb')

def user_create(NAME,PASSWD = ''):
    if os.path.exists('user_db'):
        DIC = pickle.load(open( 'user_db'), 'rb')
        if NAME in DIC and commons.md5(PASSWD) == DIC[NAME][0]:
            result = userinfo(NAME,PASSWD)
            result.save_user()
            return 0
        else:
            return 1
    else:
        result = userinfo(NAME, PASSWD)
        result.save_user()
        print("the user is not exit !")
        return 1

if __name__ == '__main__':
    user_create(userinfo.username,userinfo.password)