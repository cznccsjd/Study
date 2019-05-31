#utf-8
'''
爬虫学习文件
参考文档：https://www.cnblogs.com/carlos-mm/p/8819519.html
'''

# Urllib库是python中的一个功能强大的，用于操做URL，并在做爬虫的时候经常要用到的库

import urllib

url = "http://www.baidu.com"
response1 = urllib.request.urlopen(url)
print('第一种方法')
# 获取状态码，200表示成功
print(response1.getcode())
# 获取网页内容
print(response1.read())
