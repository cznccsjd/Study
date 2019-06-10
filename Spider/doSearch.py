#coding:utf-8
'''
执行爬虫文件
'''

from Spider import douban
import requests
from bs4 import BeautifulSoup
import time

#浏览器的User—Agent标识
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

class DoSearch():
    def __init__(self):
        self.douB = douban.Douban().search()

    def doDouBan(self):
        '''
        从douban.py获取url，执行爬虫操作
        :return:
        '''
        url = 'https://www.douban.com/group/beijingzufang/'
        if url in self.douB.keys():
        #打开单个组，获取该组下所有有价值的单条url
        # for url in self.douB.keys():
            url = url + 'discussion'
            # print(url)
            for num in range (0,10000,25):
                data = {'start': num}
                res = requests.get(url,data, headers = header)

                soup = BeautifulSoup(res.text,"lxml")
                titles = soup.select('td.title > a')
                links = soup.select('td.title > a')
                times = soup.select('td.time')
                ######对获取的最后更新时间与当前时间进行比对，超过5天的数据，就不要再继续请求了，没有时效性了，继续写
                print(times)

                for title, link, time in zip(titles, links, times):
                    title = title.text
                    link = link.get('href')
                    time = time.text
                    print(time)
                    # print('now:',now())


if __name__ == '__main__':
    DoSearch().doDouBan()