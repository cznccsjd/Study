#coding:utf-8
'''
执行豆瓣爬虫文件
'''
import time, datetime, requests, os,re
from Study.Spider import douban
from bs4 import BeautifulSoup
from openpyxl import Workbook

class DoSearch():
    def __init__(self):
        #本脚本开始执行时间，方便需要时查看执行效率
        print('脚本开始运行:', time.strftime('%H:%M:%S',time.localtime()))
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
        dict['sleep'] = 1
        return dict

    def doDouBan(self):
        '''
        从douban.py获取url，执行爬虫操作
        后续需要拆分出多个方法
        :return:
        '''
        config = self.config
        errorNum = 0
        sleeptime = config['sleep']
        wantedAreas = self.configDouban['Area']
        preTime = self.ftime
        wantedAreasStr = ''
        for wantedArea in wantedAreas:
            wantedAreasStr += wantedArea
            wantedAreasStr += '|'
        wantedAreasStr = wantedAreasStr[:-1]  # 去掉末尾的|

        # excel相关操作
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
        ws.cell(row=1, column=5).value = '最后更新时间'
        ws.cell(row=1, column=6).value = '来源'
        ws.cell(row=1, column=7).value = '微信'
        ws.cell(row=1, column=8).value = 'TEL'
        ws.cell(row=1, column=9).value = '户型'

        #打开单个组，获取该组下所有有价值的单条url
        for url in self.douB.keys():
            urlnew = url + 'discussion'
            pagetitle = self.douB[url]

            for num in range (0,2000,25):       #设置2000，最多获取1975页
                data = {'start': num}
                header = config['headers']
                cookiea = self.configDouban['cookie']
                # 关闭多余的连接
                s = requests.sessions.session()
                s.keep_alive = False
                try:
                    res = requests.get(urlnew,data, headers = header, cookies = cookiea,timeout=10)
                    # 增加request间隔时间，防止被封IP
                    time.sleep(sleeptime)
                except Exception as e:
                    errorNum += 1
                    print("%s,第%d次报错，url：%s,原因：%s" %(time.strftime('%H:%M:%S',time.localtime()),errorNum,urlnew,e))
                    continue

                soup = BeautifulSoup(res.text,"lxml")
                titles = soup.select('td.title > a')
                links = soup.select('td.title > a')
                times = soup.select('td.time')

                for title, link, atime in zip(titles, links, times):
                    title = title.text
                    link = link.get('href')
                    atime = atime.text
                    # 当前这条数据的时间在5天前，就不要了，并且终止后面的循环(for else)
                    if atime < preTime:
                        break
                    # 通过标题查找符合要求的地区
                    filterPagetitle = re.search(wantedAreasStr, title)
                    if filterPagetitle is None:
                        continue
                    # 标题含有已租、限女的，也要去除
                    filterPagetitlesex = re.search('已租|限女|长期有效', title)
                    if filterPagetitlesex is not None:
                        continue
                    # 打开具体某一条招租信息
                    try:
                        s = requests.sessions.session()
                        s.keep_alive = False
                        rs = requests.get(link, headers=header, cookies=cookiea, timeout=10)
                        # 增加request间隔时间，防止被封IP
                        time.sleep(sleeptime)
                    except Exception as e:
                        errorNum += 1
                        print("%s,第%d次报错，url：%s,原因：%s" % (
                            time.strftime('%H:%M:%S', time.localtime()), errorNum, link, e))
                        continue
                    soup = BeautifulSoup(rs.text, "lxml")

                    if '...' in title:
                        stitle1 = soup.select('td.tablecc')
                        stitle2 = str(stitle1)
                        stitle = stitle2[41:-6]
                    else:
                        stitle = title

                    contexts = soup.select('div.topic-richtext')
                    context = str(contexts)
                    conIndexsBegin = context.find('<p>')
                    conIndexsEnd = context.find('</p><div class="image-container image-float-center">')
                    context = context[conIndexsBegin:conIndexsEnd + 1]

                    if context == '':
                        continue
                    # 正则表达式，筛选出金额
                    patMoney = '[\D][\d]{4}[\D]'
                    # patTel = '[\D]?[\d]{11}[\D]?'
                    # patWe = '[微信]|[wechat]'
                    moneyTitle = re.findall(patMoney, stitle)
                    moneyContext = re.findall(patMoney, context)
                    smoney1 = moneyTitle + moneyContext
                    smoney2 = str(smoney1)        #openpyxl将str写入一个单元格
                    smoney = re.sub("[|]|'","",smoney2)
                    # stel = re.search(patTel,context)
                    # swechat = re.search(patWe,context)

                    ws_max_row = ws.max_row
                    ws_max_col = ws.max_column
                    ws.cell(row=ws_max_row+1, column=1).value = stitle.strip()
                    ws.cell(row=ws_max_row+1, column=5).value = atime
                    ws.cell(row=ws_max_row+1, column=2).value = link
                    ws.cell(row=ws_max_row+1, column=6).value = pagetitle
                    ws.cell(row=ws_max_row+1, column=3).value = smoney
                    continue

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
                    #     ws_max_row = ws.max_row
                    #     ws_max_col = ws.max_column
                    #     ws.cell(row=ws_max_row + 1, column=1).value = title.strip()
                    #     ws.cell(row=ws_max_row + 1, column=5).value = atime
                    #     ws.cell(row=ws_max_row + 1, column=2).value = link

                    # 保留在指定区域的数据，下面的筛选用正则表达式替换了
                    # strareas = self.configDouban['Area']
                    # for strarea in strareas:
                    #     if strarea in title:
                    #         try:
                    #             rs = requests.get(link,headers=header, cookies=cookiea, timeout=10)
                    #             # 增加request间隔时间，防止被封IP
                    #             time.sleep(sleeptime)
                    #         except Exception as e:
                    #             errorNum += 1
                    #             print("%s,第%d次报错，url：%s,原因：%s" % (
                    #             time.strftime('%H:%M:%S', time.localtime()), errorNum, link, e))
                    #             continue
                    #
                    #         soup = BeautifulSoup(rs.text, "lxml")
                    #         stitle = soup.select('#content > h1')
                    #         links = soup.select('td.title > a')
                    #         times = soup.select('td.time')
                    #
                    #         ws_max_row = ws.max_row
                    #         ws_max_col = ws.max_column
                    #         ws.cell(row=ws_max_row+1, column=1).value = title.strip()
                    #         ws.cell(row=ws_max_row+1, column=5).value = atime
                    #         ws.cell(row=ws_max_row+1, column=2).value = link
                    #         ws.cell(row=ws_max_col+1, column=6).value = pagetitle
                    #         continue
                else:
                    continue
                break

        # 保存Excel（可以覆盖保存）
        wb.save(file)
        print('最终excel数据写入成功：',time.strftime('%H:%M:%S',time.localtime()))
        print('文件名：',file)

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