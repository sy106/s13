

name = input("input your name:")
age = int( input("input your age:") )
print(type(age),type(name)) #integer
job = input("input your job:")
salary = int( input("input your salay:"))

info = """
---------information of %s
Name: %s
Age : %d
Job : %s
Salary : %d
------------end-------------
""" % (name,name,age,job,salary)
print(info)

