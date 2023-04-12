#coding:utf-8
"""
SQLAlchemy快速学习
"""

from sqlalchemy import create_engine, Column, DateTime, Integer, String, Text, TIMESTAMP, VARCHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()

# 定义User对象

class JlzTest(Base):
    # 表的名字
    __tablename__ = 'jlz_test'

    # 表的结构
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    result = Column(String(25))
    add_time = Column(DateTime)

# 初始化数据库连接
engine = create_engine('mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 创建session对象
session = DBSession()
# 创建查询,filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行
jlz_test = session.query(JlzTest).filter(JlzTest.id=='1').one()
print(jlz_test)
print(type(jlz_test))
print(jlz_test.result)
print(type(jlz_test.result))

# 创建新数据
new_jlz_test = JlzTest(id='50',name='max_mobile',result='19029995453')
# 添加到session
session.add(new_jlz_test)
# 提交保存到数据库
result = session.commit()
print(result)
# 关闭session
session.close()
