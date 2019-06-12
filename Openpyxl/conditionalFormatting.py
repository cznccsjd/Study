#coding:utf-8
"""
openpyxl模块学习，条件格式化部分Conditional Formatting
url:https://openpyxl.readthedocs.io/en/latest/formatting.html
"""
# Excel支持三种不同类型的条件格式:内置、标准和定制。
# 内置程序将特定的规则与预定义的样式结合在一起。
# 标准条件格式将特定规则与自定义格式相结合。
# 另外，还可以定义使用不同样式应用自定义格式的自定义公式。

######创建格式规则的基本语法是
# from openpyxl.formatting import Rule
# from openpyxl.styles import Font,PatternFill,Border
# from openpyxl.styles.differential import DifferentialStyle
# dxf = DifferentialStyle(font=Font(bold=True),fill=PatternFill(start_color='EE1111',end_color='EE1111'))
# rule = Rule(type='cellIs',dxf=dxf,formula=["10"])
# 由于一些规则的签名可能非常冗长，因此也有一些创建它们的便利工厂。

##########      内置格式 Builtin formats
# 内置的条件格式
'''
ColorScale
IconSet
DataBar
'''
# 内置格式包含一系列格式化设置，这些设置将类型和整数结合起来进行比较。
# 可能的类型是:' num '， ' percent '， ' max '， ' min '， ' formula '， ' percentile '。


###########     色级 ColerScale
# 可以有2到3个颜色的色标。2个色级可以从一种颜色到另一种渐变；三个颜色色标在2个基础上附加一种颜色；
# from openpyxl.formatting.rule import ColorScale,FormatObject
# from openpyxl.styles import Color
# first = FormatObject(type='min')
# last = FormatObject(type='max')
# #colors match the format objects:
# colors = [Color('AA0000'),Color('00AA00')]
# cs2 = ColorScale(cfvo=[first, last], color=colors)
# # a three color scale world extend the sequences
# mid = FormatObject(type='num', val=40)
# colors.insert(1, Color('00AA00'))
# cs3 = ColorScale(cfvo=[first, mid, last], color=colors)
# #create a rule with the color scale
# from openpyxl.formatting.rule import Rule
# rule = Rule(type='colorScale', colorScale=cs3)

#创建ColorScale规则有一个方便的功能
# from openpyxl.formatting.rule import ColorScaleRule
# rule = ColorScaleRule(start_type='percentile',start_value=10,start_color='FFAA0000',
#                       mid_type='percentile',mid_value=50,mid_color='FF0000AA',
#                       end_type='percentile',end_value=90,end_color='FF00AA00')


###########皮肤设置 IconSet
# 从下列图标中选择:' 3Arrows '， ' 3ArrowsGray '， ' 3flag '， ' 3TrafficLights1 '， ' 3TrafficLights2 '， ' 3Signs '， ' 3Symbols2 '， ' 4Arrows '， ' 4ArrowsGray '， ' 4Rating '， ' 4traffic light '， ' 5ArrowsGray '， ' 5Rating '， ' 525 '
# from openpyxl.formatting.rule import IconSet,FormatObject
# first = FormatObject(type='percent',val=0)
# second = FormatObject(type='percent',val=33)
# third = FormatObject(type='percent',val=67)
# iconset = IconSet(iconSet='3TrafficLights1',cfvo=[first,second,third],showValue=None,percent=None,reverse=None)
# #assign the icon set to a rule
# from openpyxl.formatting.rule import Rule
# rule = Rule(type='iconSet',iconSet=iconset)

# There is a convenience function for creating IconSet rules:
# from openpyxl.formatting.rule import IconSetRule
# rule = IconSetRule('5Arrows','percent',[10,20,30,40,50],showValue=None,percent=None,reverse=None)


##########  DataBar
# 剩下的看原文吧