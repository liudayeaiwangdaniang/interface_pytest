# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_user_business.py
# @Time      :2022/4/22 21:32
# @Author    :ming

"""
从响应结果当中提取需要的值

注册 用户名和密码
登录 同一个用户名和密码
充值 上一个接口返回值里的 token，member_id
提现 登录接口返回值里的 token，member_id
加标
"""
import unittest

from ddt import ddt,data

from Common.handle_data import EnvData, replace_case_by_regular
from Common.handle_excle import HandleExcel
from Common.handle_path import datas_dir
from Common.handle_phone import get_new_phone
from Common.handle_requests import send_requsets
from Common.handle_extract_data_from_response import extract_data_from_response

he = HandleExcel(datas_dir+"\\api_cases.xlsx","业务流")
cases = he.read_all_datas()
he.close_file()

@ddt
class TestUserBusiness(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 生成一个新的手机号码，设置为全局变量

        new_phone = get_new_phone()
        setattr(EnvData,"phone",new_phone)
    @data(*cases)
    def test_user_business(self,case):

        # 替换的数据
        replace_case_by_regular(case)

        # 发起请求,判断是否需要传递token
        if hasattr(EnvData,"token"):
            response = send_requsets(case["method"], case["url"], case["request_data"], token=EnvData.token)
        else:
            response = send_requsets(case["method"], case["url"], case["request_data"])
        # 如果有要提取数据的，提取数据，并设置为全局变量
        if case["extract_data"]:
            extract_data_from_response(case["extract_data"],response.json())