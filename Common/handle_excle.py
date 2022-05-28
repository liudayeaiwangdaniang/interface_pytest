

"""
excel 类,你的需求是实现什么？
1、读取表头
2、读取数据 - 读取表头以外的所数据  返回值：列表，成员是每一行数据

初始化工作，，加载一个excle，打开一个表单
"""
import os
from openpyxl import load_workbook
import json

from Common.handle_path import datas_dir


class HandleExcel:

    def __init__(self,file_path,sheet_name ):
        self.wb = load_workbook(file_path)
        self.sh = self.wb[sheet_name]

    def __read_titles(self):
        titles = []
        for item in list(self.sh.rows)[0]:  # 获取excel第一行（表头）
            titles.append(item.value)
        return titles
    def read_all_datas(self):
        all_datas = []
        titles = self.__read_titles()
        for item in list(self.sh.rows)[1:]:  # 遍历数据行（第二行开始）
            values = []
            for val in item:  # 获取每一行的值
                values.append(val.value)  # 追加到列表
            res = dict(zip(titles, values))  # title和每一行数据，打包成字典
           # res["check"] = eval(res["check"])  # 将check的字符串，转换为字典对象

            all_datas.append(res)  # 追加到列表
        return all_datas


    def close_file(self):
        self.wb.close()

if __name__ == '__main__':
    he = HandleExcel(datas_dir+"\\api_cases.xlsx","充值")
    cases = he.read_all_datas()
    print(cases)
    he.close_file()
