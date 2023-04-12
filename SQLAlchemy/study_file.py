#coding:utf-8
"""
学习教程：https://blog.csdn.net/stone0823/article/details/112344065
"""
import sqlacodegen
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base

# create_engine()创建engine对象，这里使用pymysql驱动连接到mysql
engine = create_engine("mysql+pymysql://rd_user:123456@localhosts:10086/test?charset=utf-8")
Base = declarative_base()

'''
数据库与 Python 对象的映射主要在体现三个方面：

数据库表 (table）映射为 Python 的类 (class)，称为 model
表的字段 (field) 映射为 Column
表的记录 (record）以类的实例 (instance) 来表示
'''

# 声明式映射（Declarative Mapping)
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 以上代码的作用是：通过 declarative_base() 函数创建 Base 类，Base 类本质上是 一个 registry 对象，Base 作为所有 model 类的父类，将在子类中把声明式映射过程作用于其子类。

# 不需要声明的两种方式
# 方式一：sqlacodegen
# 将数据库中所有表导出为mode
sqlacodegen('mysql+pymysql://root:123456@localhost:10086/test?charset=utf-8')