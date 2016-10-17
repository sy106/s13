#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import pickle,os,datetime


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


# 学生：用户名、密码、性别、年龄、选课列表[]、上课记录{课程1：【di,a,】}
class student:
    def __init__(self,username,password,gender,age):
        self.username = username
        self.password = password
        self.gender = gender
        self.age = age
        self.class_list = []#选课记录
        self.class_record = {}#上课记录

    def evaluate(self,status,teacher):
        self.status = status
        if status == 'bad':
            teacher.asset -= 10
        elif status == 'good':
            teacher.asset += 10

#####################初始化#########################
Teacher1 = Teacher('running','alex',30)
Teacher2 = Teacher('reading','sy106',30)
Teacher3 = Teacher('singing','leo',29)

student1 = student('ann','12345','female',30)
student2 = student('tom','23456','male',32)
student3 = student('john','34567','male',33)

couse1 = course('Biology',10,'1:00')
couse2 = course('mathematics',20,'2:00')
couse3 = course('Chinese',15,'3:00')
couse4 = course('English',25,'4:00')
couse5 = course('geography',30,'5:00')

list_T = [Teacher1,Teacher2,Teacher3]
list_C = [couse1,couse2,couse3,couse4,couse5]
list_S = [student1,student2,student3]

pickle.dump(list_T,open('teacher', 'wb'))
pickle.dump(list_C,open('course','wb'))
pickle.dump(list_S,open('student','wb'))
ret_T = pickle.load(open('teacher','rb'))
ret_C = pickle.load(open('course','rb'))
ret_S = pickle.load(open('student','rb'))

"""
    用户登录
    :return:
"""
def login():
    print("the student names are:")
    for i in range(len(list_S)):
        print('%s:%s' % (i + 1, ret_S[i].username))
    student_name= input('please input your username:[q=quit]:>>>').strip()
    if student_name == 'q' or student_name == 'quit':
        quit()
    for j in range(len(list_S)):
        if student_name == ret_S[j].username:
            for times in range(3):
                student_password = input('please input your password:>>>').strip()
                if student_password == ret_S[j].password:
                    if open(student_name , 'rb'):
                        print("%s历史记录存在"%(student_name))
                        return ret_S[j]
                    else:
                        print("%s历史记录不存在" % (student_name))
                        pickle.dump(ret_S[j], open(student_name , 'wb'))
                        return ret_S[j]
                else:
                    print('the password is wrong!please retry!')

            else:
              print("you try too many times!Please relogin!")
              quit()
    else:
        print("the username is wrong!please relogin!")
        quit()

"""
    选课记录
    :return:
"""
def selected_course(student):
    student = pickle.load(open(student.username, 'rb'))
    if student.class_list==[]:
        print('%s has no class_list ' % student.username)
    else:
        print(student.class_list)
"""
    上课记录
    :return:
"""
def class_record(student):
    student = pickle.load(open(student.username, 'rb'))
    if student.class_record=={}:
        print('%s has no class_record ' % student.username)
    else:
        print(student.class_record)
"""
    选课
    :return:
"""
def select_courses(student):
    for k in range(len(list_C)):
        print('%s:%s' % (k + 1, ret_C[k].course_name))
    course_num = input('please input your choose:(only be number)>>>').strip()
    course_num = int(course_num)
    if course_num <= len(list_C):
        choose_course = ret_C[course_num-1].course_name
        student = pickle.load(open(student.username, 'rb'))
        student.class_list.append(choose_course)
        pickle.dump(student, open(student.username, 'wb'))
    else:
        print("your choose is not exit!")
        quit()
"""
    上课
    :return:
"""
def take_class(student):
    student = pickle.load(open(student.username, 'rb'))
    class_name = student.class_list
    value = 0
    for i in range(len(class_name)):
        for j in range(len(ret_C)):
            if class_name[i] == ret_C[j].course_name:
                value += ret_C[j].cost
    student.class_record[GetNowTime()] = [student.username,class_name]
    print('test2',student.class_record)
    if class_name == []:
        print ("please select the corse first!")
        main(student)
    choose_teacher(student,value)
    student.class_list = []
    pickle.dump(student, open(student.username, 'wb'))

"""
    选择老师
    :return:
"""
def choose_teacher(student,value):
    print("the teachers are:")
    for a in range(len(list_T)):
        print('%s:%s' % (a + 1, ret_T[a].name))
    user_option = input("please input the teacher:[q=quit]:>>>:").strip()
    if user_option == 'q' or user_option == 'quit':
        quit()
    for b in range(len(list_T)):
        if user_option == ret_T[b].name:
            ret_T[b].gain(value)
            evaluation(student,ret_T[b])
            return ret_T[b]
"""
    评价老师
    :return:
"""
def evaluation(student,teacher):
    user_option = input("please evaluated the teacher!bad or good?>>").strip()
    student.evaluate(user_option,teacher)
    pickle.dump(teacher, open(teacher.name, 'wb'))
    print("%s assert %s"%(teacher.name,teacher.asset))
"""
    退出系统
    :return:
"""
def quit():
    exit("Bye!")
"""
    选课系统
    :return:
"""
def main(student):
    while True:
        menu = """
                      1、已选课程；
                      2、上课记录；
                      3、选课；
                      4、上课
                                      """
        print(menu)
        menu_dic = {
            '1': selected_course,
            '2': class_record,
            '3': select_courses,
            '4': take_class,
        }
        user_option = input("please input your choose:[q=quit]:>>>:").strip()
        if user_option == 'q' or user_option == 'quit':
            quit()
        if user_option in menu_dic:
            menu_dic[user_option](student)
        else:
            print("选项不存在")
"""
    当前时间
    :return:当前时间
"""
def GetNowTime():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time
"""
    运行系统
    :return:
"""
def run():
    ret = login()
    if ret:
        main(ret)

run()