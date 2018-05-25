#coding:utf-8
"""
算数游戏

"""

#1/usr/bin/env python

from operator import add, sub
from random import randint,choice

ops = {'+':add, '-':sub}
MAXTRIES = 2        #定义用户可以尝试的次数

def doprob():
    """
    这是核心的代码
    :return: 
    """
    op = choice('+-')
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse=True)     #sort()排序，默认reverse=False，正序从小到大排序；reverse=True，倒序排序
    ans = ops[op](*nums)
    pr = '%d %s %d=' % (nums[0],op,nums[1])
    oops = 0
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print "correct"
                break
            if oops == MAXTRIES:
                print 'answer\n%s%d'%(pr,ans)
            else:
                print 'incorrect...try again'
                oops += 1
        except (KeyboardInterrupt,EOFError,ValueError):
            print 'invaild input...try again'

def main():
    while True:
        doprob()
        try:
            opt = raw_input('Again? [y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt,EOFError):
            break

if __name__ == '__main__':
    main()
    # help(doprob)      #验证打印函数的说明文档