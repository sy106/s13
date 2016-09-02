#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li

f = open("config_old","r+", encoding="utf-8")
list=f.readlines()
num=list.index('backend www.oldboy.org\n')
print(f.readline(num))