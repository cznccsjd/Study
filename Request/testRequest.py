#coding:utf-8
'''
学习request模块的文件
'''

import requests

# get
r = requests.get('https://postman-echo.com/get')

# post
# r = requests.post()

# 请求结果
print(r)