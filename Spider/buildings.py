#coding:utf-8
"""
获取楼盘信息的公共方法
"""
import requests, sys
from bs4 import BeautifulSoup

class Building:
    def verify_page_infos(self, url, project_name):
        req = requests.get(url)
        res = req.text

        soup = BeautifulSoup(res, 'html.parser')
        # 先确认是项目名称是否正确
        project_infos = soup.find('td', {'id':'项目名称'})
        if project_name not in project_infos.contents[0]:
            print("获取的不是%s项目" % project_name)
            sys.exit()

        # 判断楼盘表格是否存在
        building_title = soup.find('td', {'class':'font_title2'})
        if "楼盘表" not in building_title.contents[2]:
            print("没有获取到楼盘表信息")
            sys.exit()