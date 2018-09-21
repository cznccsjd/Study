#!/usr/bin/env python
#coding:utf-8
"""
学习time模块
"""
import time, datetime
# • time.time() 获取1970.1.1.0:0:0 到当前的时间
print 'time.time():',time.time()

# • time.localtime(): 获取本地时间
print 'time.localtime():',time.localtime()
# print type(time.localtime())

# • time.gmtime(): 获取格里尼治时间
print 'time.gmtime():',time.gmtime()

# • time. strftime(): 格式化时间格式
t = (2018,9,21,10,25,23,1,23,45)
t = time.mktime(t)          #time.mktime()接收struct_time对象作为参数，返回用秒数来表示时间的浮点数。
print 'time.strftime():',time.strftime("%b %d %Y %H:%M:%S",time.gmtime(t))


# • time.strptime()：字符串时间格式转化为时间
print 'time.strptime():',time.strptime("30 Sep 18", "%d %b %y")

# • time.mktime()： 将时间元组转换为1970/1/1 0:0:0 到目前的时间值
print 'time.mktime():',time.mktime((2018,9,21,10,41,12,2,344,12))

# • datetime.timedelta: 计算两个datetime对象的时间差
now = datetime.datetime.now()       #当前时间
# print 'now:',now
timeNow =  now - datetime.timedelta(days=5)      #选择5天前，这里可以输入任意时间（日、时、分、秒等等，详情查看资料）
print 'datetime.timedelta():',timeNow



"""
练习题

在web性能测试中，我们经常需要度量一个transaction（事务）需要花费多长时间，通常开发人员会使用log4j 打印出事物的开
始点和结束点。下面是个真实的log4j输出内容
DEBUG 180106 21:58:51,607 Receiver_1#receive a new request,
the session id is 2018010610020809
….
….
….
DEBUG 180106 21:59:38,908 Receiver_4#send response to client,
the session id is 2018010610020809
计算出处理这个事务所花费的时间
"""
import os,datetime,time

log = open('./log4j','r')
for line in log.readlines():
    print line



log.close()