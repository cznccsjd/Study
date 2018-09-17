#coding:utf-8
"""
学习File模块
读取的example.txt文件
open()和file()都可以，但是推荐使用open()，因为Python3里面已经没有file函数了

还需要解决file.write()和file.writelines()写入文件时，乱码的问题！！！！！！！
"""
myfile = open('./example.txt','r')
myfilew = open('./exampleWrite.txt','w+')
list = ['one','two','three','four']
# 一次性读取全部内容
print '一次性读取全部内容：\n',myfile.read()
# 执行一次，读取一行
print '执行一次，读取一行：\n',myfile.readline()
# 一次性读取文件全部内容，并放到一个列表里面，每行是一个列表元素
print 'readlines()读取全部内容，放到列表里面：\n',myfile.readlines()


# 写内容到文件，不换行
myfilew.write(u"this is my note")
print '\nwrite()方法写入的内容：\n', myfilew.read()
# 把一个列表里的所有元素写到文件中，不换行
myfilew.truncate()
myfilew.writelines(list)
print '\nwritelines()写入的内容：\n',myfilew.read()


# 关闭文件
myfile.close()
myfilew.close()