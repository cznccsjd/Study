#coding=UTF-8
import math
import random

#1
print("I'm learning\nPython.")
print("I'm \"OK\"!")
#2
var1 = 'HelloWorld!'
var2 = "Runoob"
print (var1[0:1])
print (var2[1:5])
#3
s= 'hi'
print (s.capitalize())
#4
str='www.runoob.com'
def a(s):
    b = 0
    for i in str:
        if i == 'o':
            b = b+1
    return b
print (a(str))
print(str.count('run'))
#5
str1 = "Runoob example....wow!!!"
str2 = "exam"
print(str1.find(str2))
#6
#len()
#7
str3 = "Runoob EXAMPLE....WOW!!!"
print (str3.lower())
#8
l = [1,2,3,4,5]
print(max(l),min(l))
#9
print(math.pow(100,2))
#10
print(math.sqrt(100))
#11
print(random.randint(0,1))
#12
print(random.randint(0,100))






