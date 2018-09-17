#coding:utf-8
"""
学习json模块
"""
import json

python_dic = {'name':'zhangsan','sex':'Man','age':30}
# json_str = "{'name':'lisi','sex':'Female','age':31}"  #这种写法会导致json.loads()执行的时候，报错，下面'{"":""}'写法，就不会
json_str = '{"name":"lisi","sex":"Female","age":31}'

# 将Python对象转换为json字符串
# print 'python对象转换为json字符串后的类别：',type(json.dumps(python_dic,encoding='utf-8'))
# print 'python对象转换为json字符串后的内容：',json.dumps(python_dic,encoding='utf-8')

# 将json字符串转换成Python对象
print 'json字符串转换成python对象后的类别：',type(json.loads(json_str,encoding='utf-8'))
print 'json字符串转换成Python对象后的内容：',json.loads(json_str,encoding='utf-8')


# json.dump()的用法：往文件中写入json字符串
jsonfile = open('./test.json','w')
jsonfile.truncate()     #清空原有文件的内容
# 使用json.dump()方法，往文件中写入json字符串
print 'json.dump()往文件中写入json字符串：',json.dump(json_str,jsonfile)


#json.load()方法，读取文件中的json字符串内容
'''
下面的json.load()执行后，报错，后续应该继续查找报错的原因
'''
jsonfileR = open('./test.json','r')
print 'json.load()读取文件中的json字符串：',json.load(jsonfileR)
# print jsonfileR.readlines()




"""
下面的代码，json_load()读取正常，上面代码的读取有问题，怀疑是json_str的""导致的；
"""
# # json.dump()函数的使用，将json信息写进文件
# json_info = "{'age': '12'}"
# file = open('1.json','w')
# json.dump(json_info,file)
#
# # json.load()函数的使用，将读取json信息
# file = open('1.json','r')
# info = json.load(file)
# print(info)