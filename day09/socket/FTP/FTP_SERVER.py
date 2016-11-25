#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:sy106

import socketserver,os,time,subprocess,json,sys
from time import sleep
from day09.socket.FTP import userinfo,commons

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))# 配置文件的上层目录

BUFSIZE =4096


class MyFtpHandler(socketserver.BaseRequestHandler):
    def handle(self):
     try:
        self.request.send(bytes('auth', encoding="utf-8"))
        name = self.request.recv(BUFSIZE).decode()
        sleep(1)
        self.request.send(bytes('pauth', encoding="utf-8"))
        password = self.request.recv(BUFSIZE).decode()
        print(name, password)
        auth_result = userinfo.check(name, commons.md5(password))
        if auth_result == 0:
            self.request.sendall(bytes('ok2login', encoding="utf-8"))
            list_S = userinfo.list_S
            ret_S = userinfo.ret_S
            for j in range(len(list_S)):
                if name == ret_S[j].username:
                 global   user_bufsize,user_catalog
                 user_bufsize = ret_S[j].bufsize#给用户磁盘配额
                 user_catalog = os.path.join(ret_S[j].catalog,'home')
                 os.makedirs(user_catalog)#创建用户home目录
                 print('test>>',user_catalog)
        elif auth_result == 1:
            self.request.sendall(bytes('fail2login', encoding="utf-8"))
        while True:
                recv_data = self.request.recv(BUFSIZE)
                recv_data1 = recv_data.decode()
                if len(recv_data) == 0:break #客户端如果退出，服务端将收到空消息，退出
                print("[%s] says:%s" % (self.client_address, recv_data1))

                task_data = json.loads(recv_data1)
                task_action = task_data.get("action")
                if hasattr(self, "task_%s" % task_action):
                    func = getattr(self, "task_%s" % task_action)
                    func(task_data)
                else:
                   print("task action is not supported",task_action)
                   break
     except Exception as e:
          print(e)


    def task_send(self, *args, **kwargs):
        print("---send", args, kwargs)
        filename = args[0].get('filename')
        filesize = args[0].get('file_size')
        if filesize < user_bufsize:
            new_filename = os.path.join(user_catalog,filename)
            print (new_filename)
            size = 1024*1024
            if os.path.exists(new_filename):#断点续传
                recv_size = os.stat(new_filename).st_size
                self.request.send(bytes(str(recv_size), encoding='utf-8'))
                with open(new_filename,'ab') as f:
                    while recv_size < int(filesize):
                        data = self.request.recv(size)
                        f.write(data)
                        recv_size += len(data)
                        print('filesize: %s  recvsize:%s' % (filesize, recv_size))
                    else:
                        print("%s has exit!"%filename)
            else:#新文件上传
                recv_size = 0
                self.request.send(bytes('s', encoding='utf-8'))
                with open(new_filename, 'wb') as f:
                    while recv_size < filesize:
                        data = self.request.recv(size)
                        f.write(data)
                        recv_size += len(data)
                        print('filesize: %s  recvsize:%s' % (filesize, recv_size))
            print("file recv success")
        else:
            print("传输文件大小超出配额范围>>%s"%user_bufsize)
            self.request.send(bytes('传输文件大小超出配额范围！', encoding='utf-8'))
    def task_get(self, *args, **kwargs):
        print("---get", args, kwargs)
        filename = args[0].get("filename")
        new_filename = os.path.join(user_catalog, filename)

        if os.path.exists(new_filename):

            file_size = os.stat(new_filename).st_size
            print('get', filename, file_size)
            ready_tag = 'Ready|%s' % file_size
            self.request.send(bytes(ready_tag, encoding='utf-8'))  # 1发送数据长度
            if self.request.recv(BUFSIZE).decode() == 'Start':
                size = 1024 * 1024
                r = self.request.recv(BUFSIZE).decode()
                if r == 's':
                    has_send = 0
                else:
                    has_send = int(r)

                with open(new_filename, 'rb') as f:
                    f.seek(has_send)
                    while has_send < file_size:
                        data = f.read(size)
                        self.request.send(data)
                        has_send += len(data)
                        time.sleep(0.4)
                        view_bar(has_send, file_size)
                print('send file done')
        else:
            self.request.send(bytes('the file is not exit!',encoding='utf-8'))
            print('the file %s is not exit!'%new_filename)


    def task_help(self, *args, **kwargs):
        result = '''\033[33;1m
                            ?\help:     Get help.
                            Get:        Download file from remote server.
                            Send:       Send local file to remote server.
                            ls:         List local file.
                            rls:        List remote server file.
                            cd:         change file catalog.
                            quit\exit:  Quit the app.
                            \033[0m'''
        self.request.send(bytes(result, encoding='utf-8'))
    def task_cd(self,*args,**kwargs):

        args[0].get('action') == 'cd'
        filepath = args[0].get('filename')
        if filepath == '..'or filepath =='':
            send_data = os.getcwd()
        elif os.path.exists(os.getcwd()+'\\'+filepath):
            filename = 'FTP\\' + filepath.split("\\")[-1]  # 只能在基础目录的范围内切换
            send_data = os.path.join(user_catalog, filename)
            os.chdir(send_data)
        else:
            send_data ="the catalog is not exit!"
            print("the catalog is not exit!")

            # os.getcwd()
        send_data = bytes(send_data, encoding='utf8')
        # 解决粘包问题
        ready_tag = 'Ready|%s' % len(send_data)
        print(ready_tag)
        self.request.send(bytes(ready_tag, encoding='utf8'))  # 1发送数据长度
        feedback = self.request.recv(BUFSIZE)  # 4接收确认信息
        feedback = str(feedback, encoding='utf8')

        if feedback.startswith('Start'):
            self.request.send(send_data)  # 发送命令的执行结果


    def task_ls(self,*args,**kwargs):
        args[0].get('action') == 'ls'
        ls = os.listdir(user_catalog)
        print(ls)
        send_data = ','.join(ls)
        send_data = bytes(send_data, encoding='utf8')

        # 解决粘包问题
        ready_tag = 'Ready|%s' % len(send_data)
        print(ready_tag)
        self.request.send(bytes(ready_tag, encoding='utf8'))  # 1发送数据长度
        feedback = self.request.recv(BUFSIZE)  # 4接收确认信息
        feedback = str(feedback, encoding='utf8')

        if feedback.startswith('Start'):
            self.request.send(send_data)  # 发送命令的执行结果

    def task_other(self, *args, **kwargs):
        # p = subprocess.Popen(str(args[0].get("INPUT"), encoding='utf8'), shell=True,
        #                      stdout=subprocess.PIPE)  # 执行系统命令，windows平
        # 台命令的标准输出是gbk编码，需要转换

        p = subprocess.Popen(args[0].get("INPUT"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        res = p.stdout.read()  # 获取标准输出

        if len(res) == 0:  # 执行错误命令，标准输出为空，
            send_data = 'cmd err'
        else:
            send_data = str(res, encoding='gbk')  # 命令执行ok，字节gbk---->str---->字节utf-8

        send_data = bytes(send_data, encoding='utf8')

        # 解决粘包问题
        ready_tag = 'Ready|%s' % len(send_data)
        print(ready_tag)
        self.request.send(bytes(ready_tag, encoding='utf8'))  # 1发送数据长度
        feedback = self.request.recv(BUFSIZE)  # 4接收确认信息
        feedback = str(feedback, encoding='utf8')

        if feedback.startswith('Start'):
            self.request.send(send_data)  # 发送命令的执行结果

def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r1 = '\r%s>%d%%' %(num, rate_num)
    sys.stdout.write(r1)
    sys.stdout.flush()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyFtpHandler)
    server.serve_forever()
