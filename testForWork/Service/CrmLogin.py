#utf-8
'''
crm登录，并返回登录后的cookie
'''

from selenium import webdriver
from testForWork.Common import DomainUrl
from testForWork.Common.transdata import Trans
import requests
import time

urlDefault = DomainUrl.Domainurl().url('crm')

class CrmLogin():
    def login(self):
        url = urlDefault + '/admin/admin_login.php'
        urlLogin = urlDefault + '/admin/login.php'
        urlTest = urlDefault + '/Channel/channelList'
        payload = {
            'user_name':'admin',
            'password':123456,
            'ref':'',
            'user_type':'admin',
            'Submit':'登 录'
        }
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
            'Referer': 'http://crm.51talk.com/admin/admin_login.php',
        }
        s = requests.Session()
        res = s.get(url)
        cookie = res.cookies.get_dict()
        resLogin = s.post(urlLogin,data=payload,headers=header)
        cookieLogin = resLogin.cookies
        print('这种形式的cookie也可以的，返回给其他端s就行了：', cookieLogin)
        # 测试cookie是否生效
        resJihui = s.get(urlTest)
        if u"机会分类配置" in resJihui.text:
            print(111)
            print('后续考虑，返回什么值？')


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