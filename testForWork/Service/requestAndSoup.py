#!/usr/bin/env python3
#coding:utf-8

import requests, time
from bs4 import BeautifulSoup

class RequestAndSoup():
    def request(self, url, type='get', cookies=None, params=None, data=None, json=None, sleeptime=0, **kwargs):
        # 关闭多余的连接
        s = requests.sessions.session()
        s.keep_alive = False

        if type == 'post':
            '''
            post方法有问题，需要详细了解下post用法
            '''
            try:
                resp = requests.post(url, data, cookies, json, **kwargs)
                time.sleep(sleeptime)
            except Exception as e:
                print("ERROR:%s" %e)
        else:
            try:
                resp = requests.get(url, params, cookies, **kwargs)
                time.sleep(sleeptime)
            except Exception as e:
                print("ERROR:%s" %e)
        return resp




    def soup(self):
        RequestAndSoup().request()
        pass

if __name__ == '__main__':
    pass