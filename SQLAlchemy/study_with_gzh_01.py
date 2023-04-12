#coding:utf-8
"""
1.环境准备与基础使用
https://mp.weixin.qq.com/s/zuxckrGmPDM7Oz44Mpr7Uw
"""

#########################
# 连接数据库示例
#########################

from sqlalchemy import create_engine

# 配置链接,连接数据库，需要使用到一些配置信息，组合成满足以下条件的字符串：
# dialect+driver://username:password@host:port/database

DB_URI = 'mysql+pymysql://root:123456@localhost:10086/test'
engine = create_engine(DB_URI)    #创建引擎
conn = engine.connect()     #创建连接

result = conn.execute('select * from user;')    # 执行sql
print(result.fetchall())
conn.close()        # 关闭连接


