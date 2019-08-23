#coding:utf-8
'''
读取URL，防止代码上传GitHub后带来安全影响
'''

import configparser, os

class Domainurl():
    def url(self,domain,protocol='http'):
        '''
        返回获取的url地址
        :param domain: 需要选择的域名
        :return: 域名对应的URL
        '''
        if protocol == 'https':
            protocol = 'https://'
        else:
            protocol = 'http://'

        curdir = os.getcwd()
        if 'Conf' in curdir:
            conffile = os.path.join(curdir,'url.ini')
        elif 'Service' in curdir:
            pardir = os.path.dirname(curdir)
            conffile = os.path.join(pardir,'Conf','url.ini')
        else:
            print('Error:%s还没有适配，请在DomainUrl.py文件中进行适配！！！' % curdir)
        conf = configparser.ConfigParser()
        conf.read(conffile)
        crm = conf.get('domains','crm')
        tms = conf.get('domains','tms')
        www = conf.get('domains','www')

        if domain == 'www':
            return protocol + www
        elif domain == 'tms':
            return protocol + tms
        else:
            return protocol + crm


if __name__ == '__main__':
    Domainurl().url('crm')