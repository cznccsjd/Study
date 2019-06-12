#coding:utf-8
"""
openpyxl模块，使用样式 working with style
url:http://openpyxl.readthedocs.io/en/latest/styles.html#
"""

####    简介
#  下面的代码使用默认的样式值
# from openpyxl.styles import PatternFill, Border,Side,Alignment,Protection,Font
# font = Font(name='Calibri',
#                     size=11,
#                     bold=False,
#                     italic=False,
#                     vertAlign=None,
#                     underline='none',
#                     strike=False,
#                     color='FF000000')
# fill = PatternFill(fill_type=None,
#                    start_color='FFFFFFF',
#                    end_color='FF000000')
# border = Border(left=Side(border_style=None,
#                           color='FF000000'),
#                 right=Side(border_style=None,
#                            color='FF000000'),
#                 top=Side(border_style=None,
#                          color='FF000000'),
#                 bottom=Side(border_style=None,
#                             color='FF000000'),
#                 diagonal=Side(border_style=None,
#                               color='FF000000'),
#                 diagonal_direction=0,
#                 outline=Side(border_sytle=None,
#                              color='FF0000000'),
#                 vertical=Side(border_style=None,
#                               color='FF000000'),
#                 horizontal=Side(border_style=None,
#                                 color='FF000000')
#                 )
# alignment = Alignment(horizontal='general',
#                       vertical='bottom',
#                       text_rotation=0,
#                       wrap_text=False,
#                       shrink_to_fit=False,
#                       indent=0)
# number_format = 'General'
# protection = Protection(locked=True,
#                         hidden=False)


##########  单元格样式和命名样式
###     单元格样式
# 单元格样式在对象之间共享，一旦分配了单元格样式就不能更改。这样就可以避免不必要的副作用，比如改变很多单元格的样式，而不是只改变一个。
# from openpyxl.styles import colors
# from openpyxl.styles import Font,Color
# from openpyxl import Workbook
#
# wb = Workbook()
# ws = wb.active
# a1 = ws['A1']
# d4 = ws['D4']
# ft = Font(color=colors.RED)
# a1.font = ft
# d4.font = ft
# a1.value = 'hello'
# d4.value = 123
# ws['B3'] = 666
#
# ###a1.font.italic = True   #is not allowed，style objects aor immutable(不可变) and cannot be changed
# # if you want to change the color of a Font, you need to reassign it ;如果想要改变字体颜色，需要重新分配;
# a1.font = Font(color=colors.RED, italic=True)   #the change only affects A1
# wb.save('style.xlsx')

### 复制样式
# from openpyxl.styles import Font
# from copy import copy
#
# ft1 = Font(name='Arial',size=14)
# ft2 = copy(ft1)
# ft2.name = "Tahoma"
# print(ft1.name)
# print(ft2.name)
# print(ft2.size)

### 基本字体颜色
# 颜色通常是RGB或aRGB六边形。colors模块包含一些方便的常量
# from openpyxl.styles import Font
# from openpyxl.styles.colors import RED
# from openpyxl.workbook import Workbook
#
# wb = Workbook()
# ws = wb.active
# font = Font(color=RED)
# font1 = Font(color="FFBB00")
# ws['A1'] = "RED"
# ws['B2'] = "FFBB00"
# ws['A1'].font = font
# ws['B2'].font = font1
# wb.save('color.xlsx')

# 还支持遗留的索引颜色以及主题和色调
# 实际上下面的代码报错，样式没有保存
# from openpyxl.styles.colors import Color
# from openpyxl.workbook import Workbook
# wb = Workbook()
# ws = wb.active
# c = Color(indexed=32)
# c1 = Color(theme=6,tint=0.5)
# ws['C3'] = "indexed=32"
# ws['D4'] = "theme=6,tint=0.5"
# ws['C3'].font = c
# ws['D4'].font = c1
# wb.save('color.xlsx')


#########   应用样式 Applying Styles
###样式直接应用于单元格
# from openpyxl.workbook import Workbook
# from openpyxl.styles import Font,Fill
# wb = Workbook()
# ws = wb.active
# c = ws['A1']
# c.font = Font(size=12)
# ws['A1'] = "Applying Styles"
# wb.save('applyStyle.xlsx')

# 样式还可以应用于列和行，但请注意，这只适用于在文件关闭后(在Excel中)创建的单元格。如果要将样式应用于整个行和列，则必须自己将样式应用于每个单元格。这是对文件格式的限制:
# 其实我也没搞清楚下面代码是干嘛的，运行结果是，A列不见了，B1没什么特殊的效果
# from openpyxl.workbook import Workbook
# from openpyxl.styles import Font,Fill
# wb = Workbook()
# ws = wb.active
# col = ws.column_dimensions['A']
# col.font = Font(bold=True)
# row = ws.row_dimensions[1]
# row.font = Font(underline="single")
# ws['A1'] = "one"
# ws['A2'] = "two"
# ws['B1'] = "three"
# wb.save('applyStyle.xlsx')


