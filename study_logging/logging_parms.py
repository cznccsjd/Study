"""
记录变量数据
url:https://docs.python.org/zh-cn/3.9/howto/logging.html#logging-variable-data
"""
import logging

# logging.basicConfig(filename='myapp.log')
# # 记录变量数据
# logging.warning('%s before you %s', 'Lock', 'leap!')

# 更改显示消息的格式
# logging.basicConfig(format='%(levelname)s:%(message)s', filename='myapp.log', level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')

# 在消息中显示日期/时间
# logging.basicConfig(format='%(asctime)s %(message)s', filename='myapp.log')
# 更详细的控制日期/时间格式
logging.basicConfig(format='%(asctime)s %(message)s', filename='myapp.log', datefmt='%m/%d/%Y %I:%M:%S %p')
logging.warning('is when this event was logged.')