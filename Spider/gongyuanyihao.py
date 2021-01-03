#coding:utf-8
"""
融创公园壹号数据
"""
import requests, sys, time
from bs4 import BeautifulSoup
from Spider.buildings import Building

class YiHao:
    def __init__(self):
        self.B = Building()

    # 获取这个项目的概要信息，已经取得预售证的楼号以及每栋楼的url
    def get_summary(self):
        project_name = '融景四季雅苑'
        url = 'http://bjjs.zjw.beijing.gov.cn/eportal/ui?pageId=320801&projectID=6576027&systemID=2&srcId=1'
        self.B.verify_page_infos(url, project_name)


        pass

    # 获取这个项目已经取得预售证的每套房的信息
    def get_detail(self):
        pass

    # 获取签约信息
    def get_sign_contract(self):
        pass

if __name__ == '__main__':
    yihao = YiHao()
    print('脚本开始运行:', time.strftime('%H:%M:%S',time.localtime()))
    yihao.get_summary()

    print('脚本结束时间:', time.strftime('%H:%M:%S',time.localtime()))
