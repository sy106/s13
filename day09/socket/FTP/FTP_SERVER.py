#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:sy106

import socketserver,os,time,subprocess
from time import sleep
from day09.socket.FTP import userinfo

class MyFtpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                sleep(1)
                self.request.sendall(bytes('auth first!',encoding="utf-8"))
                name = self.request.recv(BUFSIZE).decode()
                sleep(1)
                self.request.sendall(bytes('pauth', encoding="utf-8"))

                password = self.request.recv(BUFSIZE).decode()
                print(name,password)
                auth_result = userinfo.user_create(name,password)
                if auth_result == 0:
                    self.request.sendall(bytes('wlcome login!', encoding="utf-8"))
                    break
                elif auth_result == 1:
                    self.request.sendall(bytes('fail to login!', encoding="utf-8"))
                    continue

                recv_data = self.request.recv(BUFSIZE).split().decode()
                if recv_data[0] == 'rls':
                    result = os.popen('ls -l ./').read()
                    self.request.sendall(bytes(result,encoding='utf8'))
                    continue
                if recv_data[0] == '?' or recv_data[0] == 'help':
                    result = '''\033[32;lm
                    ?\help:     Get help.
                    Get:        Download file from remote server.
                    Send:       Send local file to remote server.
                    ls:         List local file.
                    rls:        List remote server file.
                    cd:         change file catalog.
                    quit\exit:  Quit the app.
                    \033[0m'''
                    self.request.sendall(result)
                    continue
                if recv_data[0] == 'send':
                    filename = recv_data[1]
                    self.request.sendall(bytes('ok2send', encoding="utf-8"))
                    recv_data = self.request.recv(BUFSIZE)
                    file2w = open(filename,'wb')
                    file2w.write(recv_data)
                    file2w.flush()
                    file2w.close()
                    self.request.sendall(bytes('\033[33;1mFile transfer successed!\033[0m', encoding="utf-8"))

                    continue
                if recv_data[0] == 'get':
                    filename = recv_data[1]
                    if os.path.isfile(filename):
                        self.request.sendall('ok2get')
                        if self.request.recv(BUFSIZE) == 'ok2send':
                            self.request.sendall("sending")
                            sleep(1)
                            file_data = open(filename,'rb')
                            file_tmp = file_data.read()
                            self.request.sendall(file_tmp)
                            sleep(1)
                            self.request.sendall("\033[33;1mDownloading complete!")
                            file_data.close()
                    else:
                        self.request.sendall('fail2get')
                        if self.request.recv(BUFSIZE) == 'ack':
                            self.request.sendall('\033[31;1m%s not found\033[0m'%filename)
                if recv_data[0] == 'cd':
                    #self.request.sendall('ok2change')
                    result = os.popen(recv_data).read()
                    self.request.sendall(result)
                    continue

        except Exception as e:
            print(e)
if __name__=='__main__':
    HOST,PORT = '',9889
    ADDR = (HOST,PORT)
    BUFSIZE = 2048

    try:
        server = socketserver.ThreadingTCPServer(ADDR,MyFtpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()