##############  合并单元格样式
# 有时，您希望将单元格的范围格式化为单个对象。Excel假装这是可能的通过合并单元格(删除除左上角单元格之外的所有单元格)，然后重新创建它们以应用伪样式。
####****下面的代码还是看不懂，暂时先不看到了，等到有需要的时候，再回过头来研究
# from openpyxl.styles import Border, Side, PatternFill, Font, GradientFill, Alignment
# from openpyxl import Workbook
#
# def style_range(ws, cell_range, border=Border(), fill=None, font=None, alignment=None):
#     """
#     Apply styles to a range of cells as if they were a single cell.
#     :param ws: Excel worksheet instance
#     :param cell_range: An excel range to style (e.g.A1:F20)
#     :param border: An openpyxl Border
#     :param fill: An openpyxl PatternFill or GradientFill
#     :param font: An openpyxl Font object
#     :param aligment:
#     :return:
#     """
#     top = Border(top=border.top)
#     left = Border(left=border.left)
#     right = Border(right=border.right)
#     bottom = Border(bottom=border.bottom)
#
#     first_cell = ws[cell_range.split(":")[0]]
#     if alignment:
#         ws.merge_cells(cell_range)
#         first_cell.alignment = alignment
#
#     rows = ws[cell_range]
#     if font:
#         first_cell.font = font
#
#     for cell in rows[0]:
#         cell.border = cell.border + top
#     for cell in rows[-1]:
#         cell.border = cell.border + bottom
#
#     for row in rows:
#         l = row[0]
#         r = row[-1]
#         l.border = l.border + left
#         r.border = r.border + right
#         if fill:
#             for c in row:
#                 c.fill = fill
#
# wb = Workbook()
# ws = wb.active
# my_cell = ws['B2']
# my_cell.value = "My Cell"
# thin = Side(border_style='thin', color="000000")
# double = Side(border_style="double", color="ff0000")
#
# border = Border(top=double,left=thin,right=thin,bottom=double)
# fill = PatternFill("solid", fgColor="DDDDDD")
# fill = GradientFill(stop=("000000","FFFFFF"))
# font = Font(b=True,color="FF0000")
# a1 = Alignment(horizontal="center",vertical="center")
#
# style_range(ws,'B2:F4',border=border,fill=fill,font=font,alignment=a1)
# wb.save("styled.xlsx")

###########编辑页面设置Edit Page Setup
##下面的代码不懂
# from openpyxl.workbook import Workbook
# wb = Workbook()
# ws = wb.active
# ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
# ws.page_setup.paperSize = ws.PAPERSIZE_TABLOID
# ws.page_setup.fitToHeight = 0
# ws.page_setup.fitToWidth = 1
# ws['A1'] = "Edit Page Setup"
# wb.save("editPageSetup.xlsx")

###Named Styles
# 与单元格样式相反，命名样式是可变的。当您想一次对许多不同的单元格应用格式时，它们是有意义的。NB。将命名样式分配给单元格后，对样式的额外更改不会影响单元格。
# 一旦命名样式注册到工作簿中，就可以通过名称来引用它。


########创建指定的样式
# from openpyxl.workbook import Workbook
# from openpyxl.styles import NamedStyle,Font,Border,Side
# highlight = NamedStyle(name='highlight')
# highlight.font = Font(bold=True,size=20)
# bd = Side(style='thick',color="000000")
# highlight.border = Border(left=bd,top=bd,right=bd,bottom=bd)
# # 一旦创建了命名样式，就可以在工作簿中注册使用:
# wb = Workbook()
# wb.add_named_style(highlight)
# ws = wb.active
# #但是在单元格中首次应用时，也会自动注册
# ws['A1'].style = highlight
# # （单元格样式）一旦注册使用名称后分配样式
# ws['D5'].style = 'highlight'
# wb.save('CreateStyle.xlsx')


############使用内置的样式
# 该规范还包括一些可以使用的内置样式。不幸的是，这些样式的名称存储在它们的本地化表单中。openpyxl将只识别英语名称，并且只完全按照这里所写。这些都是如下:
###数据格式
'''
'Comma'
'Comma[0]'
'Currency'
'Currency[0]
'Percent'
'''
###信息类
'''
'Calculation'
'Total'
'Note'
'Warning Text'
'Explanatory Text'
'''
###文本格式
'''
'Title'
'Headline 1'
'Headline 2'
'Headline 3'
'Headline 4'
'Hyperlink'
'Followed Hyperlink'
'Linked Cell'
'''
###比较
'''
'Input'
'Output'
'Check Cell'
'Good'
'Bad'
'Neutral'
'''
###高亮
'''
'Accent1'
'20 % - Accent1'
'40 % - Accent1'
'60 % - Accent1'
'Accent2'
'20 % - Accent2'
'40 % - Accent2'
'60 % - Accent2'
'Accent3'
'20 % - Accent3'
'40 % - Accent3'
'60 % - Accent3'
'Accent4'
'20 % - Accent4'
'40 % - Accent4'
'60 % - Accent4'
'Accent5'
'20 % - Accent5'
'40 % - Accent5'
'60 % - Accent5'
'Accent6'
'20 % - Accent6'
'40 % - Accent6'
'60 % - Accent6'
'Pandas'
'''
# For more information about the builtin styles please refer to the openpyxl.styles.builtins