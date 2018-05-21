__author__ = 'donghuiyan'
# -*- coding: UTF-8 -*-
'''
第四次作业：
1【函数默认参数】定义一个函数，输出姓名和年龄，年龄默认29岁，并调用这个函数，输出（1）姓名：lili 年龄：29    （2）姓名：hanmeimei 年龄：13
2【函数参数和返回值】定义一个函数，计算三角形的面积
3【可变对象做参数】定义一个函数，参数为list类型，功能在list末尾追加list1=[1,2,3,4]
4【关键字参数】定义一个函数，有多个参数，输出姓名，年龄，性别；调用时将参数顺序打乱（年龄，性别，姓名）分别赋值
5【不定长参数】定义一个不定长参数的函数，分别输出（1）10  （2）20 30 40
6【匿名函数】定义一个匿名函数，计算两个数的和，并输出
7【全局变量和局部变量】定义一个全局变量a=9,定义一个函数，在函数体内将a 修改成13 ，并返回输出
8【嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量】定义一个嵌套函数，在外函数中定义变量为10，内函数中修改变量，并分别输出内函数和外函数的变量
9【返回多个值】请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解
10【递归函数】定义一个函数，计算n!(n的阶乘)
'''
#1【函数默认参数】定义一个函数，输出姓名和年龄，年龄默认29岁，并调用这个函数，输出（1）姓名：lili 年龄：29    （2）姓名：hanmeimei 年龄：13
def printout(name,age=29):
    print('姓名：',name)
    print('年龄：',age)

printout('lili')
printout('hanmeimei',13)

#2【函数参数和返回值】定义一个函数，计算三角形的面积
def area(len,hight):
    return 1/2*len*hight

print('底长是2，高是3的三角形面积是:',area(2,3))

#3【可变对象做参数】定义一个函数，参数为list类型，功能在list末尾追加list1=[1,2,3,4]
def addList(list):
    list1=[1,2,3,4]
    return list+list1

list0=[100,200]
print(addList(list0))

#4【关键字参数】定义一个函数，有多个参数，输出姓名，年龄，性别；调用时将参数顺序打乱（年龄，性别，姓名）分别赋值
def out(name,age,sex):
    print('姓名:',name ,' ,年龄:',age,' ,性别:',sex)

out(age='10',sex='男',name="张三")

#5【不定长参数】定义一个不定长参数的函数，分别输出（1）10  （2）20 30 40
def randout(x,*y):
    print('输出不定长参数：')
    print(x)
    for i in  y:
        print (i)

randout(10)
randout(20,30,40)

#6【匿名函数】定义一个匿名函数，计算两个数的和，并输出
sum = lambda x,y:x+y
print('1+2的和是：',sum(1,2))

#7【全局变量和局部变量】定义一个全局变量a=9,定义一个函数，在函数体内将a 修改成13 ，并返回输出
a=10
def change(x):
    x=13
    return x
print(a,"函数修改之后变成",change(a))

#8【嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量】定义一个嵌套函数，在外函数中定义变量为10，内函数中修改变量，并分别输出内函数和外函数的变量
def outer():
    x=10
    def inner():
        nonlocal  x
        x=20
        print('内函数X值:',x)
    inner()
    print('外函数X值:',x)
outer()

#9【返回多个值】请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0的两个解
import math
def quadratic(a, b, c):
    if a==0:
        print('a不能为0')
        return
    elif (b*b-4*a*c) < 0:
        print('一元二次方程无解')
        return
    else:
        z=math.sqrt(b*b-4*a*c)
        x1=(-b+z)/(2*a)
        x2=(-b-z)/(2*a)
        return x1,x2
if quadratic(1,6,3) !=None:
    x1,x2=quadratic(1,6,3)
    print('两个根分别是：X1=',x1,',X2=',x2)

#10【递归函数】定义一个函数，计算n!(n的阶乘)
def nfact(n):
    S=0
    if n==1:
        S=1
    else:
        S=n*nfact(n-1)
    return S

print('5的阶乘：',nfact(5))






