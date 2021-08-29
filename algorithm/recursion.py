#coding:utf-8
"""
递归：如果函数包含对其自身的调用，该函数就是递归；
阶乘函数：
N! = factorial(N) = 1*2*3...*N
我们可以用这种方式来看阶乘：
factorial(N) = N!
             =N * (N-1)!
             =N * (N-1) * (N-2)!
                       :
             =N * (N-1) * (n-2) * ...* 3 * 2 * 1
我们现在可以看到阶乘是递归的，因为factorial(N) = N * factorial(N-1)。换句话说，为了获取factorial(N)
的值，需要计算factorial(N-1)。而且，为了找到factorial(N-1)，需要计算factorial(N-2)等。
我们现在给出阶乘函数的递归版本》
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1;
    else:
        return n * factorial(n-1)


print(factorial(5))
