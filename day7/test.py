#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import re
# inpp = "8*12+(6-(5*6-2)/77+2)*(3-7)+8"
# # inpp2=8*12+(6-(5*6-2)/77+2)*(3-7)+8
# result = re.split('\(([^()])\)',inpp,1)
#
# result1=re.split('(\w+)\)',inpp,1)
# print(result,'\n',result1)
#
# # 无分组
# origin = "hello alex bcd alex lge alex acd 19"
# r = re.split("alex", origin, 1)
# print(r)
#
# # 有分组
#
# origin = "hello alex bcd alex lge alex acd 19"
# r1 = re.split("a(\w+)x", origin)
# print(r1)
# r2 = re.split("(al(ex))", origin, 1)
# print(r2)
# r3= re.split("(al(e(x)))", origin, 1)
# print(r3)

test="8*12+(6-(5*6-2)/77+2)*(3-7)+8"

res= re.findall(r'\((\w*)',test)#根据非数字分
res2=re.findall('\w+',test)#根据数字分
res3=re.split('\((\w+)\)',test,1)
res4=re.findall(r"[\(][^\(\)]+\.+[^\(\)]+[\)]",test)
res5=re.split(r"\((\d+[\+\-\*\/]\d+)\)",test,1)

print(res)
print(res2)
print(res3)
print(res4)
print(res5)



