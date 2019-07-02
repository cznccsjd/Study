#coding:utf-8
'''
正则表达式示例
正则表达式生成随机数据，并将产生的数据输出到屏幕
'''
from random import randint, choice
from string import ascii_lowercase
from sys import maxsize
from time import ctime

doms = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randint(5,10)):
    dtint = randint(0, maxint -1)