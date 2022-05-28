# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_add.py
# @Time      :2022/4/23 14:41
# @Author    :ming

import os
import pytest

from Common.handle_path import datas_dir
from Common.handle_excle import HandleExcel
from Common.handle_requests import send_requsets
from Common.handle_data import EnvData,replace_case_by_regular
from Common.handle_extract_data_from_response import extract_data_from_response
from Common.my_logger import logger

# 读数据
he = HandleExcel(os.path.join(datas_dir,"api_cases.xlsx"), "加标")
cases = he.read_all_datas()
he.close_file()

@pytest.mark.usefixtures("init_envdata")
class TestAdd:

    @pytest.mark.parametrize("case",cases) # pytest 数据驱动
    def test_add(self,case,db):
        #替换case
        case = replace_case_by_regular(case)
        #如果前置sql - 得到结果后，再次替换
        #发送请求 - 考虑用例是否都需要token
        if hasattr(EnvData,"admin_token"):
            response = send_requsets(case["method"],case["url"],case["request_data"],token=EnvData.admin_token)
        else:
            response = send_requsets(case["method"],case["url"],case["request_data"])
        #如果有提取表达式，提取数据，设置为全局变量
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())
        #如果有期望结果，则断言

        #如果有check_sql,数据库校验
        if case["check_sql"]:
            result = db.get_one_data(case["check_sql"])
            logger.info("数据库查询结果为：")
            logger.info(result)

