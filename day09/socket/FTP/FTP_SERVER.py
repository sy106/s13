#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import socketserver,json,os
from day09.socket.FTP import commons,userinfo

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        pass

    def user_info(self):
        """
        初始化管理员信息
        :return:
        """
        dic = [{'username': 'alex','password': commons.md5('123')},
               {'username': 'sy106', 'password': commons.md5('234')},
               {'username': 'leo', 'password': commons.md5('345')}]

        json.dump(dic, open(userinfo.USER_DIR_FOLDER, 'w'))

