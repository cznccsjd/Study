#coding:utf-8
import operator

t1 = (1,2,3,4,'abc','hj','hk','hk')
t2 = {1,2,3,4,'abc','hk','hj','aa'}

# result = operator.eq(t1,t2)
# print(result)
# print(type(result))
print(t1)
print(len(t1))
t1 = set(t1)
print(t1)
print(len(t1))

t = t1 ^ t2
print(t)
print(len(t))