# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :动态设置类属性.py
# @Time      :2022/4/17 15:19
# @Author    :ming

class AABB:
    pass
# setattr , hasattr , getattr ,delattr

setattr(AABB,"name","hello")
print(AABB.name)

values = dict(AABB.__dict__.items())
for key,value in values.items():
    if key.startswith("__"):
        pass
    else:
        delattr(AABB,key)

print(AABB.__dict__)