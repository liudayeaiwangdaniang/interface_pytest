# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_register.py
# @Time      :2022/4/11 23:16
# @Author    :ming
import json
import unittest
import os

import pytest

from Common.handle_path import datas_dir
from Common.handle_excle import HandleExcel
from Common.handle_requests import send_requsets
from Common.my_logger import logger
from Common.handle_db import HandleDB
from Common.handle_phone import get_new_phone
from Common.handle_data import replace_mark_with_data

he = HandleExcel(datas_dir+"\\api_cases.xlsx","注册")
cases = he.read_all_datas()
he.close_file()
# for item in cases:
#     print(item)

@pytest.fixture(scope="class")
def start_mark():
    logger.info("========注册模块用例  开始执行=======")
    yield
    logger.info("========注册模块用例  执行结束=======")

@pytest.mark.P0
@pytest.mark.usefixtures("start_mark")
class TestRegister:

    @pytest.mark.parametrize("case",cases)
    def test_register_ok(self,case,db):
        logger.info("执行用例{}：{}".format(case["id"],case["title"]))

    # 替换 - 动态
        # request_data里的 #phone# 替换成 new_phone
        # check_sql里的 #phone# 替换成 new_phone
        if case["request_data"].find("#phone#") != -1: # != -1 说明能找到下标
            new_phone = get_new_phone()
            case = replace_mark_with_data(case,"#phone#",new_phone)

    # 步骤 测试数据-发起请求
        response = send_requsets(case["method"],case["url"],case["request_data"])

    # 期望结果，从字符串转换为字典
        expected = eval(case["expected"])

    # 断言 -code == 0  msg == ok
        logger.info("用例的期望结果为：{}".format(case["expected"]))
        try:
            assert response.json()["code"] == expected["code"]
            assert response.json()["msg"] == expected["msg"]
            # 如果check_sql有值，说明要做数据库校验
            if case["check_sql"]:
                result = db.get_count(case["check_sql"])
                assert result != None
        except AssertionError:
            logger.exception("断言失败！")
            raise