#!/usr/bin/env python
#coding:utf-8
"""
学习logging模块
"""
import logging
def log_basic():
    # CRITICAL 50; ERROR 40; WARNING 30; INFO 20: DEBUG 10; NOSET 0;
    logging.basicConfig(filename="test.log",level=0,
                        format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
    logging.critical('this is critical log')
    logging.debug("this is debug log")
    logging.info('this is info log')
    logging.warn('this is warn log')
    logging.error('this is error log')
    logging.fatal('this is fatal log')



if __name__ == '__main__':
    log_basic()