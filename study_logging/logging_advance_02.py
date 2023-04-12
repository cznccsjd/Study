"""
配置日志记录样例02
一个简单的记录器、控制台处理器、简单的格式器
与01几乎相同，区别是对象的名称
"""
import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger('simpleExample')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('cirtical message')