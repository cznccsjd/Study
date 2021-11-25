#coding:utf-8
'''
装饰器原理：
封装了一个函数，用这样或者那样的方式来改变它的行为。
'''

# 这里的装饰器，其实就是将函数作为一个参数，传给另一个函数
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")

# 只执行方法a_function_requiring_decoration
a_function_requiring_decoration()

print('\n===================\n')
test = a_new_decorator(a_function_requiring_decoration)
print(f"test的值是a_new_decorator方法中返回的wrapTheFunction方法，{test}")

# test()是开始执行wrapTheFunction()
print('\n===================\n')
test()