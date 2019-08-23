#coding:utf-8

import unittest, time, configparser, os
from selenium import webdriver

# 登录的用户名
uname = 'disiqiao'

class SmartCrmMaidian():
    '''
    实现功能：
    1、SS看板-2019/08/15上线，点击各个卡片（如单个卡片下有多个tab页面，不再一一打开
    '''
    def setUp(self):
        ss = SmartCrmMaidian()
        dr = ss.login()

    def config(self):
        '''
        参数化，防止安全隐患
        :return:
        '''
        curdir = os.getcwd()
        if 'testCase' in curdir:
            pardir = os.path.dirname(curdir)
            conffile = os.path.join(pardir,'Conf','user')
        else:
            print(u'File Error: 未适配执行文件路径')

        conf = configparser.ConfigParser()
        conf.read(conffile)
        upass = conf.get('online',uname)

        if upass is not None:
            userpass = upass
        else:
            print('Error:username %s is not exist.' % uname)


    def login(self):
        # ss = SmartCrmMaidian()
        uname = 'disiqiao'
        upasswd = 'disiqiao2018'
        # upasswd =
        urlmain = 'http://crm.51talk.com/admin/admin_login.php'
        urlSSDashboard = 'http://smartcrm.51talk.com/SmartCrm/ss#/ss'

        dr = webdriver.Chrome()
        self.dr = dr
        self.dr.get(urlmain)
        self.dr.implicitly_wait(5)
        self.dr.maximize_window()
        self.dr.find_element_by_id("user_name").send_keys(uname)
        self.dr.find_element_by_id("pwd").send_keys(upasswd)
        self.dr.find_element_by_id("Submit").submit()
        self.dr.implicitly_wait(5)
        self.dr.get(urlSSDashboard)
        return self.dr

    def quite(self,driver):
        self.dr = driver
        self.dr.close
        print('本次用例执行完毕!', time.strftime('%H:%M:%S', time.localtime()))
        print('\n')

    def switchWindow(self, driver):
        '''
        获取当前打开的窗口，并关闭最后一个tab页面，将焦点返回第一个窗口
        :return:
        '''
        self.dr = driver
        windowHandles = self.dr.window_handles
        # 切换到新打开的页面，并关闭窗口
        self.dr.switch_to.window(windowHandles[-1])
        self.dr.close()
        time.sleep(1)
        self.dr.switch_to.window(windowHandles[0])

    def cardsIndex(self, type, num, driver):
        '''
        依次点击该模块下的卡片，打开新的页面
        :param nums:本模块下的卡片数
        :return:
        '''
        ss = SmartCrmMaidian()
        self.dr = driver
        for i in range (1, num+1):
            element = "div[%d]" % (i)
            if type == 'index':
                elements = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/' + element
                self.dr.find_element_by_xpath(elements).click()
                ss.switchWindow(self.dr)
            elif type == 'task':
                elements = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/' + element
                self.dr.find_element_by_xpath(elements).click()
                time.sleep(1)
                # 点击“销售管理系统”，返回首页
                self.dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/span[1]/span').click()
            elif type == 'basic':
                elements = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/' + element
                self.dr.find_element_by_xpath(elements).click()
                ss.switchWindow(self.dr)
            else:
                print('Error: None Exist type.')


    def test_common(self, driver):
        '''
        我的指标-常规
        :return:
        '''
        ss = SmartCrmMaidian()
        self.dr = driver
        common = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/h3/div/label[1]'
        self.dr.find_element_by_xpath(common).click()
        ss.cardsIndex('index', 8, self.dr)

    def test_basic(self, driver):
        '''
        我的指标-基本法
        :return:
        '''
        ss = SmartCrmMaidian()
        self.dr = driver
        # 点击我的指标-基本法
        basic = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/h3/div/label[2]'
        self.dr.find_element_by_xpath(basic).click()
        # 点击NCC续费率
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]').click()
        ss.switchWindow(self.dr)
        # 点击剩下的3个卡片
        ss.cardsIndex('basic', 3, self.dr)

    def test_performance(self, driver):
        '''
        任务围场-业绩
        :return:
        '''
        ss = SmartCrmMaidian()
        self.dr = driver
        # 点击任务围场-业绩
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/h3/div[1]/label[1]').click()
        # 点击8个卡片
        ss.cardsIndex('task', 8, self.dr)

    def test_service(self, driver):
        '''
        任务围场-服务
        :return:
        '''
        ss = SmartCrmMaidian()
        self.dr = driver
        # 点击任务围场-服务
        self.dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/h3/div[1]/label[2]').click()
        # 点击10个卡片
        ss.cardsIndex('task', 10, self.dr)

    def test_open(self, driver):
        '''
        测试网页打开是否正常
        :return:
        '''
        ss = SmartCrmMaidian()
        self.dr = driver
        ss.login()
        ss.quite()

    def testcase(self):
        '''
        测试用例
        :return:
        '''
        ss = SmartCrmMaidian()
        dr=ss.login()
        ss.test_common(dr)
        ss.test_basic(dr)
        ss.test_performance(dr)
        ss.test_service(dr)
        ss.quite(dr)

    def tearDown(self):
        ss = SmartCrmMaidian()
        ss.quite()


if __name__ == '__main__':
    ss = SmartCrmMaidian()
    # ss.test_open()
    # 脚本运行次数
    num = 8
    for i in range (1, num+1):
        print('第%d次执行用例,时间：%s' % (i,time.strftime('%H:%M:%S',time.localtime())))
        ss.testcase()
    # ss.config()