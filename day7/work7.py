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

    def Fall_in_love(self,person,year):
        """注释：谈恋爱，消耗200金钱"""
        person.asset -= 20000 * year
        self.asset = self.asset + 20000 * year

    def practice(self,year):
        """注释：自我修炼，"""
        self.age += year
        if self == diao_si:
            self.asset += 70000 * year
            if year ==1:
                self.house = ['租房']
                self.car = ['奥拓']
            elif year == 5:
                self.house = ['二室一厅']
                self.car = ['别克']
            elif year == 10:
                self.house = ['四室两厅']
                self.car = ['宝马']
            else:
                self.house = ['别墅','三室一厅']
                self.car = ['特斯拉','宝马']
        elif self == mei_nv:
            self.asset += 20000 * year
        elif self == gao_fu_shuai:
            self.asset += 100000 * year


    def dumped(self,person):
        person.asset -= 2000


    def speak(self,content):
        print('%s:%s'%(self.name,content))

    def graduate(self, Person):
        if self == mei_nv:
            Person.speak("%s:我喜欢上了高富帅%s!木木，我们分手吧！"%(mei_nv.name,gao_fu_shuai.name))
        elif self == diao_si:
            Person.dumped(diao_si)
            Person.speak("%s:苍天啊，可不可以不要这样对我！我一定要努力赚钱,追回%s！"%(diao_si.name,mei_nv.name))


    def Many_years_later(self):
        pass

    def detail(self):
        """注释：当前对象的详细情况"""

        temp = "姓名:%s ; 性别:%s ; 年龄:%s ; 存款:%s ; 国籍:%s ; 特长:%s ; 房子:%s ; 车子:%s"\
               % (self.name, self.gender, self.age, self.asset,self.nationality,self.specialty,self.house,self.car)
        print(temp)


# #####################  开始游戏  #####################

mei_nv = Person('Liz', '女', 18,'china', 1000,'reading',[],[])  # 创建苍井井角色
diao_si = Person('John', '男', 18,'china', 1800,'singing',[],[])  # 创建屌丝角色
gao_fu_shuai = Person('Peter', '男', 29, 'china',2500000,'swimming',['大别墅'],['奔驰'])  # 创建高富帅角色


def run():
    Person.detail(mei_nv)
    Person.detail(diao_si)
    Person.detail(gao_fu_shuai)
    print("场景1》》》》》：屌丝和美女刚毕业")
    Person.graduate(mei_nv, diao_si)
    Person.graduate(diao_si,mei_nv)
    Person.detail(mei_nv)
    Person.detail(diao_si)
    Person.detail(gao_fu_shuai)
    print("场景2》》》》》：若干年后。。。")
    Person.practice(mei_nv,16)
    Person.practice(diao_si, 16)
    Person.practice(gao_fu_shuai, 16)
    Person.Fall_in_love(mei_nv,gao_fu_shuai,10)
    Person.dumped(mei_nv,gao_fu_shuai)#恋爱10年后，美女被高富帅甩掉
    print('独白：：恋爱10年后，美女被高富帅甩掉,又过了6年，美女再次遇到当年的屌丝，发现屌丝变为高富帅，提出复合！')
    print('%s:亲爱的%s,经过16年的打拼，你终于变成高富帅，我们可以重新开始吗？'%(mei_nv.name,diao_si.name))
    Person.speak(diao_si,'抱歉，当年是你贪图富贵抛弃我，你曾经是我努力的动力。经过16年的努力，我终于成功了。但是好马不吃回头草，我已经有新的女朋友，没必要再跟你一起!')

    Person.detail(mei_nv)
    Person.detail(diao_si)
    Person.detail(gao_fu_shuai)



run()
