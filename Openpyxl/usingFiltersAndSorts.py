#coding:utf-8
"""
openpyxl模块学习，使用过滤器和排序Using filters and sorts
url:https://openpyxl.readthedocs.io/en/latest/filters.html
"""
# 过滤器和排序只能由openpyxl配置，但需要在Excel等应用程序中应用。
# 这是因为它们实际上重新排列或格式化范围内的单元格或行。

# 要添加过滤器，您需要定义一个范围，然后添加列和排序条件:
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

data = [
    ["Fruit","Quantity"],
    ["Kiwi",3],
    ["Grape",15],
    ["Apple",3],
    ["Peach", 3],
    ["Pomegranate", 3],
    ["Pear", 3],
    ["Tangerine", 3],
    ["Blueberry", 3],
    ["Mango", 3],
    ["Watermelon", 3],
    ["Blackberry", 3],
    ["Orange", 3],
    ["Raspberry", 3],
    ["Banana", 3]
]

for r in data:
    ws.append(r)

ws.auto_filter.ref = "A1:B15"
ws.auto_filter.add_filter_column(0,["Kiwi","Apple","Mango"])
ws.auto_filter.add_sort_condition("B2:B15")

wb.save("filtered.xlsx")
# This will add the relevant instructions to the file but will neither actually filter nor sort.
# 这将向文件添加相关的指令，但实际上既不会过滤也不会排序。