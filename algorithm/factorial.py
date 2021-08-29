#coding:utf-8
"""
阶乘
一个正整数的阶乘，是所有小于等于该数的正整数的积，并且0的阶乘为1；
即：n!=1*2*3*4...*(n-1)*n
阶乘亦可用递归方式定义：0!=1,n!=(n-1)!*n
"""
def fac(x):
    if x < 2:
        return 1
    else:
        return x*fac(x-1)


print(fac(5))