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
        req = requests.get(url)
        res = req.text

        soup = BeautifulSoup(res, 'html.parser')
        divs = soup.find_all('div', {'id':'Div_presellItemMortagageInfo'})
        sign_infos = divs[2].text

        if "期房签约统计" not in sign_infos:
            print("目前没有期房签约统计数据了，排查下官网吧")
            return False

        info_tmps = sign_infos.split('住宅')[1]
        info_tmp = info_tmps.split('本网站')[0]

        if "丙类储藏间" in info_tmp:
            info_houses = info_tmp.split('丙类储藏间')[0]
            info_stores = info_tmp.split('丙类储藏间')[1]

            houses = info_houses.split('\n')
            stores = info_stores.split('\n')

            # 住宅已签约套数
            sign_houses_num_total = houses[1]
            # 住宅已签约面积
            sign_houses_area_total = houses[2]
            # 住宅成交均价
            sign_houses_price_avg = houses[3]
            # 丙类储物间已签约套数
            sign_stores_num_total = stores[1]
            # 丙类储物间已签约面积
            sign_stores_area_total = stores[2]
            # 丙类储物间成交均价
            sign_stores_price_avg = stores[3]

        return [sign_houses_num_total, sign_houses_area_total, sign_houses_price_avg, sign_stores_num_total, sign_stores_area_total, sign_stores_price_avg]

if __name__ == '__main__':
    yihao = YiHao()
    print('脚本开始运行:', time.strftime('%H:%M:%S',time.localtime()))
    # yihao.get_summary()
    print(yihao.get_sign_contract())
    print('脚本结束时间:', time.strftime('%H:%M:%S',time.localtime()))
