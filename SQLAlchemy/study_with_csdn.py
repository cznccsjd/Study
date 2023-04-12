#coding:utf-8

"""
SQLAlchemy简明教程
https://blog.csdn.net/stone0823/article/details/112344065
"""

import tablib

#####################
# 建立与数据库的连接
#####################
# Engine Configuration:https://docs.sqlalchemy.org/en/14/core/engines.html
# create_engine()函数创建engine对象
from sqlalchemy import create_engine

from SQLAlchemy.study_with_csdn_ext import ModelExt

engine = create_engine("mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test")


#####################
# 建立映射关系
#####################
# 可以使用声明式映射，也可以使用命令式映射
# 命令式映射可以使用sqlacodegen自动生成model映射的代码，也可以在构建mode的时候，使用autoload=True，自动加载model的Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Table

Base = declarative_base()
metadata = Base.metadata
metadata.bind = engine

class User(Base, ModelExt):
    __table__ = Table("jlz_test",metadata,autoload=True)


#####################
# 单表 CRUD
#####################
# SQLALchemy操作数据库，需要引入另外一个对象 Session。Session 建立与数据库的会话 (conversation)，
# 可以将其想象成对象的容器，包含的对象叫 identity map 的结构，identity map 的作用就是保证对象的唯一性。另外，Session 对 Python 对象进行状态管理，
# 首先，需要构建一个 Session 对象，比较常用的方式是使用 sessionmaker() 函数来创建一个 global 的 Session Factory，进行调用后就生成 Session 对象：
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

#####################
# 查询记录

# 第一种方式，将model类作为参数传递给query()方法
def test_query_all():
    qry = session.query(User).filter(User.id=='100')
    # for user in qry.one():
    #     print(user)
    # print(qry)
    user = qry.one()
    print(user)
    print(type(user))

    print(to_formatted_table(user))

# 利用tablib将数据转换为格式化输出，方便查看
def to_formatted_table(tab_data):
    """
    tab_data is supposed to be of type list(dict)
    """
    ds = tablib.Dataset()
    return ds.load(str(tab_data))


test_query_all()