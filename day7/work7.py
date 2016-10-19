#!user/bin/env python
#-*-coding:utf-8 -*-
# Author: Sy106
# -*- coding:utf-8 -*-

# #####################  定义实现功能的类  #####################
# 性别、年龄、工作、人种、国籍、特长，存款。房、车等信息，
class Person:
    def __init__(self, na, gen,age,nationality, asset,specialty,house,car):
        self.name = na
        self.gender = gen
        self.age = age
        self.asset = asset
        self.nationality = nationality
        self.specialty = specialty
        self.house = house
        self.car = car

    def Fall_in_love(self,year,person):
        """注释：谈恋爱，消耗200金钱"""
        person.asset -= 20000 * year
        self.asset = self.asset + 20000 * year

    def practice(self,year):
        """注释：自我修炼，增长200金钱"""
        self.asset += 50000 * year
        if year ==1:
            self.house = ['二室一厅']
            self.car = ['奥拓']
        elif year == 3:
            self.house = ['三室一厅']
            self.car = ['别克']
        elif year == 5:
            self.house = ['四室两厅']
            self.car = ['宝马']
        else:
            self.house = ['别墅']
            self.car = ['特斯拉']



    def dumped(self):
        self.asset -= 200

    def speak(self,content):
        print(content)


    def detail(self):
        """注释：当前对象的详细情况"""

        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 存款:%s ; 国籍:%s ; 特长:%s ; 房子:%s ; 车子:%s"\
               % (self.name, self.gender, self.age, self.asset,self.nationality,self.specialty,self.house,self.car)
        print(temp)


# #####################  开始游戏  #####################

mei_nv = Person('苍井井', '女', 18,'china', 1000,'reading',[],[])  # 创建苍井井角色
diao_si = Person('东尼木木', '男', 20,'china', 1800,'singing',[],[])  # 创建屌丝角色
gao_fu_shuai = Person('尼普', '男', 29, 'china',25000,'swimming',[],[])  # 创建高富帅角色


def graduate(self,person):
    pass
def Many_years_later():
    pass


def run():
    pass
