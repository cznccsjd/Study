#coding:utf-8
'''
学习request模块的文件
快速上手
学习资料：https://2.python-requests.org//zh_CN/latest/user/quickstart.html
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
r = requests.get('https://postman-echo.com/get', stream=True)
print('原始响应内容:\n',r.raw , r.raw.read())
r.close()


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
# print('Cookie:\n', r.cookies)

# 发送自己的cookies到服务器
# url = 'http://httpbin.org/cookies'
# cookies = dict(cookies_are='working')
# r = requests.get(url,cookies=cookies)
# print('带有自己编写的cookie的请求：',r.text)

# Cookie的返回对象为RequestsCookieJar，它的行为和字典类似，但接口更为完整，适合跨域名跨路径使用。还可以把Cookie Jar传到Requests中
# print('Cookie的类型:\n', type(r.cookies))  #类型是:RequestsCookieJar
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# urls = 'http://httpbin.org/elsewhere'
# r = requests.get(url, cookies=jar)
# rs = requests.get(urls, cookies=jar)
# print('jar的值：\n', jar)
# print('传递给url的cookie：\n', r.text)
# print('传递给urls的cookie：\n', rs.text)


########  重定向与请求历史
# 默认情况下，除了 HEAD, Requests 会自动处理所有重定向。
# 可以使用响应对象的 history 方法来追踪重定向。
# Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。
# 例如，Github 将所有的 HTTP 请求重定向到 HTTPS：
# r = requests.get('http://github.com')
# print('重定向，此时实际请求url：', r.url)
# print('重定向，返回的状态码：', r.status_code)
# print('重定向，请求的历史：', r.history)

# 如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理：
# r = requests.get('http://github.com', allow_redirects=False)
# print('重定向，实际请求的url：', r.url)
# print('重定向，返回的状态码：', r.status_code)
# print('重定向，请求的历史:', r.history)

# 如果你使用了 HEAD，你也可以启用重定向：
# r = requests.head('http://github.com', allow_redirects=True)
# print('重定向，启用HEAD后，url：', r.url)
# print('重定向，请求历史：', r.history)


##########  超时
# 你可以告诉 requests 在经过以 timeout 参数设定的秒数时间之后停止等待响应。基本上所有的生产代码都应该使用这一参数。如果不使用，你的程序可能会永远失去响应：（错误异常ConnectTimeout）
r = requests.get('http://github.com', timeout=0.001)
'''
注意说明：
timeout 仅对连接过程有效，与响应体的下载无关。 
timeout 并不是整个下载响应的时间限制，而是如果服务器在 timeout 秒内没有应答，
将会引发一个异常（更精确地说，是在 timeout 秒内没有从基础套接字上接收到任何字节的数据时）
If no timeout is specified explicitly, requests do not time out.
'''


##########  错误与异常
'''
遇到网络问题（如：DNS 查询失败、拒绝连接等）时，Requests 会抛出一个 ConnectionError 异常。
如果 HTTP 请求返回了不成功的状态码， Response.raise_for_status() 会抛出一个 HTTPError 异常。
若请求超时，则抛出一个 Timeout 异常。
若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常。
所有Requests显式抛出的异常都继承自 requests.exceptions.RequestException 
'''