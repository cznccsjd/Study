#coding:utf-8


# x = 10
# def foo():
#     y = 5
#     bar = lambda z: x+z
#     print bar(y)
#     y = 8
#     print bar(y)
#
# foo()

#
# x = 'abc'
# def foo():
#     # global x
#     y = '100'
#     # x = 'ef'
#     print x + y
#
# foo()
# print x


#
# import  time
# def simpleGen():
#     yield 1
#     yield '2 --> punch!'
#
# MyG = simpleGen()
# print MyG.next()
# time.sleep(1)
# print MyG.next()
# time.sleep(1)
# print MyG.next()
#
#
# """
# 下面的例子，创建一个带序列并从那个序列中返回一个随机元素的随机迭代器
# """
# from random import randint
# def randGen(aList):
#     while len(aList):
#         yield aList.pop(randint(0, len(aList)))
#
# for item in randGen(['rock','paper','scissors']):
#     print item


# def odd():
#     print 'step1'
#     yield(1)
#     print 'step2'
#     yield(2)
#
#
# o = odd()
# next(o)
# next(o)


#
# def simpleGen():
#     yield 1
#     yield '2 --> punch!'
#
# myG = simpleGen()
# print myG
# print myG.next()


#
# # 九九乘法表
#
# for first_num in range(1,10):
#     for second_num in range(1, first_num+1):
#         print second_num, "*", first_num, "=", first_num*second_num, "",
#     print "\n"


#
# def test(name, *nkwargs):
#     print name
#     for args in nkwargs:
#         print "others:", args
#
# test('hello','yiou','sdf')

# 霍格沃兹作业：
# 1.把1000-2500之间，既能被7整除，也能被5整除的数取出来，放到一个列表输出
# list = []
# for num in range(1000,2501):
#     if num % 7 == 0:
#         if num % 5 == 0:
#             list.append(num)
# print list


# 2.打印出0-20之间的数字，如果此数字能被3整除，输出英文”three”, 如果能被5整除,输出”five”，如果既能被3整除也能被5整除，输出”threes+fives”, 要求用到continue.
# for num in range(0,21):
#     if num % 3 == 0:
#         print "three"
#         continue
#     elif num % 5 == 0:
#         print 'five'
#         continue
#     elif num % 3 == 0 and num % 5 == 0:
#         print "three+five"
#     else:
#         pass



while  num in range(0,21):
    print 'yes'