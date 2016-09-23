#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
import re
# origin = "hasaabc dfuojqw halaabc m098u2934l"
# # r = re.match("h\w+", origin)
# # r = re.match("h(\w+)", origin)
# r = re.findall("h(\w+)a(ab)c", origin)
# print(r)
# print(r.group())     # 获取匹配到的所有结果
# print(r.groups())    # 获取模型中匹配到的分组结果
# print(r.groupdict()) # 获取模型中匹配到的分组结果
 # 无分组
origin = "hello alex bcd alex lge alex acd 19"
r = re.split("alex", origin, 1)
print(r)

# 有分组
#
origin = "hello alex bcd alex lge alex acd 19"
r1 = re.split("(alex)", origin, 1)
print("r1>>",r1)
r2 = re.split("(al(e(x)))", origin, 1)
print("r2>>",r2)


def fun(ex):
    if ex!=None:
        ex= re.findall(r"\((.+)\)", ex[0])
        print("r3>>", r3)

# 无分组
origin = "hello alex b(c(r(e))r)d adf+bcd lge acd 19"
r3 = re.findall(r"\((.+)\)", origin)
while r3!=[]:
    if r3!=[]:
        r3= re.findall(r"\((.+)\)", r3[0])
        print("r3>>", r3)
    else:
        print("r3 is None")






# 有分组
# origin = "hello alex bcd abcd lge acd 19"
r4 = re.findall("a((\w*\W*)c)(d)", origin)
print("r4>>",r4)