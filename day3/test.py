#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import json
#
# inp_str = "[11,22,33,44]"
# inp_list = json.loads(inp_str)  # 根据字符串书写格式，将字符串自动转换成 列表类型
#
#
# inp_str = ' {"k1":123, "k2": "wupeiqi"} '  # 正确的输入      切记，内部必须是 双引号 ！！！
# # inp_str = " {'k1':123, 'k2': 'wupeiqi'}"   # 错误的输入
# inp_dict = json.loads(inp_str)  # 根据字符串书写格式，将字符串自动转换成 字典类型
#
# print(inp_list,inp_dict)

# read = input(
#     'pls input the add record:')  # 如: {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
# read_dict = json.loads(read)
# print(read_dict)
# 如: {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
# 讲read字符串转换成 字典类型
# backend_title = read_dict['backend']  # backend 下的值
# record_dict = read_dict['record']
# server = record_dict['server']
# weight = record_dict['weight']
# maxconn = record_dict['maxconn']
# print(server, weight, maxconn)
# with open('config_old', 'r', encoding="utf-8") as f1, open("config_new", 'w', encoding="utf-8") as f2:
#     for line in f1:
#         f2.write(line)
#         if line.strip() == 'backend' + ' ' + backend_title:  # 如果匹配到输入的内容，就输出标题下的内容
#             str = 'server ' + server + 'weight ' + weight + 'maxconn ' + maxconn
#             f2.write(str)
#             f2.write('\n')
#             list = f1.readlines()
#             f2.writelines(list)
#         else:
#             list = f1.readlines()
#             f2.writelines(list)


# encoding: utf-8
import os
import os.path
import shutil
# curDir = os.getcwd()
# oldId = "config_back"
# newId = "config_old"
# for parent, dirnames, filenames in os.walk(curDir):
#     for filename in filenames:
#         if filename.find(oldId) != -1:
#             newName = filename.replace(oldId, newId)
#             print(filename, "---->", newName)
#             os.rename(os.path.join(parent, filename), os.path.join(parent, newName))

# def backupFile():
#     with open('config_old', 'r', encoding="utf-8") as f1, open("config_old_back", 'w', encoding="utf-8") as f2:
#     f2.writelines(f1.read())
#
# backupFile()

# # 去配置文件中找到指定的节点，并在删除指定记录，如:
# backend test.oldboy.org
# server 100.1.7.10 100.1.7.10 weight 20 maxconn 3000
# server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000   # 删除掉
# # （可选）如果backend下所有的记录都已经被删除，那么将当前 backend test.oldboy.org 也删除掉。

read =input('pls input the delete record:')
# 输入要删除的记录
# 如: {"backend": "www.oldboy.org","record":{"server": "100.1.7.90","weight": 20,"maxconn": 300}}
read_dict = json.loads(read)
backend_title = read_dict['backend']  # backend 下的值
record_dict = read_dict['record']
server = record_dict['server']
weight = str(record_dict['weight'])
maxconn = record_dict['maxconn']
msg="""server %s %s weight %s maxconn %s"""
with open('config_old', 'r', encoding="utf-8") as f1, open("config_new", 'w+', encoding="utf-8") as f2:
    lable = False
    for line in f1:
        if line.strip() == 'backend' + ' ' + backend_title:  # 如果找到删除的记录,就不写到新文件里
            f2.write(line)

            lable = True
            list = f1.readlines()
            print(list)
            test_str=msg % (server,server, weight, maxconn)
            print(test_str)
            for i in list:
                if i.strip()==test_str:
                    index=list.index(i)
                    print('test1',list[0:index])
                    print('test2', list[index+1:])
                    f2.writelines(list[0:index])
                    f2.writelines(list[index+1:])
                    break
                else:
                   continue
        else:
           f2.write(line)



