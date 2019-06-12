#coding:utf-8
"""
openpyxl模块学习,readonlymode
url:http://openpyxl.readthedocs.io/en/latest/optimized.html
"""

# 有时候，您需要打开或编写非常大的XLSX文件，而openpyxl中的通用例程无法处理这种负载。幸运的是，有两种模式允许您使用(接近)有限的内存消耗读写无限数量的数据。
# openpyxl.worksheet.read_only.ReadOnlyWorksheet
from openpyxl import load_workbook

wb = load_workbook(filename='./teacher.xlsx',read_only=True)
ws = wb['teacher_info']

for row in ws.rows:
    for cell in row:
        print(cell.value)