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

# test="8*12+(6-(5*6-2)/77+2)*(3-7)+8"
#
# res= re.split('\-',test)#根据非数字分
# res2=re.split('\w+',test)#根据数字分,分出来的全是字符
# res3=re.sub(' ','',test)
# # res4=re.findall(r"[\(][^\(\)]+\.+[^\(\)]+[\)]",test)
# res4=re.findall('\(',test)
#
# res5=re.findall('\)',test)
# res6=re.sub('\(',' ',test)
# res7=re.sub('\)',' ',res6)
# res8=re.findall('(\d+[\*\/\+\-]\d+)',res7)
# num=len(res8)
# res9=eval(test)
# print(res9)
# # for i in range(num):
# #    print(res8[i])
# #    num1=len(res8[i])
# #    for k in range(num1):
# #        sum=res8[i].split([])
# #        print(sum)
#
# key=5*6
# print(type(key))

# res5=re.split(r"\((\d[\+\-\*\/]\d[\+\-\*\/]\d)\)",test,1)
# # res5=re.split(r"\((\d+[\+\-\*\/]\d+)\)",res5[0],1)
# res6=re.split(r"\((\d[\+\-\*\/]\d)\)",res5[0])
# res6=re.split(r"\((\d[\+\-\*\/]\d)\)",res6[0])
# num=len(res2)
# for i in range(num):
#     res2[i]=re.split('(\()',res2[i])
#     if res2[i]=="(":
#         print(res2[i])

# while True:
#     if res5!=[]:
#         res5= re.split("\((\d+[\+\-\*\/]\d+)\)",res5[0])
#         print("res5>>", res5)
#     else:
#         print("res5 is None")
#         break
# m = re.search("\(([^()]*)\)",test).groups()
# content=re.split("\(([^()]*)\)",test,1)
# print(content)
# num=len(content)
# print(num)
# for i in range(num):
#     if re.findall('[()]',content[i])==[]:
#         print(content[i])
#         print(i)

# test2="20+300-100"
# mch = re.search("(\d+[*/]\d+)", test2)
# print(mch)

# def firstvalue(a,b):
#  c = a + b
#  return 6
#
# value=firstvalue(1,2)
# print(value )
# def compute_mul_div(expresstion):
#     calc_list = re.split("[\W]", expresstion)  # 用* or /分割公式,得到数字
#     operators = re.findall("[\w]", expresstion)  # 找出所有*和／号，得到
#     res = None
#     for index, i in enumerate(calc_list):
#         if res:
#             if operators[index - 1] == '*':
#                 res *= float(i)
#             elif operators[index - 1] == '/':
#                 res /= float(i)
#         else:
#             res = float(i)
#     print("[%s]运算结果=" % expresstion, res)
#     return res

# print(res2)
# print(res3)
# print(res4)
# print(res5)
# print(res6)
# print(res7)
# print(res8)



# inpp = "-20.5+200.6*-3/-200*-300-100"
inpp = "20.5+200.6+-300-100"
# def compute_mul_div(arg):
#     """ 操作乘除
#         :param expression:表达式
#         :return:计算结果"""
#     # calc_list = re.split("(\d+[*/]\d+)", arg, 1)  # 用* or /分割公式,得到数字
#     # operators = re.search("[*/]", calc_list[1]).group()  # 找出所有*和／号，得到字符
#
#     mch = re.search("([-]*\d+\.*\d*[*/][-]*\d+\.*\d*)", arg)
#     print("arg",arg)
#     print("mch",mch)
#     if mch==None:
#         print("arg",arg)
#         return arg
#
#     before, nothing, after = re.split("([-]*\d+\.*\d*[*/][-]*\d+\.*\d*)", arg, 1)#用* or /分割公式,得到中间的计算式
#     print(before, '>>', nothing, '>>', after)
#     print('before*/：',  arg)
#
#     content = re.split("[*/]", nothing)#得到表达式第一个*或者/的数字
#     operator = re.split('([*/])', nothing)#得到表达式第一个*或者/的符号
#     print("content", content[0],content[1])
#     print("operator", operator)
#
#     if operator[1] == '*':
#         value = float(content[0]) * float(content[1])
#     else:
#         value = float(content[0])/float(content[1])
#     value=float(value)
#     print("结果：》",value)
#     new_str = "%s%s%s" % (before, value, after)
#     print("new_str*/",new_str)
#     arg = new_str
#     return compute_mul_div(arg)
#
#
#
# compute_mul_div(inpp)

def compute_add_sub(arg):
    """ 操作加减
    :param expression:表达式
    :return:计算结果
    """
    while True:
        if arg.__contains__('+-') or arg.__contains__("++") or arg.__contains__('-+') or arg.__contains__(
                "--"):
            arg = arg.replace('+-', '-')
            arg = arg.replace('++', '+')
            arg = arg.replace('-+', '-')
            arg = arg.replace('--', '+')
        else:
            break
    mch = re.search("([-]*\d+\.*\d*[-+]\d+\.*\d*)", arg)
    print("mch", mch)
    if mch==None:
        print("arg",arg)
        return arg

    before, nothing, after = re.split("(\d+\.*\d*[-+]\d+\.*\d*)",arg,1)
    print(before,'>>',nothing,'>>',after)
    print('before+-：', arg)

    content=re.split("[-+]", nothing)
    operator=re.split('([-+])',nothing,1)
    print('content+-：', content)
    print('operator+-：', operator)
    print("content",content)
    print("operator", operator)

    if before=='-':
        content[0]='-'+content[0]
        print("content", content)
        if operator[1]=='+':
            value=float(content[0])+float(content[1])
        else:
            value=float(content[0])-float(content[1])
        new_str = "%s%s" % (value, after)
    else:
        if operator[1]=='+':
            value=float(content[0])+float(content[1])
        else:
            value=float(content[0])-float(content[1])
        new_str = "%s%s%s" % (before, value, after)

    print("value",value)
    print("after+-：",new_str)
    arg = new_str
    return compute_add_sub(new_str)

compute_add_sub(inpp)