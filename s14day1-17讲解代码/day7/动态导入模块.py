#
# lib = __import__("lib.aa") #lib
# lib.aa


import importlib
aa = importlib.import_module('lib.aa') #，官方建议用这个
obj = aa.C()

assert type(obj.name) is int
if type(obj.name) is not int :
    exit("must be in")
print(obj.name /2)
# obj = mod.aa.C()
# print(obj.name)

