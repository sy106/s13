#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import os,json,time
from day09.socket.FTP import commons


class userinfo(object):
    def __init__(self,username,password,time):
        self.username = username
        self.password = password
        self.time = time

    def save_user(self):
        dic_user = [{'username': self.username, 'password': commons.md5(self.password),"login_time":self.time}]
        json.dump(dic_user,open('user_db'),'wb')

    def user_create(name,passwd = ''):
        if
        user_dict = json.load(open( 'user_db'), 'rb')
        len = len(user_dict)
        for i in range(len):
            if name == user_dict[i]['username'] and commons.md5(passwd) == user_dict[i]['password']:
                    result = userinfo(name,passwd,time.time())
                    result.save_user()


