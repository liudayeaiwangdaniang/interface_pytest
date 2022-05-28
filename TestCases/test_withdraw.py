# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_withdraw.py
# @Time      :2022/4/22 21:09
# @Author    :ming

import pytest
from jsonpath import jsonpath


from Common.handle_path import datas_dir
from Common.handle_excle import HandleExcel
from Common.handle_requests import send_requsets
from Common.my_logger import logger
from Common.handle_db import HandleDB
from Common.handle_phone import get_old_phone
from Common.handle_data import replace_mark_with_data,EnvData,replace_case_by_regular,clear_EnvData_attrs

he = HandleExcel(datas_dir+"\\api_cases.xlsx","充值")
cases = he.read_all_datas()
he.close_file()

db = HandleDB()

@pytest.mark.usefixtures("use_login")
class TestWithdraw:
 pass
