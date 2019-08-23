#coding:utf-8
'''
SS看板，测试各个卡片下的数据
'''

from testForWork.Common.db import DB
import unittest





where = 'ss_id = 6125 AND renew_money > 0'
orderby = 'renew_money'


ssTable = 'crmdata.dm_user_fact_clever_crm_ss_detail_new'
remarkTable = 'crm_log.remark_log'

class Test_renew(unittest.TestCase):
    def setUp(self):
        pass

    def test_renew_sql(self):
        '''
        续费业绩详情列表验证
        1、查询数据库，指定ss_id的续费业绩
        2、查询接口，指定ss_id的续费业绩
        3、比对两组数值
        :return:
        '''
        pass

    def tearDown(self):
        pass
