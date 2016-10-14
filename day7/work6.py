#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import pickle,sys,os

CURRENT_USER_INFO = {'is_authenticated': False, 'current_user': None}
student_g=''
# 创建老师：姓名、性别、年龄、资产
class Teacher:
    def __init__(self,favor,name,age):
        self.favor = favor
        self.name = name
        self.age = age
        self.asset = 0

    def Teaching_accident(self):
        self.asset = self.asset - 1

    def gain(self,value):
        self.asset += value

# 创建课程：课程名称、上课时间、课时费
class course:
    def __init__(self,course_name,cost,time):
        self.course_name = course_name
        self.cost = cost
        self.time = time

    def Teaching(self,Teacher):
         Teacher.asset += course.cost

# 学生：用户名、密码、性别、年龄、选课列表[]、上课记录{课程1：【di,a,】}
class student:
    def __init__(self,username,password,class_list,class_record):
        self.username = username
        self.password = password
        self.class_list = class_list
        self.class_record = class_record

    def evaluate(self,status,Teacher):
        self.status = status
        if status == 'bad':
            Teacher.asset -= 10

#####################初始化#########################
Teacher1 = Teacher('running','alex',30)
Teacher2 = Teacher('reading','sy106',30)
Teacher3 = Teacher('singing','leo',29)

student1 = student('ann','12345')
student2 = student('tom','23456')
student3 = student('john','34567')

couse1 = course('Biology',20,'9:00')
couse2 = course('mathematics',20,'10:00')
couse3 = course('Chinese',20,'11:00')
couse4 = course('English',20,'14:00')
couse5 = course('geography',20,'15:00')

list_T = [Teacher1,Teacher2,Teacher3]
list_C = [couse1,couse2,couse3,couse4,couse5]
list_S = [student1,student2,student3]

pickle.dump(list_T,open('teacher', 'wb'))
pickle.dump(list_C,open('course','wb'))
pickle.dump(list_S,open('student','wb'))
ret_T = pickle.load(open('teacher','rb'))
ret_C = pickle.load(open('course','rb'))
ret_S = pickle.load(open('student','rb'))


def login():
    print("the student names are:")
    for i in range(len(list_S)):
        print('%s:%s' % (i + 1, ret_S[i].username))
    student_name= input('please input your username:[must be the above number]>>>').strip()
    for j in range(len(list_S)):
        if student_name == ret_S[j].username:
            student_password = input('please input your password:>>>').strip()
            if student_password == ret_S[j].password:
                choose_course()
            else:
                print('the password is wrong!')
                break
        else:
            print("the username is wrong!please retry!")
            exit('Bye!')

def choose_course():
    for k in range(len(list_C)):
        print('%s:%s' % (k + 1, ret_C[k].course_name))
    course_num = input('please input your choose:(only be number)>>>').strip()
    course_num = int(course_num)
    if course_num <= len(list_C):
        choose_course = ret_C[course_num-1].course_name

    else:
        print("your choose is not exit!")
        exit("Bye!")



login()

# def run():
#     ret = login()
#     if ret:
#         main()