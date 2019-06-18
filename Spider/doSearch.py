#coding:utf-8
'''
执行爬虫文件
'''

import time, datetime, requests, os
from Spider import douban
from bs4 import BeautifulSoup
from openpyxl import Workbook

class DoSearch():
    def __init__(self):
        #本脚本开始执行时间，方便需要时查看执行效率
        # doBeginTime = time.time()
        # print('Begin Time:', doBeginTime)
        engine = douban.Douban()
        self.douB = engine.search()
        self.configDouban = engine.config

    @property
    def config(self):
        '''
        后续参数化
        :return:
        '''
        dict = {}
        dict['date'] = 5
        dict['headers'] = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        dict['sleep'] = 3
        # print(dict)
        return dict

    def doDouBan(self):
        '''
        从douban.py获取url，执行爬虫操作
        后续需要拆分出多个方法
        :return:
        '''
        # url = 'https://www.douban.com/group/beijingzufang/'       #调试用的url
        config = self.config

        # if url in self.douB.keys():         #配合调试url使用的
        #打开单个组，获取该组下所有有价值的单条url
        for url in self.douB.keys():
            url = url + 'discussion'
            # print(url)
            # 定义一个新的字典，存放单个组内，筛选出来的结果
            result = {}
            temprusult = {} #临时存放

            for num in range (0,200,25):
                data = {'start': num}
                header = config['headers']
                cookiea = self.configDouban['cookie']
                errorNum = 0

                # 关闭多余的连接
                s = requests.sessions.session()
                s.keep_alive = False
                try:
                    res = requests.get(url,data, headers = header, cookies = cookiea,timeout=10)
                except Exception as e:
                    errorNum += 1
                    print("第%d次报错，此时url：%s,原因：%s" %(errorNum,url,e))
                    continue
                # 增加request间隔时间，防止被封IP
                sleeptime = config['sleep']
                time.sleep(sleeptime)
                ########### 需要新增功能，如果帖子最新回复时间已经是5天前的了，整个num也不用循环了，直接跳出。所以需要一个新的方法，并且返回值
                soup = BeautifulSoup(res.text,"lxml")
                titles = soup.select('td.title > a')
                links = soup.select('td.title > a')
                times = soup.select('td.time')

                for title, link, atime in zip(titles, links, times):
                    title = title.text
                    link = link.get('href')
                    atime = atime.text
                    preTime = self.ftime

                    # 当前这条数据的时间在5天前，就不要了，并且终止后面的循环
                    if atime < preTime:
                        break

                    # title中包含不需要地区的数据，直接去除
                    # strNos = self.configDouban['notArea']
                    # i = 0
                    # for strno in strNos:
                    #     if strno in title:
                    #         break
                    #     else:
                    #         i += 1
                    #
                    # if i == len(strNos):
                    #     val = [title,atime]
                    #     result[link] = val
                    # 保留在指定区域的数据
                    strareas = self.configDouban['Area']
                    for strarea in strareas:
                        if strarea in title:
                            val = [title,atime]
                            result[link] = val



                else:
                    continue
                break




        print('单条数据获取成功:',result)

        wb = Workbook()
        ws = wb.active
        dir = os.getcwd()
        filetime = time.strftime('_%Y%m%d_%H%M%S', time.localtime())
        file = 'douban' + filetime + '.xlsx'

        # 绘制Excel表格
        ws.cell(row=1, column=1).value = '标题'
        ws.cell(row=1, column=2).value = 'URL'
        ws.cell(row=1, column=3).value = '价格'
        ws.cell(row=1, column=4).value = '地区'
        ws.cell(row=1, column=5).value = '户型'
        ws.cell(row=1, column=6).value = 'TEL'
        ws.cell(row=1, column=7).value = '微信'
        ws.cell(row=1, column=8).value = '最后更新时间'
        ws.cell(row=1, column=9).value = '来源'

        ws_max_row = ws.max_row
        ws_max_col = ws.max_column

        lines = len(dict)

        for line in lines:

            for dic in dict:
                # 往表格中输入数值
                ws.cell(row=line, column=1).value = dict[dic][0]
                ws.cell(row=line, column=8).value = dict[dic][1]
                ws.cell(row=line, column=2).value = dic

                print('单条数据写入成功\n')

        # 保存Excel（可以覆盖保存）
        wb.save(file)
        print('最终数据写入成功')





    @property
    def excel(self,dict):
        '''
        数据存储到Excel中
        :return:
        '''
        wb = Workbook()
        ws = wb.active
        dir = os.getcwd()
        filetime = time.strftime('_%Y%m%d_%H%M%S', time.localtime())
        file = 'douban' + filetime + '.xlsx'

        # 绘制Excel表格
        ws.cell(row=1, column=1).value = '标题'
        ws.cell(row=1, column=2).value = 'URL'
        ws.cell(row=1, column=3).value = '价格'
        ws.cell(row=1, column=4).value = '地区'
        ws.cell(row=1, column=5).value = '户型'
        ws.cell(row=1, column=6).value = 'TEL'
        ws.cell(row=1, column=7).value = '微信'
        ws.cell(row=1, column=8).value = '最后更新时间'
        ws.cell(row=1, column=9).value = '来源'

        ws_max_row = ws.max_row
        ws_max_col = ws.max_column

        lines = len(dict)

        for line in lines:

            for dic in dict:
                # 往表格中输入数值
                ws.cell(row=line,column=1).value = dict[dic][0]
                ws.cell(row=line,column=8).value = dict[dic][1]
                ws.cell(row=line,column=2).value = dic

                print('单条数据写入成功\n')

        # 保存Excel（可以覆盖保存）
        wb.save(file)
        print('最终数据写入成功')

    @property
    def ftime(self):
        # 获取指定x天前时间
        config = self.config
        day = config['date']
        preday = (datetime.datetime.now() - datetime.timedelta(days=day)).strftime("%m-%d %H:%M")
        return preday

if __name__ == '__main__':
    DoSearch().doDouBan()
    # DoSearch().ftime()
    # DoSearch().config()
    # DoSearch().excel()