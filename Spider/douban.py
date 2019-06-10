#coding:utf-8
'''
豆瓣小组查找符合条件的租房信息 dict{key=url:values=组名}
'''

import requests
from bs4 import BeautifulSoup

class Douban():
    def searchUrl(self,num=0):
        '''
        拼接get请求的url和传输的params
        :param num: 起始页面，默认为0
        :return: 返回请求时的url和传递的参数
        '''
        while(num >= 0):
            searchurl = 'https://www.douban.com/group/search'
            searchdata = {'start':num, 'cat': '1019', 'q': '北京租房'}      #cat=1019是直接通过豆瓣页面获取到
            header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
            return searchurl, searchdata, header


    def search(self):
        '''
        执行搜索动作，获取相应后的小组名称和url
        :return:
        '''
        urls = {}   # 定义一个字典存储BeautifulSoup处理后的豆瓣租房小组的标题和url

        for num in range (0, 220, 20):      #通过豆瓣页面查询到的，当start>200时，会跳转到登录页面了
            url, data, header= Douban().searchUrl(num)
            rSearch = requests.get(url, data, headers=header)

            # 使用BeautifulSoup4处理requests返回的结果，找到全部的标题和url
            soup = BeautifulSoup(rSearch.text,'lxml')
            titles = soup.select('div.title > h3 > a')
            links = soup.select('div.title > h3 > a')

            for title, link in  zip(titles, links):
                title = title.text
                link = link.get('href')
                ret = Douban().searchResult(title)

                if ret:
                    urls[link] = ret      #豆瓣租房小组的组名可能有重复，用来做dict的value；小组的url肯定是唯一的，用来做dict的key
        return urls


    def searchResult(self,title):
        '''
        将不符合规则的响应结果去除
        :return:
        '''
        str = '北京'
        strNos = ['朝阳','望京','丰台','通州','大兴','燕郊','顺义','CBD','芍药居','惠新西街南口','双井','八通','国贸','宋家庄','酒仙桥']

        while(str in title):
            num = 0
            for strNo in strNos:
                if strNo in title:
                    break
                else:
                    num += 1

            if num == len(strNos):
                return title
            else:
                break

if __name__ == '__main__':
    Douban().search()
