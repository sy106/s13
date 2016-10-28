#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Alex Li
from settings import ClassName
from settings import Path

def execute():
    # 字符串 "Foo"
    model = __import__(Path,fromlist=True)
    cls = getattr(model, ClassName)
    obj = cls()
    obj.f1()

if __name__ == '__main__':
    execute()
