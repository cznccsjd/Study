__author__ = 'donghuiyan'
# -*- coding: UTF-8 -*-

#1.	打印出下面这个字符串,注意Python和Im  learning不在同一行
print("I'm learning \n Python")
print('''I'm  "OK"!''')

#2.	var1 = 'Hello World!' var2 = "Runoob",获取var1的第一个字母,var2的第2-5个字母
var1 = 'Hello World!'
var2 = "Runoob"
print (var1[0])
print(var2[1:5])

#3.	将字符串的第一个字符转换为大写的函数
s ='abcsdeee'
print(s.capitalize())

#4.	字符串str=www.runoob.com,计算出o在字符串中出现次数,run在字符串中出现的次数
str='www.runoob.com'
n=0
m=0
for i in str:
    if i=='o':
        n=n+1
print(n)

import re
print(len(re.findall(r'(?=run)', str)))
print(str.count('run'))

#5.	str1 = "Runoob example....wow!!!" str2 = "exam";判断str2是否在str中,如果在,返回所在位置的索引值第一位
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.find(str2))

#6.	返回字符串长度函数是哪个
print(len(str2))

#7.	str = "Runoob EXAMPLE....WOW!!!",把字符串中大写转换成小写
str = "Runoob EXAMPLE....WOW!!!"
print(str.lower())

#8.	1 2 3 4 5 求这组数字的最大值和最小值,
list =[1,2,3,4,5]
print(max(list))
print(min(list))
#9.	计算100的平方
import math
print(math.sqrt(100))
#10.	计算100的平方根
print(math.pow(100,2))
#11.	输出一个0-1之间的随机数
import random
print(random.randint(0,1))
#12.	输出一个1-100的随机数
print(random.randint(1,100))






