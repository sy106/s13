#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
import pickle,sys,os



class Teacher:
    def __init__(self,favor,name,age):
        self.favor = favor
        self.name = name
        self.age = age
        self.asset = 0
obj1 = Teacher('running','alex',30)
obj2 = Teacher('reading','sy106',30)
obj3 = Teacher('singing','leo',29)
a1={1:obj1,2:obj2,3:obj3}



pickle.dump(a1,open('temp', 'wb'))
ret = pickle.load(open('temp','rb'))
print(ret)
