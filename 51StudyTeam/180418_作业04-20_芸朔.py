#coding=UTF-8

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
list3 = [1,2,3,3,4]
list4 = ['Google', 'Runoob', 'Taobao']
list5 = [456, 700, 200]
aTuple = (123, 'Google', 'Runoob', 'Taobao')
aList = [123, 'Google', 'Runoob', 'Taobao', 123]
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#输出list1的第一个值,list2的第2-5个值
print(list1[0],list2[1:5])
#将list1的第三个值变成2001,并输出新的list
list1[2] = 2001
print(list1)
#删除list3的第三个元素并输出新的list
list3.pop(2)
print(list3)
#求list1的长度
print(len(list1))
#求list4,list5的最大值
print(max(list4))
print(max(list5))
#List1+list2的新list6,输出新list6
list6 = list1+list2
print(list6)
#将元组装换成list
list7 = list(aTuple)
print(list7)
#list1的末尾插入’baidu’这个元素
list1.append('baidu')
print(list1)
#计算123 在aList中出现的次数
print(aList.count(123))
#计算Runoob在list4中的索引位置
print(list4.index('Runoob'))
#删除list1中的第二个值
#list1.pop(1)
#将list1倒序输出
list1.reverse()
print(list1)
#将list2排序
list2.sort()
print(list2)
#dict中输出name所对应的kye
print(dict['Name'])
#Fibonacci series: 斐波纳契数列 # 两个元素的总和确定了下一个数,写一个程序计算10以内菲波那切数列,并把结果输入在同一列








