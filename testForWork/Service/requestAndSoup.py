#!/usr/bin/env python3
#coding:utf-8

import requests
from bs4 import BeautifulSoup

class RequestAndSoup():
    def request(self, url, type='get', params=None, data=None, json=None, **kwargs):
        if type == 'post':
            res = requests.post(url, data, json, **kwargs)
        else:
            res = requests.get(url, params, **kwargs)


        pass

    def soup(self):
        pass

if __name__ == '__main__':
    pass