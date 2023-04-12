#coding:utf-8
"""
学习链接：https://mp.weixin.qq.com/s/zuxckrGmPDM7Oz44Mpr7Uw
创建ORM模型
"""
from sqlalchemy import Column, Date, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

# 拼接配置dialect + driver://username:passwor@host:port/database
DB_URI = 'mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test'
Base = declarative_base()

class JlzTest(Base):
    __tablename__ = 'jlz_test'    # 表名

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    result = Column(String(20))
    add_time = Column(Date())

    def __repr__(self):
        return "<Date(name='%s', result='%s'>" % (self.name, self.result)

if __name__ == '__main__':
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)