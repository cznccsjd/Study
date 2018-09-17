#coding:utf-8
"""
学习Radnom模块
"""
import random

# 生成浮点随机数
print '1-20的随机浮点数：',random.uniform(1, 20)
#生成随机整数
print '1-20随机整数：',random.randint(1,20)
# 随机获取sequence序列一个元素(列表[]，或者元组()均可)
print '获取随机数：',random.choice(('tom','jim','lily','lucy'))
# 随机获取sequence序列中多个元素
print '获取%d个随机数：%s'%(2,random.sample(('tom','jim','lily','lucy'),2))
# 打乱list里面元素的顺序
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list)
print '打乱list元素顺序后的输出结果：',list