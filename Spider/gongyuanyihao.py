#coding:utf-8
"""
融创公园壹号数据
"""
import re, requests, sys, time
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

    def get_sign_contract(self):
        '''
        获取签约信息
        :return: [住宅已签约套数,住宅已签约面积,住宅成交均价,丙类储物间已签约套数,丙类储物间已签约面积,丙类储物间成交均价]
        '''
        url = 'http://bjjs.zjw.beijing.gov.cn/eportal/ui?pageId=320801&projectID=6576027&systemID=2&srcId=1'
        print("融创公园壹号截止至今日的销售数据为:\n")
        ret = self.B.get_sign_contract_infos(url)
        if ret:
            print(ret)

if __name__ == '__main__':
    yihao = YiHao()
    print('脚本开始运行:', time.strftime('%H:%M:%S',time.localtime()))
    # yihao.get_summary()
    yihao.get_sign_contract()
    print('脚本结束时间:', time.strftime('%H:%M:%S',time.localtime()))
