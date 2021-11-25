#coding:utf-8
'''
元组学习
集合（set）是一个无序的不重复元素序列。
可以使用{ }或者set()函数创建集合。
注意：创建一个空集合必须用set()而不是{ }，因为{ }用来创建一个空字典。
创建格式：
parame = {value01,value02,...}或者set(value)
'''
# 演示去重功能
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(f'演示去重功能{basket}')
print(f"快速判断元素orange是否在集合内:{'orange' in basket}")
print(f"快速判断元素crabgrass是否在集合内:{'crabgrass' in basket}")

# 集合间运算
a = set('abracadabra')
b = set('alacazam')
print(f'集合a中的元素:{a}')
print(f'集合b中的元素：{b}')
print(f'a - b：集合a中包含而集合b中不包含的元素{a - b}')    #集合a中包含而集合b中不包含的元素
print(f'a | b:集合a或集合b中包含的所有元素{a | b}')    #集合a或集合b中包含的所有元素
print(f'a & b:集合a和集合b中都包含的元素{a & b}')    #集合a和集合b中都包含的元素
print(f'a ^ b:不同时包含于集合a和集合b中的元素{a ^ b}')    #不同时包含于集合a和集合b中的元素

# s.add(x) 添加元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add("Facebook")
print(thisset)

# s.update(x) 添加元素，并且参数可以是列表、元组、字典等等
thisset.update({1,3})
print(thisset)

# s.remove(x) 移除元素
thisset.remove("Taobao")
print(thisset)
# 如果移除不存在的元素，会报错
# thisset.remove("Wechat")
# 使用discard移除不存在的元素，不会报错
thisset.discard("Wechat")
# pop,随机删除一个元素
thisset.pop()
print(thisset)

# len(),计算集合的长度
print(f"此时集合的元素为：{thisset}")
print(f"计算集合元素的个数：{len(thisset)}")

# clear()清空集合
thisset.clear()
print(f"clear后，集合的元素为：{thisset}")

# difference()，返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合（方法的参数）中
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference()
print(z)