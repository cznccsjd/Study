#coding:utf-8
'''
菜鸟学习装饰器
'''
def deco_one():
    print("这是一个装饰器测试方法")

def test(func):
    def test_deco():
        print("装饰器方法开始了")
        func()
        print("装饰器方法结束了")
    return test_deco


t = test(deco_one)
t()

@test
def deco_two():
    print("这是deco_two装饰器测试方法")


deco_two()
print(deco_two.__name__)
