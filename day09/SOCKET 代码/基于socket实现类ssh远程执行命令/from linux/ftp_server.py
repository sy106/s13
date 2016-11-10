#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li


#!/usr/bin/env python
# -*- coding:utf-8 -*-
#import SocketServer
import socketserver,json
class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        try:
        # print self.request,self.client_address,self.server
            self.request.sendall(bytes('欢迎访问FTP.',encoding="utf-8"))
            while True:
                data = self.request.recv(1024)
                if len(data) == 0:break
                print("data", data)
                print("[%s] says:%s" % (self.client_address,data.decode() ))

                task_data = json.loads( data.decode() )
                task_action = task_data.get("action")
                if hasattr(self, "task_%s"%task_action):
                   func = getattr(self,"task_%s" %task_action)
                   func(task_data)
                else:
                   print("task action is not supported",task_action)
        except Exception as e:
            print ("has error:",e)

    def task_put(self,*args,**kwargs):
        print("---put",args,kwargs)         
        filename = args[0].get('filename')
        filesize = args[0].get('file_size')
        server_response = {"status":200}
        self.request.send(bytes( json.dumps(server_response), encoding='utf-8'  ))
        f = open(filename,'wb')
        recv_size = 0
        while recv_size < filesize:
            data = self.request.recv(4096)
            f.write(data)
            recv_size += len(data)
            print('filesize: %s  recvsize:%s' % (filesize,recv_size))
        print("file recv success")
        f.close()

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',8009),MyServer)
    server.serve_forever()


