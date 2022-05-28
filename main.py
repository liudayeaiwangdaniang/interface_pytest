# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2022/4/12 23:20
# @Author    :ming


import pytest

if __name__ == '__main__':
    pytest.main(["-s","-v",
                "-m","P0",
                "--alluredir=Outputs/reports"
                "--reruns", "2", "--reruns-delay", "5"])


"""
                "--reruns", "2", "--reruns-delay", "5"
"-s",执行用例，携带详细信息，比如打印的print内容
"-v",表示查看详细的报告内容
运行多个标记的用例"-m P0 or P1"
allure报告 集成到jenkins
 --reruns 重试次数 --reruns-delay 次数之间的延时设置（单位：秒）
"""