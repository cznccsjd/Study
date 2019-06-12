#coding:utf-8
"""
openpyxl模块学习，工作表表格Worksheet Tables
url：https://openpyxl.readthedocs.io/en/latest/worksheet_tables.html
"""
# 工作表是对单元格的引用。这使得某些操作(例如对表中的单元格进行样式化)更容易。

# 新建一个table
from openpyxl import Workbook
from openpyxl.worksheet.table import Table,TableStyleInfo

wb = Workbook()
ws = wb.active

data = [
    ['Apples', 10000, 5000, 8000, 6000],
    ['Pears',   2000, 3000, 4000, 5000],
    ['Bananas', 6000, 6000, 6500, 6000],
    ['Oranges',  500,  300,  200,  700],
]

#add column headings.NB.these must be strings
ws.append(["fruite","2011","2012","2013","2014"])
for row in data:
    ws.append(row)

tab = Table(displayName="Table1",ref="A1:E5")

#add a default sytle with striped rows and banded columns
style = TableStyleInfo(name="TableStyleMedium9",showFirstColumn=False,
                       showLastColumn=False,showRowStripes=True,showColumnStripes=True)
tab.tableStyleInfo = style
ws.add_table(tab)
wb.save("table.xlsx")
# 默认情况下，表是用第一行的标题和所有列的过滤器创建的。
# 使用TableStyleInfo对象管理样式。这允许您对行或列进行条纹，并应用不同的配色方案。

###重要提示
# 表名必须在工作簿中唯一，表标题和筛选范围必须始终包含字符串。如果不是这样，Excel可能认为文件无效并删除表