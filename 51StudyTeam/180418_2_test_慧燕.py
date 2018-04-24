__author__ = 'donghuiyan'
# -*- coding: UTF-8 -*-
'''1.	list1 = ['Google', 'Runoob', 1997, 2000];
2.	list2 = [1, 2, 3, 4, 5, 6, 7 ];
3.	list3 = [1，2，3，3，4]
4.	输出list1的第一个值,list2的第2-5个值
5.	将list1的第三个值变成2001,并输出新的list
6.	删除list3的第三个元素并输出新的list
7.	求list1的长度
8.	List4, list5 = ['Google', 'Runoob', 'Taobao'], [456, 700, 200],求list4,list5的最大值
9.	List1+list2的新list6,输出新list6
10.	aTuple = (123, 'Google', 'Runoob', 'Taobao'),将这个元组装换成list
11.	list1的末尾插入’baidu’这个元素
12.	aList = [123, 'Google', 'Runoob', 'Taobao', 123];计算123在alist中出现的次数
13.	计算runoob在list中的索引位置
14.	删除list1中的第二个值
15.	将list1倒序输出
16.	将list2排序
17.	dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'},输出name所对应的kye
18.	# Fibonacci series: 斐波纳契数列 # 两个元素的总和确定了下一个数,写一个程序计算10以内菲波那切数列,并把结果输入在同一列
19.	写一个程序,让用户输入年龄,0-3岁告诉用户是婴儿,3-6岁幼儿,6-12岁少年,12-18青年,18岁以上是成人
20.	计算0-100的整数之和
21.	计算并输出0-10的质数,提示,质数:只有1和他本身两个因数,只能被1和他本身整除
'''




list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
list3 = [1,2,3,3,4]
print('list1的第一个值:',list1[0])
print('list2的第2-5个值:',list2[1:5])
list1[2]='2001'
print('新的list1:',list1)
list3.pop(2)
print('新的list3:',list3)
print('list1的长度:',len(list1))
list4= ['Google', 'Runoob', 'Taobao']
list5=[456, 700, 200]
print('list4的最大值',max(list4))
print('list5的最大值',max(list5))
list6=list1+list2
print('List1+list2的新list6,输出新list6',list6)
aTuple = (123, 'Google', 'Runoob', 'Taobao')
print('将aTuple这个元组装换成list',list(aTuple))
list1.append('baidu')
print('新的list1:',list1)
aList = [123, 'Google', 'Runoob', 'Taobao', 123];
print('计算123在alist中出现的次数',aList.count(123))
print('计算runoob在list中的索引位置',aList.index('Runoob'))
list1.pop(2)
print('新的list1:',list1)
list1.reverse()
print('将list1倒序输出',list1)
list2.sort()
print('将list2排序:',list2)
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print('输出name所对应的kye:',dict['Name'])
print('斐波纳契数列')
def feb():
    f1, f2 = 0, 1
    while f2 < 10:
        print(f2)
        f1, f2 = f2, f1+f2
feb()
#	写一个程序,让用户输入年龄,0-3岁告诉用户是婴儿,3-6岁幼儿,6-12岁少年,12-18青年,18岁以上是成人
def UserAge():
    age=int(input("请输入用户年龄: "))
    if age>=0 and age<3:
        print("用户是婴儿")
    elif age>=3 and age<6:
        print("用户是幼儿")
    elif age>=6 and age<12:
        print("用户是少年")
    elif age>=12 and age<18:
        print("用户是青年")
    elif age>=18:
        print("用户是成人")
UserAge()
#	计算0-100的整数之和
def sum100():
    s=0
    for i in range(101):
        s=s+i
    print("计算0-100的整数之和",s)
sum100()
#计算并输出0-10的质数,提示,质数:只有1和他本身两个因数,只能被1和他本身整除
def zhishu():
    list7 = []
    for n in range(1,10):
        if n == 1:
            continue
        elif n == 2:
            list7.append(2)
        else:
            if 0 not in [n%i for i in range(2,n)]:
             list7.append(n)
    print('0-10的质数',list7)
zhishu()