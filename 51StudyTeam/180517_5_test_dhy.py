__author__ = 'donghuiyan'
# -*- coding=utf-8 -*-
'''
题目：写一个摇骰子游戏，要求用户压大小，赔率一赔一。
要求：三个骰子，摇大小，每次打印摇骰子数。
'''
import  random

#随机生成三个骰子，庄家得出大小
def zhuangrand():
    ran1=random.randint(1,6)
    ran2=random.randint(1,6)
    ran3=random.randint(1,6)
    sum=ran1+ran2+ran3
    print("三个骰子的值是：",ran1,ran2,ran3)
    if sum>=11:
        print("庄家出大")
        return True
    else:
        print("庄家出小")
        return False

#客人压大压小
def kerand():
    ke=random.randint(0,1)
    if ke==1:
        print("客人压大")
        return True
    else:
        print("客人压小")
        return False

#比较结果
def compare():
    if zhuangrand()==kerand():
        return True
    else:
        return False




#开始游戏
def startGame():
    #赌注
    global zhuangmoney
    global kemoney
    global money
    xmoney=0
    money=0
    if(zhuangmoney<=kemoney):
        xmoney=zhuangmoney
    else:
        xmoney=kemoney
    if xmoney>50:
        money=random.randrange(50,xmoney,50)
    else:
        money=50

    print('客人压钱为：',money)
    if kemoney>0 and zhuangmoney>0:
        if compare()==True:
            print('客人赢')
            zhuangmoney=zhuangmoney-money
            kemoney=kemoney+money
        else:
            print('庄家赢')
            zhuangmoney=zhuangmoney+money
            kemoney=kemoney-money
        print("庄家剩余钱是：",zhuangmoney,'客人剩余钱是：',kemoney)
        if kemoney>0 and zhuangmoney>0:
            print('钱还是很充足的，继续吧！')
            return True
        elif kemoney>0 and zhuangmoney==0:
            print('客人手气真好，把庄家赢光了！')
            return False
        elif kemoney==0 and zhuangmoney>0:
            print('客人手气有点差，今天输完了，下次继续！')
            return False








if __name__ == '__main__':
    zhuangmoney=1000
    kemoney=1000
    money=0
    n=2
    print('*********************************************************')
    print('第1局开始！')
    while(startGame()==True):
        print('*********************************************************')
        print('第%d局开始！'%n)
        n=n+1






