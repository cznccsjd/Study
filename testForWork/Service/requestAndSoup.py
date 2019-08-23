#!/usr/bin/env python3
#coding:utf-8

import requests, time
from bs4 import BeautifulSoup

class RequestAndSoup():
    def request(self, url, type='get', session=None, params=None, data=None, json=None, sleeptime=0, **kwargs):
        # 判断是否有Session，如果没有，新建一个
        if session == None:
            s = requests.Session()
        else:
            s = session

        if type == 'post':
            '''
            post方法有问题，需要详细了解下post用法
            '''
            try:
                # resp = requests.post(url, data, cookies, json, **kwargs)
                resp = s.post(url, data=None, json=None, **kwargs)
                time.sleep(sleeptime)
            except Exception as e:
                print("ERROR:%s" %e)
        else:
            try:
                # resp = requests.get(url, params, cookies, **kwargs)
                resp = s.get(url, **kwargs)
                time.sleep(sleeptime)
            except Exception as e:
                print("ERROR:%s" %e)
        return resp




    def soup(self):
        RequestAndSoup().request()
        pass

if __name__ == '__main__':
    pass