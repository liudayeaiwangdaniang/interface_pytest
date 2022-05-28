# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_recharge.py
# @Time      :2022/4/16 11:11
# @Author    :ming

"""
充值接口：
     所有用例的前置：登录
            拿到两份数据 id，token
    把前置的数据，传递给到测试用例
    充值接口的请求数：id
            请求头：token
问题1、充值前的用户余额：{'leave_amount': Decimal('0.00')}
 方式一  处理sql语句：把Decimal对应的字段值修改为字符串返回， CAST(字段名 AS CHAR)
 SELECT CAST(member.leave_amount AS CHAR) as leave_amount FROM member WHERE ID=34325120
 方式二 python Decimal 类型处理
"""
import unittest

import pytest
from jsonpath import jsonpath
import json
from ddt import ddt,data

from Common.handle_path import datas_dir
from Common.handle_excle import HandleExcel
from Common.handle_requests import send_requsets
from Common.my_logger import logger
from Common.handle_db import HandleDB
from Common.handle_data import replace_mark_with_data,EnvData,replace_case_by_regular,clear_EnvData_attrs

he = HandleExcel(datas_dir+"\\api_cases.xlsx","充值")
cases = he.read_all_datas()
he.close_file()

db = HandleDB()

@pytest.mark.usefixtures("use_login") #执行函数名叫use_login的前后置fixture
class TestRecharge:

    @pytest.mark.parametrize("case",cases)
    def test_recharge(self,case):
        #替换的数据
        if case["request_data"].find("#member_id#") != -1: # != -1 说明能找到下标
            # case = replace_mark_with_data(case,"#member_id#",str(EnvData.member_id))
            case = replace_case_by_regular(case)
        # 数据库 - 查询当前用户的余额 - 在充值之前
        if case["check_sql"]:
            user_money_before_recharge = db.get_one_data(case["check_sql"])["leave_amount"]
            logger.info("充值的用户余额：{}".format(user_money_before_recharge))
            # 期望的用户余额， 充值之前的余额 + 充值的钱
            recharge_money = json.loads(case["request_data"])["amount"]
            logger.info("充值的金额为：{}".format(recharge_money))
            expected_user_leave_amount = round(float(user_money_before_recharge) + recharge_money,2)
            logger.info("期望的充值之后的金额为：{}".format(expected_user_leave_amount))
            setattr(EnvData,"#money#",str(expected_user_leave_amount))
            # 更新期望的结果 - 将期望的用户余额更新到期望结果当中
            case = replace_mark_with_data(case,"#money#",str(expected_user_leave_amount))
            # case = replace_case_by_regular(case)
        print(case)
        # 发起请求 - 给用户充值
        response = send_requsets(case["method"],case["url"],case["request_data"],token=EnvData.token)
        # 将期望的结果转换成字典对象，再去对比
        print(case["expected"])
        expected = json.loads(case["expected"])
        # 断言
        try:
            assert response.json()["code"] == expected["code"]
            assert response.json()["msg"] == expected["msg"]
            if case["check_sql"]:
                assert response.json()["data"]["id"] == expected["data"]["id"]
                assert (response.json()["data"]["leave_amount"] == expected["data"]["leave_amount"])
                #数据库 - 查询当前用户的余额
                user_money_after_recharge = db.get_one_data(case["check_sql"])["leave_amount"]
                logger.info("充值后的用户余额：{}".format(user_money_after_recharge))
                assert "{:.2f}".format(expected["data"]["leave_amount"]) == "{:.2f}".format(float(user_money_after_recharge))
        except:
            logger.exception("断言失败！")
            raise