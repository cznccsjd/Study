#coding:utf-8
"""
11.10 生成器部分学习
"""
import time

"""
当到达一个真正的返回或者函数结束没有更多的值返回（当调用next()），一个StopIteration异常就会抛出。
"""
# def simpleGen():
#     yield 1
#     yield '2 --> punch!'
# try:
#     myG = simpleGen()
#     print 'myG = simpleGen()表达式中myG的值是：',myG
#     print myG.next()
#     time.sleep(1)
#     print myG.next()
#     time.sleep(1)
#     print myG.next()
# except StopIteration:
#     print '报错了：StopIteration'


"""
由于Python的for循环有next()调用和对StopIteration的处理，使用一个for循环而不是手动迭代穿过一个
生成器（或者那种事务的迭代器）总是要简洁漂亮的多
"""
# time.sleep(1)
# for eachItem in simpleGen():
#     print eachItem


"""
上面是个有点笨拙的例子，为什么不对着使用真正的迭代器呢？许多动机院子能够迭代穿越序列，而这需要函数为例而不是已经在某个序列中静态对象。
接下来的例子中，我们将要创建一个带序列并从那个序列中返回一个随机元素的随机迭代器：
"""
# from random import randint
# def randGen(aList):
#     while len(aList) > 0:
#         yield aList.pop(randint(0,len(aList)))
# '不同点在于每个返回的元素将从那个队列中消失，像一个list.pop()和random.choice()的结合的归类'
# for item in randGen(['rock','paper','scissors']):
#     print item


"""
    使用生成器最好的地方就是当你正迭代穿越一个巨大的数据集合，而重复迭代这个数据集合是一个很麻烦的事，比如一个巨大的磁盘文件，
或者一个复杂的数据库查询。对于每行的数据，你希望执行非元素的操作以及处理，但当正指向和迭代过它的时候，你“不想失去你的地盘”。
    你想要抓取一块数据，比如，将它返回给调用者来处理以及可能的对（另外一个）数据库的插入，接着你想要运行一次next()来获得下一块的数据，
等等。状态在挂起和再继续的过程中是保留了的，所以你会觉得很舒服有一个安全的处理数据的环境。没有生成器的话，你的程序代码很有可能会有很长的
函数，里面有一个很长的循环。当然，这仅仅是因为一个语言这样的特征不意味着你需要用它。如果在你程序里没有明显合适的话，那就别增加多余的复杂性！
当你遇到合适的情况时，你便会知道什么时候生成器正是要使用的东西。
"""

######      11.10.2 加强的生成器特性
#   用户可以将值会送给生成器[send()]，在生成器中抛出异常，以及要求生成器退出[close()]
# 由于双向的动作涉及叫做send()的代码来向生成器发送值（以及生成器返回的值发送回来），现在yield语句必须是一个表达式，
# 因为当回到生成器中继续执行的时候，你或许正在接受一个进入的对象。
def counter(start_at=0):
    count = start_at
    while True:
        val = (yield count)
        if val is not None:
            count = val
        else:
            count += 1
#   生成器带有一个初始化的值，对每次对生成器[next()]调用以1累加计数。用户亦可以选择重置这个值，如果他们非常想要用新的值来
# 调用send()不是调用next()。这个生成器是永远运行的，所以如果你想要终结它，调用close()方法。如果我们交互运行这段代码，会得到如下
# 输出：
print "counter(5)"
count = counter(5)
time.sleep(1)
print count.next()
time.sleep(1)
print count.next()
time.sleep(1)
print "调用count.send(9)"
print count.send(9)
time.sleep(1)
print count.next()
time.sleep(1)
print "调用count.close()",count.close()
time.sleep(1)
print count.next()



#生成器测试
# def test():
#     yield 1     #方法中只要包含yield语句，就会变成生成器
#     print 'hello, world'
#
# test = test()
# print test


if __name__ == '__main__':
    # main()
    pass


