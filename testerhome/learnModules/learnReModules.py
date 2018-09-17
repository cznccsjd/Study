#coding=utf-8
"""
学习RE模块
"""
import re

# 将正则表达式语法转化成正则表达式对象        正则表达式对象是啥？
pattern = re.compile(r'if')


# 在整个字符串中查找匹配字符串的位置，没有返回None，有返回MatchObject实例
# match1 = re.search(pattern,'yes')    #没有匹配，返回Money
match1 = pattern.search('yes')      #另外一种写法
match2 = re.search(pattern,'for while switch,if... else...')   #有匹配，返回MatchObject实例

# 在字符串开始位置尝试匹配正则表达式
match3 = re.match(pattern, 'for while switch,if... else...')     #开始位置匹配不到
match4 = re.match(pattern, 'if...else...and others.')     #开始位置可以匹配到

# findall显示字符串中模式的所有匹配项
# match5 = re.findall(pattern, "if else ifelse elif yes no")
# 另外一种写法
match5 = pattern.findall("if else ifelse elif yes no")


print '正则表达式语法转换成正则表达式对象后为：',pattern
print '没有匹配，返回：',match1
print '有匹配，返回MatchObject实例：',match2
print '在开始的位置匹配不到：',match3
print '在开始的位置可以匹配到：',match4
print 'findall的结果：',match5