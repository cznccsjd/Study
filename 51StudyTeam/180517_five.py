#coding:utf-8
"""
题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。
要求：三个骰子，摇大小，每次打印摇骰子数。
"""

from random import randint,choice,randrange
import time

money_zhuang = 1000 #庄家初始1000块钱
money_keren = 1000  #客人初始1000块钱
num = 1

def saizi():
    """
    # 生成三个随机数，作为三个骰子
    :return: 
    """
    ram1 = randint(1,6)
    ram2 = randint(1,6)
    ram3 = randint(1,6)
    sum = ram1 + ram2 + ram3

    print "******  第",num,"局  *****"
    print "三个骰子的数值是：", (ram1,ram2,ram3)

    if sum < 11:
        result = u"小"
    else:
        result = u"大"
    print "骰子结果是：",result
    # print type(result)

    # 客人猜测骰子大小
    cho = choice(u"大小")
    print "客人猜的骰子结果是：",(cho)
    # print type(cho)

    #客人押的钱
    money = randrange(10,500,5)     #   取随机数，def randrange(self, start, stop=None, step=1, _int=int):
    print "本次赌注是：",money

    # 游戏结果，包含金钱计算
    if result == cho:
        mon_keren = money_keren + money
        mon_zhuang = money_zhuang - money
        print "客人赢了！赢了",money,"元钱。当前客人总共有",mon_keren,"元钱；"
        print "当前庄家还有", mon_zhuang, "元钱"
    else:
        mon_keren = money_keren - money
        mon_zhuang = money_zhuang + money
        print "客人输了！输了",money,"元钱。当前客人总共有",mon_keren,"元钱；"
        print "当前庄家还有", mon_zhuang, "元钱"

    ###################下面的global全局变量定义的应该有问题，后面有时间再改吧
    global money_zhuang
    global money_keren
    global num
    money_zhuang = mon_zhuang
    money_keren = mon_keren
    num = num + 1

    #如果有任何一方还有钱，继续赌
    if(mon_keren < 10):
        # mon_temp = 0 - money_keren        #要避免 最后钱是负的
        # mon_keren = mon_keren + mon_temp
        print "客人余额",mon_keren,"不足10元，不让玩了"
    elif(mon_zhuang < 10):
        print "庄家余额",money_zhuang,"不足10元，不让玩了"
    else:
        print "钱还多着呢，继续嗨皮！"
        print "*******************************************"
        print "\n"
        #每局结束，休息2秒钟
        time.sleep(2)
        saizi()

if __name__ == '__main__':
    saizi()

