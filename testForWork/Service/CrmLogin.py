#utf-8
'''
crm登录，并返回登录后的cookie
'''

from selenium import webdriver
from testForWork.Common import DomainUrl
import requests
import time

urlDefault = DomainUrl.Domainurl().url('crm')

class CrmLogin():
    def login(self):
        url = urlDefault + '/admin/admin_login.php'
        urlLogin = urlDefault + '/admin/login.php'
        payload = {'user_name':'admin','password':123456}
        res = requests.get(url)
        cookie = res.cookies
        print(cookie)
        header = {
            'Cookie':1
        }

        resLogin = requests.post(url,data=payload,headers=header)
        print(resLogin)

        pass

    def loginSe(self, uname='admin', upasswd='123456'):
        '''
        通过Selenium登录后台，返回cookie
        :param uname: 登录后台的用户名，默认admin
        :param upasswd: 登录后台的密码，默认123456
        :return: 返回登录后获取的cookie
        '''
        dr = webdriver.Chrome()
        url = urlDefault +'/admin/admin_login.php'
        dr.get(url)
        dr.implicitly_wait(5)
        dr.find_element_by_id("user_name").send_keys(uname)
        dr.find_element_by_id("pwd").send_keys(upasswd)
        dr.find_element_by_id("Submit").submit()
        dr.implicitly_wait(5)

        cookie = dr.get_cookie("PHPSESSID")
        cname = cookie['name']
        cvalue = cookie['value']
        cookies = {}
        cookies[cname] = cvalue
        dr.close()
        print('%s登录成功后的cookie：%s' % (uname, cookies))
        return cookies



if __name__ == '__main__':
    # CrmLogin().loginSe()
    CrmLogin().login()