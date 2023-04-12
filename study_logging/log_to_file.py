#coding:utf-8
"""
记录日志到文件，url：https://docs.python.org/zh-cn/3/howto/logging.html#logging-to-a-file
"""
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')

