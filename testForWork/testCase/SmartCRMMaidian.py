#coding:utf-8
'''
自动点击卡片，生成埋点数据
'''

from selenium import webdriver
import time, unittest

urlmain = 'http://crm.51talk.com/admin/admin_login.php'
urlSSDashboard = 'http://smartcrm.51talk.com/SmartCrm/ss#/ss'
uname = 'disiqiao'
upasswd = 'disiqiao2018'

# 登录crm
dr = webdriver.Chrome()
dr.get(urlmain)
dr.implicitly_wait(5)
dr.find_element_by_id("user_name").send_keys(uname)
dr.find_element_by_id("pwd").send_keys(upasswd)
dr.find_element_by_id("Submit").submit()
dr.implicitly_wait(5)


# 打开SS看板
dr.get(urlSSDashboard)
dr.implicitly_wait(10)

# 点击卡片
num = 1
maxnum = 1
while (num < maxnum+1):
    # 我的指标-常规
    zhibiaos = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/h3/div/label[1]'
    dr.find_element_by_xpath(zhibiaos).click()

    for ii in range(1,9):
        div = "div[%d]"% ii
        divs = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/' + div
        dr.find_element_by_xpath(divs).click()
        windowHandles = dr.window_handles
        # windowHandle = dr.current_window_handle
        # print(windowHandle,windowHandles)
        # 切换到新打开的页面，并关闭窗口
        dr.switch_to.window(windowHandles[-1])
        dr.close()
        dr.switch_to.window(windowHandles[0])
    time.sleep(2)

    # 我的指标-基本法
    zhibiao = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/h3/div/label[2]'
    dr.find_element_by_xpath(zhibiao).click()
    # 点击NCC续费率
    dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[1]/div[1]').click()
    windowsHandles = dr.window_handles
    dr.switch_to.window(windowsHandles[-1])
    dr.close()
    dr.switch_to.window(windowsHandles[0])
    time.sleep(2)
    # 点击剩余3个卡片
    for iii in range (1,4):
        basic = "div[%d]" % iii
        basics = '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div/div[2]/' + basic
        dr.find_element_by_xpath(basics).click()
        windowsHandles = dr.window_handles
        dr.switch_to.window(windowsHandles[-1])
        dr.close()
        dr.switch_to.window(windowsHandles[0])
    time.sleep(2)

    # 任务围场-业绩
    dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/h3/div[1]/label[1]').click()
    for n in range (1,9):
        performance = 'div[%d]' % n
        performances = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/' + performance
        dr.find_element_by_xpath(performances).click()
        # 点击“销售管理系统”，返回首页
        dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/span[1]/span').click()


    # 任务围场-服务
    dr.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/h3/div[1]/label[2]').click()
    for n in range (1,9):
        service = 'div[%d]' % n
        services = '//*[@id="app"]/div/div[2]/div[2]/div/div[2]/div/div/div/' + service
        dr.find_element_by_xpath(services).click()
        # 点击“销售管理系统”，返回首页
        dr.find_element_by_xpath('//*[@id="app"]/div/div[1]/div[1]/div[2]/span[1]/span').click()
    time.sleep(2)


    num += 1



print('点击了%d次。'% (num-1))
dr.close()


