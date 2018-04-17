#coding:utf-8
"""
陈直树的作业，2018/4/13
"""
import math,random

class Chen():
    #第一题：
    def one(self):
        '''
        1.	打印出下面这个字符串,注意Python和Im  learning不在同一行
            I'm learning
            Python.
            I'm "OK"!
        :return: 
        '''
        print "I\'m learning\nPython.\nI\'m",'\"OK\"!\n'

    def two(self):
        '''
        2.	var1 = 'Hello World!' var2 = "Runoob",获取var1的第一个字母,var2的第2-5个字母
        :return: 
        '''
        var1 = 'Hello World!'
        var2 = "Runoob"
        print "获取var1的第一个字母:%s" % var1[0]
        print "var2的第2-5个字母:%s" % var2[1:6]

    def three(self):
        '''
        3.	将字符串的第一个字符转换为大写的函数
        :return: 
        '''
        string = raw_input("请输入任意字符：")
        str = string.capitalize()
        print str

    def four(self):
        '''
        4.	字符串str=www.runoob.com,计算出o在字符串中出现次数,run在字符串中出现的次数
        :return:
        '''
        str = 'www.runoob.com'
        counto = str.count('o')
        countrun = str.count('run')
        print 'o在%s中出现了%d次' % (str, counto)
        print 'run在%s中出现了%d次' % (str, countrun)

    def five(self):
        '''
        5.	str1 = "Runoob example....wow!!!" str2 = "exam";判断str2是否在str中,如果在,返回所在位置的索引值第一位
        :return:
        '''
        str1 = "Runoob example....wow!!!"
        str2 = "exam"
        index = str1.find(str2)
        print '%s在%s第%d位' % (str2, str1, index)

    def six(self):
        '''
        6.	返回字符串长度函数是哪个
        :return:
        '''
        print '返回字符串长度函数是\tlen()'

    def seven(self):
        '''
        7.	str = "Runoob EXAMPLE....WOW!!!",把字符串中大写转换成小写
        :return:
        '''
        str = "Runoob EXAMPLE....WOW!!!"
        strLow = str.lower()
        print '%s中所有大写转换成小写后为：%s' % (str, strLow)

    def eight(self):
        '''
        8.	1 2 3 4 5 求这组数字的最大值和最小值,
        :return:
        '''
        num = range(1,6)
        print '%s中最大值是%d' % (num,max(num))
        print '%s中最小值是%d' % (num, min(num))

    def nine(self):
        '''
        9.	计算100的平方
        :return:
        '''
        num = 100
        print '%d的平方是%d' % (num, pow(num,2))

    def ten(self):
        '''
        10.	计算100的平方根
        平方根使用的math.sqrt()方法
        :return:
        '''
        num = 100
        print '%d的平方根是%d' % (num, math.sqrt(num))

    def eleven(self):
        '''
        11.	输出一个0-1之间的随机数
        使用random模块的randint方法
        :return:
        '''
        print '输出一个0-1之间的随机数:%s' % random.randint(0,1)
        random.

    def twelve(self):
        '''
        12.	输出一个1-100的随机数
        :return:
        '''
        print '输出一个0-100之间的随机数:%d' % random.randint(1,100)

if __name__ == '__main__':
    # Chen().one()
    # Chen().two()
    # Chen().three()
    # Chen().four()
    Chen().five()
    # Chen().six()
    # Chen().seven()
    # Chen().eight()
    # Chen().nine()
    # Chen().ten()
    # Chen().eleven()
    # Chen().twelve()