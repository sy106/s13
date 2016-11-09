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
            while True:
                self.request.send(bytes('auth',encoding="utf-8"))
                name = self.request.recv(BUFSIZE).decode()
                sleep(1)
                self.request.send(bytes('pauth', encoding="utf-8"))

                password = self.request.recv(BUFSIZE).decode()
                print(name,password)
                auth_result = userinfo.check(name,commons.md5(password))
                if auth_result == 0:
                    self.request.sendall(bytes('ok2login', encoding="utf-8"))

                elif auth_result == 1:
                    self.request.sendall(bytes('fail2login', encoding="utf-8"))
                    continue

                recv_data = self.request.recv(BUFSIZE)
                recv_data1 = recv_data.decode()
                print(recv_data1)
                if len(recv_data) == 0:break #客户端如果退出，服务端将收到空消息，退出

                elif recv_data1 == '?' or recv_data1 == 'help':
                    result = '''\033[33;1m
                    ?\help:     Get help.
                    Get:        Download file from remote server.
                    Send:       Send local file to remote server.
                    ls:         List local file.
                    rls:        List remote server file.
                    cd:         change file catalog.
                    quit\exit:  Quit the app.
                    \033[0m'''
                    self.request.send(bytes(result,encoding='utf-8'))

                elif json.loads(recv_data1)['action'] == 'send':
                    data = json.loads(recv_data1)
                    filename = data['filename']
                    filesize = data['file_size']
                    server_response = {"status": 200}
                    self.request.send(bytes(json.dumps(server_response), encoding='utf-8'))

                    # recv_data = self.request.recv(BUFSIZE)
                    # file2w = open(filename,'wb')
                    # file2w.write(recv_data)
                    # file2w.flush()
                    # file2w.close()
                    # self.request.sendall(bytes('\033[33;1mFile transfer successed!\033[0m', encoding="utf-8"))

                    f = open(filename, 'wb')
                    recv_size = 0
                    while recv_size < filesize:
                        data = self.request.recv(BUFSIZE)
                        f.write(data)
                        recv_size += len(data)
                        print('filesize: %s  recvsize:%s' % (filesize, recv_size))
                    print("file recv success")
                    f.close()

                elif  recv_data1[0] == 'get':
                    abs_filepath = recv_data1[1]
                    file_size = os.stat(abs_filepath).st_size
                    filename = abs_filepath.split("\\")[-1]

                    ready_tag = 'Ready|%s' % file_size
                    if os.path.isfile(filename):
                        self.request.send(bytes(ready_tag, encoding='utf-8'))  # 1发送数据长度
                        if self.request.recv(BUFSIZE) == 'Start':
                            f = open(filename,'rb')
                            for line in f:
                                self.request.send(line)
                            print("send file done! ")
                            f.close()
                else:
                    # 发消息
                    print("fffff")
                    p = subprocess.Popen(str(recv_data, encoding='utf8'), shell=True,
                                         stdout=subprocess.PIPE)  # 执行系统命令，windows平
                    # 台命令的标准输出是gbk编码，需要转换
                    res = p.stdout.read()  # 获取标准输出
                    print("tttttt", res)
                    if len(res) == 0:  # 执行错误命令，标准输出为空，
                        send_data = 'cmd err'
                    else:
                        send_data = str(res, encoding='gbk')  # 命令执行ok，字节gbk---->str---->字节utf-8

                    send_data = bytes(send_data, encoding='utf8')

                    # 解决粘包问题
                    ready_tag = 'Ready|%s' % len(send_data)
                    self.request.send(bytes(ready_tag, encoding='utf8'))  # 1发送数据长度
                    feedback = self.request.recv(1024)  # 4接收确认信息
                    feedback = str(feedback, encoding='utf8')

                    if feedback.startswith('Start'):
                        self.request.send(send_data)  # 发送命令的执行结果



        # except Exception as e:
        #     print(e)
if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyFtpHandler)
    server.serve_forever()
