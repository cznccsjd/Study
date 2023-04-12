#coding:utf-8
"""
采用YAML格式，用于新的基于字典的方法
"""
import logging
import logging.config
import yaml

# 读取yaml文件，获取dict
with open('logging.yaml', 'r') as f:
    conf = yaml.safe_load(f)

# 注意，传递给dictConfig()的一定是一个dict，不然报错
logging.config.dictConfig(conf)

# create logger
logger = logging.getLogger('simpleExample2')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')