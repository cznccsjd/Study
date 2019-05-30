#coding:utf-8
'''
requests模块的高级用法
参考资料：https://2.python-requests.org//zh_CN/latest/user/advanced.html
'''
import requests

##########  会话对象
'''
会话对象让你能够跨请求保持某些参数。他也会在同一个Session实例发出的所有请求之间保持cookie，期间使用urllib3的connection pooling功能。
所以如果你向同一主机发送多个请求，底层的TCP连接将会被重用，从而带来显著的性能提升。
'''
# 会话对象具有主要的 Requests API 的所有方法。
# 我们来跨请求保持一些 cookie:
# s = requests.Session()

# s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# r = s.get("http://httpbin.org/cookies")

# print('会话对象的cookie:\n', r.text)

# 会话也可用来为请求方法提供缺省数据。这是通过为会话对象的属性提供数据来实现的。
# s = requests.Session()
# s.auth = ('user', 'pass')
# s.headers.update({'x-test': 'true'})

#'x-test'和'x-test2'都会被发送
# r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
# print('会话对象，添加属性:\n', r.text)

# 任何你传递给请求方法的字典都会与已设置会话层数据合并。方法层的参数覆盖会话的参数。
# 不过需要注意，就算使用了会话，方法级别的参数也不会被跨请求保持。下面的例子只会和第一个请求发送 cookie ，而非第二个：
# s = requests.Session()

# r = s.get('http://httpbin.org/cookies', cookies={'form-my': 'browser'})
# print(r.text)

# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# 如果要手动为绘画添加cookie，就是用Cookie utility函数来操纵Session.cookies
# 会话还可以用作前后文管理器
# with requests.Session() as s:
#     s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

# 这样能确保with区块退出后会话能被关闭，即使发生了异常也一样




##########  请求与响应对象
'''
任何时候进行了类似 requests.get() 的调用，你都在做两件主要的事情。其一，你在构建一个 Request 对象， 该对象将被发送到某个服务器请求或查询一些资源。
其二，一旦 requests 得到一个从服务器返回的响应就会产生一个 Response 对象。该响应对象包含服务器返回的所有信息，也包含你原来创建的 Request 对象。
如下是一个简单的请求，从 Wikipedia 的服务器得到一些非常重要的信息：
'''
# r = requests.get('https://www.baidu.com')

# 如果想访问服务器返回给我们的响应头部信息，可以这样做：
# print('请求与响应对象，response的headers：\n', r.headers)

# 如果想得到发送到服务器的请求的头部，可以简单的访问该请求，然后是该请求的头部：
# print('请求与响应对象，request的headers：\n',r.request.headers)




##########  准备的请求（Prepared Request）
'''
当你从 API 或者会话调用中收到一个 Response 对象时，request 属性其实是使用了 PreparedRequest。
有时在发送请求之前，你需要对 body 或者 header （或者别的什么东西）做一些额外处理，下面演示了一个简单的做法：
'''
#下面的代码不全，看文档吧，有些参数不全，代码运行不起来

# from requests import Request, Session

# url = 'https://postman-echo.com/post'
# data = {"method": "POST"}
# header = {"Content-Type":"application/json"}

# s = Session()
# req = Request('POST', url,
#               data = data,
#               headers=header
#               )
# prepped = req.prepare()

# do someting with prepped.body
#do something with prepped.headers

# resp = s.send(prepped,
#               stream=stream,
#               verify=verify,
#               proxies=proxies,
#               cert=cert,
#               timeout=timeout
#               )

# print(resp.status_code)




#########  SSL证书验证
'''
Requests可以为HTTPS请求验证SSL证书，就像web浏览器一样。SSL验证默认是开启的，如果证书验证失败，Requests会抛出SSLError：
'''
# requests.get('https://requestb.in') #返回“requests.exceptions.ConnectionError: HTTPSConnectionPool(host='requestb.in', port=443): Max retries exceeded with url: / (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x05E500D0>: Failed to establish a new connection: [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。',))”

#域名上没有设置SSL，所以失败了。但Github设置了SSL：
# r = requests.get('https://github.com', verify=True)
# print(r.status_code)

#可以为verify传入CA_BUNDLE文件的路径，或者包含可新人CA证书文件的文件夹路径
# requests.get('https://github.com', verify='/path/to/certfile')


##########  客户端证书
# 可以指定一个本地证书用作客户端证书，可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组
# requests.get('https://kennethreitz.org', cert=('/path/client.cert','/path/client.key'))


###########  响应体内容工作流
# 默认情况下，进行网络请求后，响应体会立即被下载。可以通过stream参数覆盖这个行为，推迟下载响应体直到访问Response.content属性
tarball_url = 'https://github.com/kennethreitz/requests/tarball/master'
r = requests.get(tarball_url, stream=True)
# 此时仅有响应头被下载下来了，连接保持打开状态，因此允许我们根据条件获取内容：
# print(r.headers['content-length'])    #看看content-length的长度
if int(r.headers['content-length']) < 500000:
    content = r.content
    print('content:\n', content)    #这个url返回的二进制内容是NULL