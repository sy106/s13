#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import socket, os,json


# class FtpClient(object):
#    def __init__(self,ip,port,):
#        self.ip=ip
#        self.port=port
#        self.s=socket.socket()
#        self.s.connect((self.ip,self.port))
ip_port=('127.0.0.1',8009)
s=socket.socket()
s.connect(ip_port)

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
                        continue
                    else:
                        break

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
            s.send(bytes(INPUT, encoding='utf-8'))
            recv_data = s.recv(BUFSIZE)
            print(recv_data.decode())
        elif INPUT == 'get' or INPUT == 'send':
            print('\033[33;1mYou must specified filename!!\033[0m')

        # elif INPUT == 'ls':
        #     cmd = os.popen('ls -l ./').read()
        #     print(cmd)

        elif INPUT == 'rls':
            s.send(bytes(INPUT, encoding='utf-8'))
            recv_data = s.recv(BUFSIZE)
            print(recv_data.decode())

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
                server_confirmation_msg = s.recv(BUFSIZE).decode()
                confirm_data = json.loads(server_confirmation_msg)
                if confirm_data['status'] == 200:
                    print("start sending file ", filename)
                    f = open(abs_filepath, 'rb')
                    for line in f:
                        s.send(line)
                    f.close()
                    print('send file done')
                else:
                    print('\033[33;1m%s not found\033[0m' % filename)
        elif INPUT.split()[0] == 'get':
            abs_filepath = INPUT.split()[1]
            s.send(bytes(INPUT, encoding="utf-8"))
            ready_tag = s.recv(BUFSIZE).decode()
            # ready_tag = str(ready_tag, encoding='utf8')
            msg_size = 0
            if ready_tag.startswith('Ready'):  # Ready|9998
                msg_size = int(ready_tag.split('|')[-1])  # 获取待接收数据长度
            start_tag = 'Start'
            s.send(bytes(start_tag, encoding='utf-8'))  # 3发送确认信息

            # 基于已经收到的待接收数据长度，循环接收数据
            recv_size = 0
            f = open(abs_filepath, 'wb')
            while recv_size < msg_size:
                recv_data = s.recv(BUFSIZE)
                f.write(recv_data)
                recv_size += len(recv_data)
                print('filesize: %s  recvsize:%s' % (msg_size, recv_size))
            print("file recv success")
            f.close()
        else:
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

            print(str(recv_msg, encoding='utf8'))
            # if msg1 == 'ok2send':
            #     s.send(bytes('ok2get', encoding="utf-8"))
            #     msg2 = s.recv(BUFSIZE).decode()
            #     if msg2 == 'sending ':
            #         file_data = s.recv(BUFSIZE)
            #         file2w = open(abs_filepath, 'wb')
            #         # for line in file2w:
            #         #    s.send(line)
            #         file2w.write(file_data)
            #         file2w.flush()
            #         file2w.close()
            #         msg3 = s.recv(BUFSIZE)
            #         print(msg3)
            #         continue
            #     elif msg1 == 'fail2get':
            #         s.send(bytes('ack', encoding='utf8'))
            #         msg4 = s.recv(BUFSIZE)
            #         print(msg4)
            #         continue


if __name__ == '__main__':
    BUFSIZE = 4096
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
