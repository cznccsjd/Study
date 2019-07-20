#!/usr/bin/env python3
#coding:utf-8

import requests, time
from bs4 import BeautifulSoup

class RequestAndSoup():
    def request(self, url, type='get', params=None, data=None, json=None, sleeptime=0, **kwargs):
        # 关闭多余的连接
        s = requests.sessions.session()
        s.keep_alive = False

        if type == 'post':
            try:
                res = requests.post('post', url, data, json, **kwargs)
                time.sleep(sleeptime)
            except Exception as e:
                print("ERROR:%s" %e)
        else:
            try:
                res = requests.get(url, params, **kwargs)
                time.sleep(sleeptime)
            except Exception as e:
                print("ERROR:%s" %e)
        return res




    def soup(self):
        RequestAndSoup().request()
        pass

if __name__ == '__main__':
    pass