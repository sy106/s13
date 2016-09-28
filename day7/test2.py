#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import re
from functools import reduce
from tkinter import *

'''处理特殊－号运算'''


def minus_operation(expresstion):
    minus_operators = re.split("-", expresstion)
    calc_list = re.findall("[0-9]", expresstion)
    if minus_operators[0] == "":
        calc_list[0] = '-%s' % calc_list[0]
    res = reduce(lambda x, y: float(x) - float(y), calc_list)
    print(">>>>>>>>>>>>>>减号[%s]运算结果:" % expresstion, res)
    return res


'''reduce()对sequence连续使用function, 如果不给出initial, 则第一次调用传递sequence的两个元素,
以后把前一次调用的结果和sequence的下一个元素传递给function'''

'''处理双运算符号'''


def del_duplicates(expresstion):
    expresstion = expresstion.replace("++", "+")
    expresstion = expresstion.replace("--", "-")
    expresstion = expresstion.replace("+-", "-")
    expresstion = expresstion.replace("--", "+")
    expresstion = expresstion.replace('- -', "+")

    return expresstion


'''＊／运算函数'''


def mutiply_dividend(expresstion):
    calc_list = re.split("[*/]", expresstion)  # 用＊ or /分割公式
    operators = re.findall("[*/]", expresstion)  # 找出所有＊和／号
    res = None
    for index, i in enumerate(calc_list):
        if res:
            if operators[index - 1] == '*':
                res *= float(i)
            elif operators[index - 1] == '/':
                res /= float(i)
        else:
            res = float(i)
    procession0 = "[%s]运算结果=" % expresstion, res
    final_result.insert(END, procession0)  # 插入窗体
    print(procession0)
    return res


'''处理运算符号顺序混乱情况'''


def special_features(plus_and_minus_operators, multiply_and_dividend):
    for index, i in enumerate(multiply_and_dividend):
        i = i.strip()
        if i.endswith("*") or i.endswith("/"):
            multiply_and_dividend[index] = multiply_and_dividend[index] + plus_and_minus_operators[index] + \
                                           multiply_and_dividend[index + 1]
            del multiply_and_dividend[index + 1]
            del plus_and_minus_operators[index]
    return plus_and_minus_operators, multiply_and_dividend


def minus_special(operator_list, calc_list):
    for index, i in enumerate(calc_list):
        if i == '':
            calc_list[index + 1] = i + calc_list[index + 1].strip()


'''运算除了（）的公式＋－＊／'''


def figure_up(expresstion):
    expresstion = expresstion.strip("()")  # 去掉外面括号
    expresstion = del_duplicates(expresstion)  # 去掉重复＋－号
    plus_and_minus_operators = re.findall("[+-]", expresstion)
    multiply_and_dividend = re.split("[+-]", expresstion)
    if len(multiply_and_dividend[0].strip()) == 0:
        multiply_and_dividend[1] = plus_and_minus_operators[0] + multiply_and_dividend[1]
        del multiply_and_dividend[0]
        del plus_and_minus_operators[0]

    plus_and_minus_operators, multiply_and_dividend = special_features(plus_and_minus_operators, multiply_and_dividend)
    for index, i in enumerate(multiply_and_dividend):
        if re.search("[*/]", i):
            sub_res = mutiply_dividend(i)
            multiply_and_dividend[index] = sub_res

    print(multiply_and_dividend, plus_and_minus_operators)  # 计算
    final_res = None
    for index, item in enumerate(multiply_and_dividend):
        if final_res:
            if plus_and_minus_operators[index - 1] == '+':
                final_res += float(item)
            elif plus_and_minus_operators[index - 1] == '-':
                final_res -= float(item)
        else:
            final_res = float(item)
    procession = '[%s]计算结果:' % expresstion, final_res
    final_result.insert(END, procession)  # 插入窗体
    print(procession)
    return final_res


"""主函数：运算逻辑：先计算拓号里的值,算出来后再算乘除,再算加减"""


def calculate():
    expresstion = expresstions.get()  # 获取输入框值
    flage = True
    calculate_res = None  # 初始化计算结果为None
    while flage:
        m = re.search("\([^()]*\)", expresstion)  # 先找最里层的（）
        # pattern = re.compile(r"\([^()]*\)")
        # m = pattern.match(expresstion)
        if m:
            sub_res = figure_up(m.group())  # 运算（）里的公式
            expresstion = expresstion.replace(m.group(), str(sub_res))  # 运算完毕把结果替换掉公式
        else:
            print('---------------括号已经计算完毕--------------')
            procession1 = "最终计算结果:", figure_up(expresstion)
            final_result.insert(END, procession1)  # 插入窗体
            print('\033[31m最终计算结果:', figure_up(expresstion))

            flage = False


if __name__ == "__main__":
    # res = calculate("1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )")
    window = Tk()  ###创建窗体
    window.title('计算器')  ###命名窗体
    frame1 = Frame(window)  ###框架1
    frame1.pack()  ###放置
    frame2 = Frame(window)  ###框架2
    frame2.pack()  ###放置
    lable = Label(frame1, text="请输入公式：")  ###文字标签
    lable.pack()
    expresstions = StringVar()  ###输入框属性，字符串
    entryname = Entry(frame1, textvariable=expresstions)  ###文本输入框
    bt_get_expresstions = Button(frame1, text="提交", command=calculate)  ###按钮挂件
    bt_get_expresstions.pack()
    entryname.pack()
    # lable.grid(row=1, column=1)  ###位置
    # entryname.grid(row=1, column=2)
    # bt_get_expresstions.grid(row=1, column=3)
    final_result = Text(frame2)  ###计算结果显示框
    final_result.tag_config("here", background="yellow", foreground="blue")
    final_result.pack()
    window.mainloop()  ###事件循环