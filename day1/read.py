#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106


f = file('user.txt','w')
#a = file("lock.txt")
f.write("sy106 123\n")
f.write('admin admin\n')
f.write('Alex 123')
f.close()

f=file('user.txt')
a=f.read()
print "a read is:\n" ,a
d='-'
print d.center(40,'-')
f=file('user.txt')
b=f.readline()
print"b readline() is:\n" ,b
f=file('user.txt')
d='-'
print d.center(40,'-')
c=f.readlines()
d=c[0].split()
e=c[1].split()
print"c readlines() is:\n" ,c,d[0],d[1],e[0],e[1]


