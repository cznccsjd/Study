#!/usr/bin/env python
#coding:utf-8
"""
学习logging模块
"""
import logging
from logging.handlers import RotatingFileHandler

def log_basic():
    # CRITICAL 50; ERROR 40; WARNING 30; INFO 20: DEBUG 10; NOSET 0;
    logging.basicConfig(filename="test.log",level=50,
                        format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    logging.critical('this is critical log')
    logging.debug("this is debug log")
    logging.info('this is info log')
    logging.warn('this is warn log')
    logging.error('this is error log')
    logging.fatal('this is fatal log')
    # 定义RotatingFileHandler,日志文件大小超过5KB时进行旋转，最大5个备份日志文件
    # RotatingFileHandler('back.log',maxBytes=1024*1,mode='a',backupCount=2)
    #
    logging.getLogger("yayaay").setLevel(logging.ERROR)
# def



if __name__ == '__main__':
    log_basic()