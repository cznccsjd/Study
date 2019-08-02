#coding:utf-8

from testForWork.Service.requestAndSoup import RequestAndSoup
from testForWork.Service.CrmLogin import CrmLogin

class AddStudents():
    def checkMobile(self):
        # mobile = input('请输入手机号：')
        mobile = 19029999880
        url = 'http://crm.51talk.com/CrmUser/check_user_name'
        datas = {"user_name":str(mobile)+"@170.com"}
        cookie = CrmLogin().loginSe()
        result = RequestAndSoup().request(url, 'post', data=datas, cookies=cookie)
        print(result)

    def checkUsername(self):
        pass

    def addStu(self):
        pass

if __name__ == '__main__':
    AddStudents().checkMobile()