#coding:utf-8
"""
openpyxl模块学习    Additional Worksheet Porperties附加工作表属性
url：https://openpyxl.readthedocs.io/en/latest/worksheet_properties.
"""
# 这些是特定行为的高级属性，最常用的是“fitTopage”页面设置属性和定义工作表选项卡背景颜色的tabColor。

########    可用的属性工作表Available properties for worksheets
'''
'enableFormatConditionsCalculation'
'filterMode'
'published'
'syncHorizontal'
'syncRef'
'syncVertical'
'transitionEvaluation'
'transitionEntry'
'tabColor'
'''

######  页面设置属性的可用字段Available fields for page setup properties
'''
'autoPageBreadks'
'fitToPage'
'''

########    可用的字段轮廓Available fields for outlines
'''
'applyStyles'
'summaryBelow'
'summaryRight'
'showOutlineSymbols'
'''

# 默认情况下，大纲属性(outline)是初始化的，因此您可以直接修改它们的4个属性，而页面设置属性(page setup properties)没有。如果您想修改后者，您应该首先初始化一个openpyxpath .worksheet.properties。具有所需参数的PageSetupProperties对象。完成之后，如果需要，可以在以后由例程直接修改它们。
from openpyxl.workbook import Workbook
from openpyxl.worksheet.properties import  WorksheetProperties,PageSetupProperties
wb = Workbook()
ws = wb.active

wsprops = ws.sheet_properties
wsprops.tabColor = "1072BA"
wsprops.filterMode = False
wsprops.pageSetUpPr = PageSetupProperties(fitToPage=True,autoPageBreaks=False)
wsprops.outlinePr.summaryBelow = False
wsprops.outlinePr.applyStyles = True
wsprops.pageSetUpPr.autoPageBreaks = True