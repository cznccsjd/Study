#coding:utf-8
"""
累加：
eg:
    5 = 4 + 3 + 2 + 1
"""
def sum(x):
    if x < 2:
        return 1;
    return x + sum(x-1)


print(sum(5))