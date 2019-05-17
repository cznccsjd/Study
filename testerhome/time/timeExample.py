#coding:utf-8

import time

def time_format():
    print time.time()
    print time.localtime()
    print time.gmtime()
    print time.strftime("%y/%m/%d %H:%M")
    # print time.strptime()
    # print time.mktime()
    # print


if __name__ == '__main__':
    time_format()