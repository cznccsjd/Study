#coding:utf-8
'''
学习request模块的文件
'''

import requests

########## 发送请求
# get
r = requests.get('https://postman-echo.com/get')

# post
# R = requests.post('https://postman-echo.com/post',data={'method':'POST'})

# 请求结果，返回的结果是状态码 200。类型是<class 'requests.models.Response'>
# print('返回的结果：',r,R)
# print(type(r),type(R))

# put
# put = requests.put('https://postman-echo.com/put', data={'method':'PUT'})
# delete
# dele = requests.delete('https://postman-echo.com/delete')
# head
# head = requests.head('http://httpbin.org/get')
# option
# opt = requests.options('http://httpbin.org/get')
# 请求的结果，返回的是状态码200
# print(put, dele, head, opt)


##########  传递URL参数
# quest = {'q':'talk','tag':'','start':0,'count':1}
# post = requests.get('https://api.douban.com/v2/book/search',params=quest)
# print('传递URL参数：', post.url)


#########  响应内容
# print('get响应的内容：\n',r.text)
# print('get响应的编码：\n',r.encoding)


########  二进制响应内容
# print('get响应的二进制内容：\n',r.content)


#########  JSON响应内容
# print('JSON响应的内容：\n',r.json())
'''
需要注意的是，成功调用 r.json() 并**不**意味着响应的成功。有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。
这种 JSON 会被解码返回。要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。
'''
# print('通过判断响应状态码来确认，返回的json是否正确：')
# print(r.status_code,r.raise_for_status())   #"""r.raise_for_status():Raises stored :class:`HTTPError`, if one occurred."""


#########  原始响应内容
# r = requests.get('https://postman-echo.com/get', stream=True)
# print('原始响应内容:\n',r.raw , r.raw.read())


#########  定制请求头  --> 这部分还是去看官方文档吧
# url = 'https://api.github.com//some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)
# print('定制请求头:\n', r.text)



#########  更加复杂的POST请求
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)


########  响应状态码
# print('响应状态码：\n', r.status_code)
# Requests还附带一个内置的状态码查询对象
# print(r.status_code == requests.codes.ok)

# 如果发送了一个错误请求(一个 4XX 客户端错误，或者 5XX 服务器错误响应)，我们可以通过 Response.raise_for_status() 来抛出异常：
# bad_r = requests.get('http://httpbin.org/status/404')
# print('bad_status:',bad_r.status_code)
# print('抛出异常:\n',bad_r.raise_for_status())


#########  响应头
# print('python字典形式展示的服务器响应头：\n', r.headers)
# 由于HTTP头部大小写不敏感
# print('响应大小写都可以访问:',r.headers['Content-Encoding'])
# print(r.headers['content-encoding'])


##########  Cookie
# 某些响应中包含一些cookie
print('Cookie:\n', r.cookies)