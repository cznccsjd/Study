#coding:utf-8
"""
只写模式
"""
# from openpyxl import Workbook
# wb = Workbook(write_only=True)
# ws = wb.create_sheet()
#
# #now we'll fill it with 100 rows x 200 columns
# for irow in range(100):
#     ws.append(['%d' % i for i in range(200)])
# #savs the file
# wb.save('./new_big_file.xlsx')

#####  单元格想带上样式或者注释，使用openpyxl.worksheet.write_only.WriteOnlyCell()
# from openpyxl import Workbook
# wb = Workbook(write_only = True)
# ws = wb.create_sheet()
# from openpyxl.worksheet.write_only import WriteOnlyCell
# from openpyxl.comments import Comment
# from openpyxl.styles import Font
# cell = WriteOnlyCell(ws, value='hello,world')
# cell.font = Font(name='Courier', size=36)
# cell.comment = Comment(text="A comment",author="Author's Name")
# ws.append([cell,3.14,None])
# wb.save('./write_only_file.xlsx')
# 上面的代码中，创建了一个只读的单一sheet页，并且插入了三个单元格：一个自定义了字体和注释的单元格，一个
# 单精度数字，和一个空单元格（直接丢弃）
'''
需要注意的是：
1、与普通工作簿不同，新创建的只写工作簿不包含任何工作表;必须使用create_sheet()方法专门创建工作表。
2、在只写的工作簿中，只能使用append()添加行。使用cell()或iter_rows()在任意位置写入(或读取)单元格是不可能的。
3、它可以导出无限数量的数据(甚至超过Excel实际能够处理的数据)，同时将内存使用量控制在10Mb以下。
4、只写工作簿只能保存一次。在此之后，每次试图保存工作簿或将()追加到现有工作表的尝试都会引发openpyxpath .utils.exceptions. exception。WorkbookAlreadySaved例外。
5、在实际单元格数据之前出现在文件中的所有内容都必须在添加单元格之前创建，因为在添加单元格之前必须将其写入文件。例如，在添加单元格之前应该设置freeze_panes。
'''
