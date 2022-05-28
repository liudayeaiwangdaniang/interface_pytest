# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :conftest.py
# @Time      :2022/4/29 22:33
# @Author    :ming

"""
项目根目录下（最顶层）的conftest.py  整个项目都可以用

1、放的都是fixture
2、fixtures可以对外共享
3、共享的范围：
    当前conftest.py所在目录下的（子孙目录），所有用例共享
4、conftest.py 是可以创建多个，在不同的包下，可以层级创建的
5、优先级，就近原则！！
    发现fixture：用例自己的模块 → 用例所在目录下的conftest.py → 目录的父级目录下的conftest.py
6、嵌套方式：
    6.1 什么时候嵌套?  一个fixture，想完全使用另一个fixture，并在人家的基础上新增一些代码
    6.2 怎么嵌套？
    @pytest.fixture
    def fix1()
        pass
    @pytest.fixture
    def fix2(fix1)
        # 新增的代码
        pass
    6.3    嵌套后的执行顺序
        fix1 的前置
        fix2 的前置
        fix2 的后置
        fix1 的后置

    6.4 可以任意fixture级别嵌套吗？
    fix1 >= fix2 级别
"""

import pytest
from jsonpath import jsonpath

from Common.handle_data import clear_EnvData_attrs, EnvData
from Common.handle_db import HandleDB
from Common.handle_phone import get_old_phone
from Common.handle_requests import send_requsets
from Common.my_logger import logger


@pytest.fixture(scope="class")
def init_envdata():
    logger.info("==========接口 开始测试==========")
    # 清理 EnvData里设置的属性
    clear_EnvData_attrs()
    #调用登录接口得到token和member_id
    yield
    logger.info("==========接口 结束测试==========")


@pytest.fixture(scope="session", autouse=True)
def db():
    dbs = HandleDB()
    yield dbs
    dbs.close()

@pytest.fixture(scope="class")
def use_login():
    # 清理 EnvData里设置的属性
    clear_EnvData_attrs()
    # 得到登录的用户名和密码
    user,passwd = get_old_phone()
    # 登录接口调用
    resp = send_requsets("POST", "member/login",
                  {"mobile_phone": user, "pwd": passwd})
    # 得到的id，token设置为类属性
    # cls.member_id = jsonpath(resp.json(),"$..id")[0]     # jsonpath处理 返回的数据
    # cls.token = jsonpath(resp.json(),"$..token")[0]
    setattr(EnvData,"member_id",str(jsonpath(resp.json(),"$..id")[0])) # 动态设置类属性
    setattr(EnvData,"token",jsonpath(resp.json(),"$..token")[0])
    yield
    if hasattr(EnvData,"money"):
        delattr(EnvData,"money")


@pytest.fixture(scope="class")
def admin_login():
    pass
    yield
    pass
