#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

import re

def exec_bracket(expression):
    """ 递归处理括号，并计算
    :param expression: 表达式
    :return:最终计算结果
    """
# 如果表达式中已经没有括号，则直接调用负责计算的函数，将表达式结果返回，如：2*1-82+444
    if  re.findall("[()]",expression)==[]:
        final = compute(expression)
        return final
    else:
        content= re.split("\(([^()]*)\)",expression,1)

        # 分割表达式，即：
        # 将['1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
        # 分割更三部分：['1-2*((60-30+(    (-40.0/5)      *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
        before, nothing, after = re.split("\(([^()]*)\)",expression,1)
        print('before：', expression)
        content = content[1]

        # 计算，提取的表示 (-40.0/5)，并活的结果，即：-40.0/5=-8.0
        ret = compute(content)
        print('括号内的计算结果：%s=%s' % (content, ret))
        # 将执行结果拼接，['1-2*((60-30+(      -8.0     *(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))']
        expression = "%s%s%s" % (before, ret, after)
        print('after：', expression)
        print("=" * 10, '上一次计算结束', "=" * 10)
        # 如此周而复始的操作，直到表达式中不再含有括号
        return exec_bracket(expression)

def compute(expression):
    """ 操作加减乘除
    :param expression:表达式
    :return:计算结果
    """
    # 先处理表达式中的乘除
    value=compute_mul_div(expression)
    # 后处理表达式中的加减
    result=compute_add_sub(value)
    return result


def compute_mul_div(arg):
    """ 操作乘除
        :param expression:表达式
        :return:计算结果"""
    while True:
        if arg.__contains__('+-') or arg.__contains__("++") or arg.__contains__('-+') or arg.__contains__(
                "--"):
            arg = arg.replace('+-', '-')
            arg = arg.replace('++', '+')
            arg = arg.replace('-+', '-')
            arg = arg.replace('--', '+')
        else:
            break
    mch = re.search("([-]*\d+\.*\d*[*/][-]*\d+\.*\d*)", arg)
    if mch==None:
        return arg

    before, nothing, after = re.split("([-]*\d+\.*\d*[*/][-]*\d+\.*\d*)", arg, 1)#用* or /分割公式,得到中间的计算式
    # print(before, '>>', nothing, '>>', after)
    # print('before*/：', arg)

    content = re.split("[*/]", nothing)#得到表达式第一个*或者/的数字
    operator = re.split('([*/])', nothing)#得到表达式第一个*或者/的符号
    # print('content[*/]：', content)
    # print('operator[*/]：', operator)

    if operator[1] == '*':
        value = float(content[0]) * float(content[1])
    else:
        value = float(content[0])/float(content[1])
    value=float(value)
    # print('value',value)
    if value<0:
        new_str = "%s%.2f%s" % (before, value, after)
    else:
        new_str = "%s+%.2f%s" % (before, value, after)
    # print('new_str*/',new_str)
    arg = new_str
    return compute_mul_div(arg)


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
    # print('mch+-',mch)
    if mch==None:
        return arg

    before, nothing, after = re.split("([-]*\d+\.*\d*[-+]\d+\.*\d*)",arg,1)
    # print(before, '>>', nothing, '>>', after)
    # print('nothing[0]>>',nothing[0])
    if nothing[0]=='-':
        nothing=re.sub('-', '#', nothing,1)
    content=re.split("[-+]", nothing)
    operator=re.split('([-+])',nothing,1)
    # print('content[-+]：', content)
    # print('operator[-+]：', operator)
    # print(print('nothing[0]>>after',nothing[0]))
    if nothing[0]=='#':
        content[0] = re.sub('#', '-', content[0], 1)
        # print("content", content)
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
    # print('new_str[-+]：', new_str)
    arg = new_str
    return compute_add_sub(arg)

# 使用 __name__ 的目的：
#   只有执行 python index.py 时，以下代码才执行
#   如果其他人导入该模块，以下代码不执行
if __name__ == "__main__":
    # print '*'*20,"请计算表达式：", "1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )" ,'*'*20
    # inpp = '1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) ) '
    inpp = "1-(2.0*-30)/-12*(-20+200.5*-3/-200.78*-300.7-100)"
    # inpp = "1-5*980.0"
    inpp = re.sub('\s*', '', inpp)
    # 表达式保存在列表中
    result = exec_bracket(inpp)
    print("the result is:>>>",result)