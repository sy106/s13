#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import os,pickle
from day09.socket.FTP import commons



class userinfo(object):
    def __init__(self,username,password):
        self.username = username
        self.password = commons.md5(password)


user1 = userinfo('alex','123')
user2 = userinfo('tom','234')
user3 = userinfo('john','345')

list_S = [user1,user2,user3]
pickle.dump(list_S,open('user_info','wb'))
ret_S = pickle.load(open('user_info','rb'))


def check(username,password):


    if username== 'q' or username == 'quit':
        quit()
    for j in range(len(list_S)):
        if username == ret_S[j].username:
                if password == ret_S[j].password:
                    print("%s password is right" % (username))
                    return 0
                else:
                    print('the password is wrong!please retry!')
    else:
        print("the username is wrong!please relogin!")
        return 1
