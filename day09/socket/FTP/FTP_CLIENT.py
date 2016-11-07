#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import socket, os, pickle


# class FtpClient(object):
#    def __init__(self,ip,port):
#        self.ip=ip
#        self.port=port
#        self.s=socket.socket()
#        self.s.connect((self.ip,self.port))

#       self.i

def auth():
    while True:
        try:
            recv_msg = s.recv(BUFSIZE)
            if recv_msg == 'auth':
                USER = input('Please input your username:>>').strip()
                s.send(bytes(USER, encoding='utf8'))
                if s.recv(BUFSIZE) == 'pauth':
                    PASS = input('Please input your password:>>').strip()
                    s.send(bytes(PASS, encoding='utf8'))
                    recv_msgl = s.recv(BUFSIZE).decode()
                    if recv_msgl == 'ok2login':
                        print('\033[33;1mlogin success!!!\033[0m')
                        break
                    elif recv_msgl == 'fail2login':
                        print('\033[33;1mlogin failure!!!\033[0m')
                        continue
                    else:
                        continue

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
            s.send(bytes(INPUT, encoding='utf8'))
            recv_data = s.recv(BUFSIZE)
            print(recv_data.decode())
            continue
        elif INPUT == 'get' or INPUT == 'send':
            print('\033[33;1mYou must specified filename!!\033[0m')
            continue
        elif INPUT == 'ls':
            cmd = os.popen('ls -l ./').read()
            print(cmd)
            continue
        elif INPUT == 'rls':
            s.send(bytes(INPUT, encoding='utf8'))
            recv_data = s.recv(BUFSIZE).decode()
            print(recv_data)
            continue
        elif INPUT.split()[0] == 'send':
            abs_filepath = INPUT.split()[1]
            if os.path.isfile(abs_filepath):
                file_size = os.stat(abs_filepath).st_size
                filename = abs_filepath.split("\\")[-1]
                print('file:%s size:%s' % (abs_filepath, file_size))
                msg_data = {"action": "send",
                            "filename": filename,
                            "file_size": file_size}
                s.send(bytes(pickle.dumps(msg_data), encoding="utf-8"))
                server_confirmation_msg = s.recv(BUFSIZE).decode()
                confirm_data = pickle.loads(server_confirmation_msg)
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
            msg1 = s.recv(BUFSIZE).decode()
            if msg1 == 'ok2send':
                s.send(bytes('ok2get', encoding="utf-8"))
                msg2 = s.recv(BUFSIZE).decode()
                if msg2 == 'sending ':
                    file_data = s.recv(BUFSIZE)
                    file2w = open(abs_filepath, 'wb')
                    # for line in file2w:
                    #    s.send(line)
                    file2w.write(file_data)
                    file2w.flush()
                    file2w.close()
                    msg3 = s.recv(BUFSIZE)
                    print(msg3)
                    continue
                elif msg1 == 'fail2get':
                    s.send(bytes('ack', encoding='utf8'))
                    msg4 = s.recv(BUFSIZE)
                    print(msg4)
                    continue


if __name__ == '__main__':
    HOST = input("Server IP:>>").strip()
    PORT = int(input("Server PORT:>>")).strip()
    ADDR = (HOST, PORT)
    BUFSIZE = 2048

    s = socket.socket()
    try:
        s.connect(ADDR)
    except:
        pass

    if auth() == 'error':
        print('connection refused')
    else:
        switch()
