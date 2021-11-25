#coding:utf-8

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Docorate me!"""
    print("I am the function which needs some decoration to remove my foul smell")

a_function_requiring_decoration()
# 没有加@时，a_function_requiring_decoration.__name__的值是a_function_requiring_decoration
# 加了@后，a_function_requiring_decoration.__name__的值是wrapTheFunciton
print(f"a_function_requiring_decoration.__name__的值是：{a_function_requiring_decoration.__name__}")
print(a_function_requiring_decoration.__doc__)

# 加了@后，如果希望a_function_requiring_decoration.__name__输出a_function_requiring_decoration，那就使用functools.wraps