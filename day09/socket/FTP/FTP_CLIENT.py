#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import socket,os,json,sys,time


# class FtpClient(object):
#    def __init__(self,ip,port,):
#        self.ip=ip
#        self.port=port
#        self.s=socket.socket()
#        self.s.connect((self.ip,self.port))
ip_port=('127.0.0.1',8009)
s=socket.socket()
s.connect(ip_port)
BUFSIZE = 4096
def auth():
    while True:
        try:
            recv_msg = s.recv(BUFSIZE).decode()
            if recv_msg == 'auth':
                USER = input('Please input your username:>>').strip()
                s.send(bytes(USER, encoding='utf8'))
                if s.recv(BUFSIZE).decode() == 'pauth':
                    PASS = input('Please input your password:>>').strip()
                    s.send(bytes(PASS, encoding='utf8'))
                    recv_msgl = s.recv(BUFSIZE).decode()
                    if recv_msgl == 'ok2login':
                        print('\033[33;1mlogin success!!!\033[0m')
                        return True
                    elif recv_msgl == 'fail2login':
                        print('\033[33;1mlogin failure!!!\033[0m')
                        return False

        except Exception as e:
            print(e)


def switch():
    while True:
        INPUT = input('ftp:>>').strip()
        if len(INPUT) == 0:
            continue

        elif INPUT == 'quit' or INPUT == 'exit':
            s.close()
            break

        elif INPUT == '?' or INPUT == 'help':
            msg_data = {"action": "help"}
            s.send(bytes(json.dumps(msg_data), encoding="utf-8"))
            recv_data = s.recv(BUFSIZE)
            print(recv_data.decode())

        elif INPUT == 'get' or INPUT == 'send':
            print('\033[33;1mYou must specified filename!!\033[0m')

        elif INPUT.split()[0] == 'send':
            abs_filepath = INPUT.split()[1]
            if os.path.isfile(abs_filepath):
                file_size = os.stat(abs_filepath).st_size
                filename = abs_filepath.split("\\")[-1]
                print('file:%s size:%s' % (abs_filepath, file_size))
                msg_data = {"action": "send",
                            "filename": filename,
                            "file_size": file_size}
                s.send(bytes(json.dumps(msg_data), encoding="utf-8"))
                r= s.recv(BUFSIZE).decode()
                size = 1024*1024
                if r =='s':
                    has_send = 0
                    print('\033[33;1m%s not found\033[0m' % filename)
                elif r =='传输文件大小超出配额范围！':
                    print("传输文件大小超出配额范围！请压缩后再传！")
                    continue
                else:
                    has_send = int(r)

                with open(abs_filepath,'rb') as f:
                    f.seek(has_send)
                    while has_send < file_size:
                        data = f.read(size)
                        s.send(data)
                        has_send += len (data)
                        time.sleep(0.4)
                        view_bar(has_send,file_size)
                print('send file done')
        elif INPUT.split()[0] == 'get':
            abs_filepath = INPUT.split()[1]
            filename = abs_filepath.split("\\")[-1]
            msg_data = {"action": "get",
                        "filename": filename}
            s.send(bytes(json.dumps(msg_data), encoding="utf-8"))
            ready_tag = s.recv(BUFSIZE).decode()
            print("test2", ready_tag)
            if ready_tag.startswith('Ready'):  # Ready|9998
                msg_size = int(ready_tag.split('|')[-1])  # 获取待接收数据长度
                start_tag = 'Start'
                s.send(bytes(start_tag, encoding='utf-8'))  # 3发送确认信息
                size = 1024 * 1024
                if os.path.exists(abs_filepath):  # 断点续传
                    recv_size = os.stat(abs_filepath).st_size
                    s.send(bytes(str(recv_size), encoding='utf-8'))
                    with open(abs_filepath, 'ab') as f:
                        while recv_size < int(msg_size):
                            data = s.recv(size)
                            f.write(data)
                            recv_size += len(data)
                            time.sleep(0.4)
                            view_bar(recv_size, msg_size)
                            # print('filesize: %s  recvsize:%s' % (msg_size, recv_size))
                        else:
                            print("%s has exit!" % filename)
                else:  # 新文件下载
                    recv_size = 0
                    s.send(bytes('s', encoding='utf-8'))
                    with open(abs_filepath, 'wb') as f:
                        while recv_size < msg_size:
                            data = s.recv(size)
                            f.write(data)
                            recv_size += len(data)
                            time.sleep(0.4)
                            view_bar(recv_size, msg_size)
                            # print('filesize: %s  recvsize:%s' % (msg_size, recv_size))
                print("file recv success")

        else:
            if INPUT.split()[0] == 'cd':
                if INPUT == 'cd':
                    abs_filepath=''
                else:
                    abs_filepath = INPUT.split()[1]
                msg_data = {"action": "cd",
                            "filename": abs_filepath}

            elif INPUT.split()[0] == 'ls':

                msg_data = {"action": "ls"}
            else:
                msg_data = {"action": 'other',
                            "INPUT":INPUT}
            s.send(bytes(json.dumps(msg_data), encoding="utf-8"))
            ready_tag = s.recv(BUFSIZE)  # 2收取带数据长度的字节：Ready|9998
            ready_tag = str(ready_tag, encoding='utf8')
            msg_size = 0
            if ready_tag.startswith('Ready'):  # Ready|9998
                msg_size = int(ready_tag.split('|')[-1])  # 获取待接收数据长度
            start_tag = 'Start'
            s.send(bytes(start_tag, encoding='utf8'))  # 3发送确认信息

            # 基于已经收到的待接收数据长度，循环接收数据
            recv_size = 0
            recv_msg = b''
            while recv_size < msg_size:
                recv_data = s.recv(BUFSIZE)
                recv_msg += recv_data
                recv_size += len(recv_data)
                print('MSG SIZE %s RECE SIZE %s' % (msg_size, recv_size))

            recv_msg = recv_msg.decode()
            if ',' in recv_msg:
                li = recv_msg.split(',')
                for i in li:
                    print(i)
            else:
                print(recv_msg)





def view_bar(num, total):
    rate = num / total
    rate_num = int(rate * 100)
    r1 = '\r%s>%d%%' %(num, rate_num)
    sys.stdout.write(r1)
    sys.stdout.flush()

if __name__ == '__main__':

    if auth():
        switch()
    else:
        print("connection refused!")




    # HOST = '127.0.0.1'
    # PORT = 8009
    # ADDR = (HOST, PORT)
    # BUFSIZE = 4096
    #
    # s = socket.socket()
    # try:
    #     s.connect(ADDR)
    # except:
    #     pass
    # auth()
    # if auth() == 'error':
    #     print('connection refused')
    # else:
    #     switch()
