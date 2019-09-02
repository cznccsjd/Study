#coding:utf-8
'''
Author:jlz
Date:2019/9/2
Describe:实现简单的计算器：+ - * /
'''
class Calculator():
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)
        
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
        