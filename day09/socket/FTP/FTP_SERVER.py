#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:sy106

import socketserver,os,time,subprocess,json
from time import sleep
from day09.socket.FTP import userinfo
from day09.socket.FTP import commons

BUFSIZE =4096
class MyFtpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # try:
        self.request.send(bytes('auth', encoding="utf-8"))
        name = self.request.recv(BUFSIZE).decode()
        sleep(1)
        self.request.send(bytes('pauth', encoding="utf-8"))
        password = self.request.recv(BUFSIZE).decode()
        print(name, password)
        auth_result = userinfo.check(name, commons.md5(password))
        if auth_result == 0:
            self.request.sendall(bytes('ok2login', encoding="utf-8"))
        elif auth_result == 1:
            self.request.sendall(bytes('fail2login', encoding="utf-8"))
        while True:
                recv_data = self.request.recv(BUFSIZE)
                recv_data1 = recv_data.decode()
                if len(recv_data) == 0:break #客户端如果退出，服务端将收到空消息，退出
                # print("data", recv_data1)
                print("[%s] says:%s" % (self.client_address, recv_data1))

                task_data = json.loads(recv_data1)
                task_action = task_data.get("action")
                if hasattr(self, "task_%s" % task_action):
                    func = getattr(self, "task_%s" % task_action)
                    func(task_data)
                else:
                   print("task action is not supported",task_action)

    def task_send(self, *args, **kwargs):
        print("---send", args, kwargs)
        filename = args[0].get('filename')
        filesize = args[0].get('file_size')
        server_response = {"status": 200}
        self.request.send(bytes(json.dumps(server_response), encoding='utf-8'))
        f = open(filename, 'wb')
        recv_size = 0
        while recv_size < filesize:
            data = self.request.recv(BUFSIZE)
            f.write(data)
            recv_size += len(data)
            print('filesize: %s  recvsize:%s' % (filesize, recv_size))
        print("file recv success")
        f.close()

    def task_get(self, *args, **kwargs):
        print("---get", args, kwargs)
        abs_filepath = args[0].get("filename")
        file_size = os.stat(abs_filepath).st_size
        filename = abs_filepath.split("\\")[-1]
        print('get', filename, file_size)
        ready_tag = 'Ready|%s' % file_size
        if os.path.isfile(filename):
            self.request.send(bytes(ready_tag, encoding='utf-8'))  # 1发送数据长度
            if self.request.recv(BUFSIZE).decode() == 'Start':
                f = open(filename, 'rb')
                for line in f:
                    # self.request.send(bytes(line, encoding='utf-8'))
                    self.request.send(line)
                print("send file done! ")
                f.close()

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
        self.request.send(bytes(ready_tag, encoding='utf8'))  # 1发送数据长度
        feedback = self.request.recv(BUFSIZE)  # 4接收确认信息
        feedback = str(feedback, encoding='utf8')

        if feedback.startswith('Start'):
            self.request.send(send_data)  # 发送命令的执行结果

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyFtpHandler)
    server.serve_forever()
