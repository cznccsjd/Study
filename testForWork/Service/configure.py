#coding:utf-8
'''
获取指定文件的配置信息
'''

import os, configparser

uname = 'disiqiao'

class Configure():
    def conf(self):
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
            return upass
        else:
            print('Error:username %s is not exist.' % uname)

    def test(self):
        file = 'CrmLogin.py'
        pardir = os.path.dirname(file)
        print('parent dir is : %s'% pardir)

if __name__ == '__main__':
    config = Configure()
    config.test()