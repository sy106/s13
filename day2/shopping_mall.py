#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

salary=input('please input your salary:').strip()
if salary.isdigit():
    salary=int(salary)
    print ('your salary is:%d'%salary)
else:
    exit('invalid data type..')

welcom_msg='''wlecome to sy106 shopping mall!'''.center(60,'-')

print(welcom_msg)