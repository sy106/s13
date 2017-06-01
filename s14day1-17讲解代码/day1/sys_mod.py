__author__ = "Alex Li"
#import login

'''import sys
#print(sys.path) #打印环境变量
print(sys.argv)
print(sys.argv[2])

import os

#cmd_res = os.system("dir") #执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("-->",cmd_res)
os.mkdir("new_dir")'''


msg = "我爱北京天安门"

print(msg)

print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))