#coding:utf-8
'''
执行爬虫文件
'''

from Spider import douban
import requests
from bs4 import BeautifulSoup
import time, datetime

class DoSearch():
    def __init__(self):
        #本脚本开始执行时间，方便需要时查看执行效率
        # doBeginTime = time.time()
        # print('Begin Time:', doBeginTime)
        self.douB = douban.Douban().search()
        self.configDouban = douban.Douban().config()
        pass

    def config(self):
        '''
        后续参数化
        :return:
        '''
        dict = {}
        dict['date'] = 5
        dict['headers'] = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        dict['sleep'] = 10
        # print(dict)
        return dict

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
            # 定义一个新的字典，存放单个组内，筛选出来的结果
            result = {}

            for num in range (0,10000,25):
                data = {'start': num}
                header = DoSearch().config()['headers']
                cookie = self.configDouban['cookie']
                res = requests.get(url,data, headers = header, cookies = cookie)
                # 增加request间隔时间，防止被封IP
                time.sleep(DoSearch().config()['sleep'])
                ########### 需要新增功能，如果帖子最新回复时间已经是5天前的了，整个num也不用循环了，直接跳出。所以需要一个新的方法，并且返回值
                soup = BeautifulSoup(res.text,"lxml")
                titles = soup.select('td.title > a')
                links = soup.select('td.title > a')
                times = soup.select('td.time')

                for title, link, time in zip(titles, links, times):
                    title = title.text
                    link = link.get('href')
                    time = time.text
                    preTime = DoSearch().time()
                    # 当前这条数据的时间在5天前，就不要了，并且终止后面的循环
                    if time < preTime:
                        break

                    # title中包含不需要地区的数据，直接去除，符合条件的可以存到Excel文件中
                    strNos = self.configDouban['notArea']
                    for strno in strNos:
                        if strno in title:
                            break
                        else:
                            num += 1
                        # 符合条件的存到Excel文件中
                        if num == len(strNos):
                            result[link] = title
                        else:
                            break


    def time(self):
        # 获取指定x天前时间
        day = DoSearch().config()['date']
        preday = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%m-%d %H:%M")
        return preday

if __name__ == '__main__':
    DoSearch().doDouBan()
    # DoSearch().time()
    # DoSearch().config()