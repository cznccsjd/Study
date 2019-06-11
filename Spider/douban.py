#coding:utf-8
'''
实现功能：
1、豆瓣小组关键字搜索（北京租房）
2、去除不符合要求的小组
3、返回小组名称和小组url
PS：返回dict类型，key=url, values=组名
'''

import requests
from bs4 import BeautifulSoup
import time

class Douban():
    def __init__(self):
        pass

    def config(self):
        '''
        配置，参数化，便于后续新增配置文件
        :return:
        '''
        dict = {}
        dict['url1'] = 'https://www.douban.com/group/search'
        dict['headers'] = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        dict['sleep'] = 10
        # 浏览器拷贝过来的cookie是str，需要转换为dict
        cookie = 'bid=n4knZ-I4N7k; __utmc=30149280; ct=y; ll="108288"; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1560237015%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D98_AscV-k0modJWTChFjjwhOXLp6KfrVyC641njNilm%26wd%3D%26eqid%3Daf1567b90000368a000000025cff53d0%22%5D; _pk_ses.100001.8cb4=*; __utma=30149280.1704380107.1560230238.1560237021.1560237022.4; __utmz=30149280.1560237022.4.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; dbcl2="180074916:nif7JgNsI3I"; ck=4nDJ; _pk_id.100001.8cb4=5164272b35769681.1560230238.3.1560238077.1560234397.; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18007; __utmb=30149280.9.9.1560238079303'
        if type(cookie) == str:
            items = cookie.split(";")
            coo = {}
            for item in items:
                kv = item.split("=")
                coo[kv[0]] = kv[1]
            dict['cookie'] = coo

        dict['city'] = '北京'
        dict['notArea'] = ['朝阳','望京','丰台','通州','大兴','燕郊','顺义','CBD','芍药居','惠新西街南口','双井','八通','国贸','宋家庄','酒仙桥']
        return dict

    def searchUrl(self,num=0):
        '''
        拼接get请求的url和传输的params
        :param num: 起始页面，默认为0
        :return: 返回请求时的url和传递的参数
        '''
        while(num >= 0):
            config = Douban().config()
            searchurl = config['url1']
            searchdata = {'start':num, 'cat': '1019', 'q': '北京租房'}      #cat=1019是直接通过豆瓣页面获取到
            return searchurl, searchdata

    def search(self):
        '''
        执行搜索动作，获取相应后的小组名称和url
        :return:
        '''
        urls = {}   # 定义一个字典存储BeautifulSoup处理后的豆瓣租房小组的标题和url
        config = Douban().config()

        for num in range (0, 220, 20):      #通过豆瓣页面查询到的，当start>200时，会跳转到登录页面了
            url, data = Douban().searchUrl(num)
            rSearch = requests.get(url, data, headers = config['headers'], cookies = config['cookie'])
            # 新增一个打印，调试时判断请求是否出现问题，比如被豆瓣封锁IP了
            print(rSearch)
            print(rSearch.text)
            # 增加请求间歇时间，防止被封IP
            sleep = config['sleep']
            time.sleep(sleep)

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
        print(urls)
        return urls

    def searchResult(self,title):
        '''
        将不符合规则的响应结果去除
        :return:
        '''
        config = Douban().config()
        str = config['city']
        strNos = config['notArea']

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
    # Douban().config()
    # Douban().searchUrl(0)
    # Douban().searchResult(title='北京')