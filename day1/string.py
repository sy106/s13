#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

name='sy106,sy107,sy108'
print name
name2=name.split(',')
print name2
name3=('!'.join(name2))
print name3

name4 = "sy106"
print""in name4
print name4.center(40,'-')
# print name4.capitalize()

msg="Hello ,{name},it's been a long {age} since last time spoke..."
msg1=msg.format(name='sy106',age=333)
print msg1