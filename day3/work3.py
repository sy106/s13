#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

num = input('请输入操作序号:')

if num== 1:
    read = input('请输入backend:')
    # 如输入:www.oldboy.org
    # 讲配置文件 backend www.oldboy.org 节点下的所有记录获取到，并输入到终端

elif num== 2:
    read = input('请输入要新加的记录:')
    # 如: {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}
    # 讲read字符串转换成 字典类型
    read_dict = json.loads(read)

backend_title = read_dict['backend']
    # 去配置文件中找到指定的节点:
    # backend test.oldboy.org
    # 如果已经存在，
        # 则在此节点下添加根据用输入构造出的记录，例如:
            server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
# 如果不存在，
        # 则添加backend节点和记录，例如:
    backend test.oldboy.org
server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000
# （可选）可以再对节点下记录进行判断是否已经存在
if num== 3:
    read = input('请输入要删除的记录:')
如: {"backend": "test.oldboy.org","record":{"server": "100.1.7.9","weight": 20,"maxconn": 30}}

# 将read字符串转换成 字典类型
read_dict = json.loads(read)
backend_title = read_dict['backend']
# 去配置文件中找到指定的节点，并在删除指定记录，如:
backend test.oldboy.org
server 100.1.7.10 100.1.7.10 weight 20 maxconn 3000
server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000   # 删除掉
# （可选）如果backend下所有的记录都已经被删除，那么将当前 backend test.oldboy.org 也删除掉。

