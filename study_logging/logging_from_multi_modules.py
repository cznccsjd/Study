"""
从多个模块记录日志
url:https://docs.python.org/zh-cn/3.9/howto/logging.html#logging-from-multiple-modules
"""
import logging
from study_logging import mylib


def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()