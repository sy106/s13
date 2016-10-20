#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106

# import  datetime
#
# current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(current_time)

class Foo:
    """ 描述类信息，这是用于看片的神奇 """

    def func(self):
        pass

print (Foo.__doc__)