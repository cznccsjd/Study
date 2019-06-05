#utf-8
'''
爬虫学习文件
'''

# Urllib库是python中的一个功能强大的，用于操做URL，并在做爬虫的时候经常要用到的库
'''
基本使用
urllib.request.urlopen()：访问一个URL，返回一个包含网页信息的对象
response.read()：获取返回对象的内容
response.getcode()：获取返回的HTTP Code
response.info()：获取返回的元数据信息，例如HTTP Header
response.geturl()：获取访问的url
'''

import urllib.request
import time

# 使用Python访问博客园，获取网页信息
# response = urllib.request.urlopen('https://www.cnblogs.com/csjd')
# data = response.read().decode('utf-8')      #如果不加decode('utf-8')，返回的类型是bytes；加了decode('utf-8')，返回的类型是str
# print(data)


# 使用Python下载一个图片
# url = 'http://img.lenovomm.com/s3/img/app/app-img-lestore/2370-2015-07-16035439-1437033279327.jpg?isCompress=true&width=320&height=480&quantity=1&rotate=true'
# response = urllib.request.urlopen(url)
# data = response.read()

#图片输入二进制文件，所以需要用b模式打开写入
# with open('img.jpg', 'wb') as f:
#     f.write(data)   #下载的图片会写入到当前路径下


##########  定制HTTP header
'''
HTTP Header，表示在浏览器在进行访问(HTTP请求)时携带的头部信息，
什么叫定制HTTP请求头呢，举个栗子：其实每天活跃在网上的爬虫太多了，如果网站不进行限制的话，
那么访问流量会很高，所以站点基本都会对爬虫进行基本的限制，而利用User-Agent (浏览器标示)是最常用的方式，
使用浏览器和使用Python代码来访问站点时，浏览器标示时不同的。
chrome浏览器：Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36
Python代码：Python-urllib/3.6
这里既然说定制，那么就是说可以对User-Agent等头部参数进行修改
'''
#修改User-Agent
# 修改请求的User-Agent就需要先定制request对象了，然后把对象传给urlopen进行访问
# url = 'http://img.lenovomm.com/s3/img/app/app-img-lestore/2370-2015-07-16035439-1437033279327.jpg?isCompress=true&width=320&height=480&quantity=1&rotate=true'

# head = {}
# head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'

#创建request对象，设置headers
# request = urllib.request.Request(url,headers=head)
# response = urllib.request.urlopen(request)

# data = response.read()

# with open('img.jpg','wb') as f:
#     f.write(data)


##### 添加headers的另一种方法
# 除了在代码中通过字典定义header以外，还可以使用request对象的add_header()方法，进行添加
# url = 'http://img.lenovomm.com/s3/img/app/app-img-lestore/2370-2015-07-16035439-1437033279327.jpg?isCompress=true&width=320&height=480&quantity=1&rotate=true'

# request = urllib.request.Request(url)
# request.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36')
# response = urllib.request.urlopen(request)

# data = response.read()

# with open('img.jpg','wb') as f:
#     f.write(data)


##### HTTP代理
'''
使用HTTP代理步骤

#1、创建一个HTTP代理
http_proxy = urllib.request.ProxyHandler({'代理类型':'IP:Port'})

# 2、创建一个opener
opener = urllib.request.build_opener(http_proxy)
#PS：当我们使用urlopen访问url时，其实使用的是默认的opener来进行工作的，我们可以对其进行定制，这里就是定制它使用http代理进行访问

# 3、安装opener
urllib.request.install_opener(opener)
# PS:执行完毕后，后续所有的请求都会使用该opener进行访问，所以如果只是一次特殊的请求，那么可以使用 opener.open(url) 来访问url
'''
# 下述代码报错了，估计是代理服务器的问题
#create http_proxy
# http_proxy = urllib.request.ProxyHandler(proxies={'http':'114.215.192.184.8081'})

# create opener
# opener = urllib.request.build_opener(http_proxy)
# response = opener.open("http://ifconfig.io")
# data = response.read().decode('utf-8')
# print(data)

#可以定义多个http_list，利用random随机选择
import random

# http_proxy_list = [
#     '110.73.10.15:8123',
#     '114.230.105.34:21642'
# ]

# http_proxy = urllib.request.ProxyHandler(proxies={'http':random.choice(http_proxy_list)})

##  添加header
# opener也可以添加header，使用addheaders = [('key','value')]
# opener = urllib.request.build_opener(http_proxy)
# opener.addheaders = [('User-Agent','Mozilla/5.0')]



##########  异常处理
# URLError，是urllib的异常类
import urllib.error

# url故意写成htt，可以得到一个错误
# urllib.request.urlopen('htt://www.baidu.com')   #urllib.error.URLError: <urlopen error unknown url type: htt>

# 捕获异常，不让程序崩溃
# try:
#     urllib.request.urlopen('htt://www.baidu.com')
# except urllib.error.URLError as e:
#     print(e.reason)

# 捕获域名到期异常
# try:
#     urllib.request.urlopen('http://www.imooclimooc2.com')
# except urllib.error.URLError as e:
#     print(e.reason)

# HTTPError 访问不存在 404
# urllib.request.urlopen('http://www.imooc.com/cheshen.html')
# 捕获异常
# try:
#     urllib.request.urlopen('http://www.imooc.com/cheshen.html')
# except urllib.error.HTTPError as e:
#     print(e.reason)
#     print(e.code)




##########  Beautiful Soup
# Beautiful Soup: Python 的第三方插件用来提取 xml 和 HTML 中的数据，官网地址 https://www.crummy.com/software/BeautifulSoup/
# 实战，获取imooc首页推荐的实战课，这几个图片xpath路径最后都为：<h3 class="course-card-name">xxxx</h3>，其实这么简单的写，还真的是有问题，会获取所有图片，不仅仅是实战课中的

# 导包
from bs4 import BeautifulSoup

# 创建一个request对象
# req = urllib.request.Request('https://www.imooc.com/')

# 使用Request对象发送请求
# res = urllib.request.urlopen(req)
# response = res.read()
# print('response返回结果:\n', response.decode('utf-8'))

# soup = BeautifulSoup(response,'html.parser')

# course_names = soup.find_all('h3', {'class':'course-card-name'})
# print('最终筛选结果：\n',course_names)
# print('lens of result:\n', len(course_names))


#上面返回了71个结果，显然包含很多不是实战推荐的课程，继续找页面上一级路径，再进行搜索，缩小检索范围
req = urllib.request.Request('https://www.imooc.com/')
res = urllib.request.urlopen(req)
response = res.read()

soup = BeautifulSoup(response,'html.parser')
# 先获取找到的div
course_div = soup.find('div',{'class':'clearfix types-content'})
# 再从div里获取想要的内容,注意，AttributeError: ResultSet object has no attribute 'find_all'. You're probably treating a list of items like a single item. Did you call find_all() when you meant to call find()?
course_names = course_div.find_all('h3', {'class':'course-card-name'})
print('增加div筛选后，结果：\n',course_names)
print('这次结果长度为：\n', len(course_names))

# 将结果中多余的h3 class="course-card-name" 字样去除
for course_name in course_names:
    print(course_name.text)