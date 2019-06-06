#coding:utf-8
'''
豆瓣小组租房文件
'''

import urllib.request
import requests
from bs4 import BeautifulSoup

# url = 'https://www.douban.com/group/beijingzufang/discussion?start=0'

# 搜索豆瓣北京租房小组
urlSearch = 'https://www.douban.com/group/search'
dataSearch = {'start':'0','cat':'1019','q':'北京租房'}

rSearch = requests.get(urlSearch,dataSearch)
# print(rSearch.text)

# 使用BeautifulSoup4处理返回的结果
soup = BeautifulSoup(rSearch.text,'lxml')
# div = soup.select('div > div.article > div.groups > div:nth-child(4) > div.content > div.title > h3 > a')
titles = soup.select('div.title > h3 > a')
links = soup.select('div.title > h3 > a')

print(titles)
print(len(titles))
# for title, link in  zip(titles, links):
#     print("title:\n", title)

# results = soup.find_all('a',{'class':'','href':'https://www.douban.com/group'})
results = soup.find('div',{'class':'title'})
print(results)
result = results.find_all('a',{'class':''})
print(result)
print(len(result),type(result))
# print(result.text)