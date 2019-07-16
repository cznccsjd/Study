#!/usr/bin/env python3
#coding:utf-8

'''
检查老师training时，Medium的province和city对应关系是否正确
'''

import requests, time, pymysql
from bs4 import BeautifulSoup
from Study.Spider.douban import Douban

url = 'http://tms.51talk.com/training/traing_medium'
url_ajax = 'http://tms.51talk.com/training/ajax_get_city'
cookie = 'rmbUser=false; PHPSESSID=j2narg0cslv931kbqu8p4sv374; price_show_type=1; SpMLdaPx_uuid=802127918; __zlcmid=tIiO2xBnJdXz9S; _ga=GA1.2.289154381.1563169869; _gid=GA1.2.1342815520.1563169869; uuid=a4fc5c8a-fab3-4a5f-a603-3527538c00c8; www_ugroup=4; user_ust=I%2B0RRTZM5GktIrPO%2Bp5ipiySaWuM2ZnnfiT7iPFm0sTA1X%2BWU%2FTEVkDvRubSmK2RWNS6O82iq7dOSDDXnNcKgZzTwcPSRy4mSk2U81E%3D; user_usg=MC4CFQDRPprTOVDfspTzrq0ftIrIBxrsWAIVANH1slb35tuCtOUuFHocAQjrFBn4; ust_v=1; from_url=tms.51talk.com%2Cmypage.51talk.com%2Ccrm.51talk.com%2Clogin.51talk.com; Hm_lvt_cd5cd03181b14b3269f31c9cc8fe277f=1563173913; Hm_lpvt_cd5cd03181b14b3269f31c9cc8fe277f=1563174277; SpMLdaPx_poid=19; tms_training_sso=dGVhY2hlcklkPTEmZW1haWw9YWRtaW4%3D.21DDFE185D5C62EF230A8EB93EC06A5F; SpMLdaPx_pvid=1563188419843'
cookiedict = Douban().dict(cookie, sign1=';', sign2='=')
pros = []
pagecities = []




res = requests.get(url, cookies=cookiedict)
soup = BeautifulSoup(res.text,'lxml')
provinces = soup.select('span.province_td')
province_ids = soup.select('span.province_td')
province_pids = soup.select('span.province_td')

conn = pymysql.connect(host="172.16.70.20",user="rd_user",password="NTHXDF7czYwi",port=3306,database='teanew')
cur = conn.cursor()
cur.execute("SELECT name FROM teanew.cfg_ph_city WHERE type = 'province';")
sqlpros = cur.fetchall()



# 获取页面province信息
for province,province_id, province_pid in zip(provinces,province_ids, province_pids):
    sqlcities = []
    pro = province.text
    pros.append(pro)
    pro_id = province_id.get('province_id')
    pro_pid = province_pid.get('province_pid')
    # 通过province获取city信息
    date = {'province_id':pro_id,'province_pid':pro_pid}

    ajaxres = requests.post(url_ajax,date,cookies=cookiedict)
    provincedate = ajaxres.json()['data']
    # 防止触发防刷新
    time.sleep(3)
    while(provincedate['province_name'] == pro):
        citydates = provincedate['city_info']

        for i in range (0,len(citydates)):
            city = citydates[i]['name']
            pagecities.append(city)

        # 数据库获取city数据
        sql1 = "SELECT id FROM teanew.cfg_ph_city WHERE name = '%s';" % pro
        cur.execute(sql1)
        sqlpid = cur.fetchall()
        sqlpid = sqlpid[0][0]
        sql2 = "SELECT name FROM teanew.cfg_ph_city WHERE pid = %d ;" % sqlpid
        cur.execute(sql2)
        sqlcity = cur.fetchall()
        lensqlcity1 = len(sqlcity)
        sqlcity = set(sqlcity)
        lensqlcity2 = len(sqlcity)

        lenpagecity1 = len(pagecities)
        pagecity = set(pagecities)
        lenpagecity2 = len(pagecity)

        if lensqlcity1 != lensqlcity2:
            print('ERROR：数据库存储的city数据(%s)有重复，请及时调整！！！' %pro)
        elif lenpagecity1 != lenpagecity2:
            print('BUG：页面展示的city数据(%s)有重复，请跟进！！！'%pro)
        elif len(sqlcity ^ pagecity) == 0:
            print(sqlcity)
            print(pagecity)
            print('PASS：city(%s)测试通过！！！'%pro)
        elif len(sqlcity ^ pagecity) != 0:
            print(sqlcity)
            print(pagecity)
            print(sqlcity ^ pagecity)
            print('BUG：city(%s)，(页面数据与数据库不一致，请跟进！！！'%pro)
        else:
            print('ERROR：city(%s)测试出现未知问题，请排查！！！'%pro)
        break





lensql1 = len(sqlpros)
sqlpros = set(sqlpros)
lensql2 = len(sqlpros)
lenpage1 = len(pros)
pagepros = set(pros)
lenpage2 = len(pagepros)

# 通过转换成set集合前后的长度判断province是否有Bug
if lensql1 != lensql2:
    print('ERROR：数据库存储的province信息有重复，请及时调整！！！')
elif lenpage1 != lenpage2:
    print('Bug：页面展示的province信息有重复，请跟进！！！')
elif len(sqlpros ^ pagepros) == 0:
    print('PASS：province测试通过')
elif len(sqlpros ^ pagepros) != 0:
    print('BUG：province，页面数据与数据库不一致，请跟进！！！')
else:
    print('ERROR：province测试出现未知问题，请排查！！！')


cur.close()
conn.close()

