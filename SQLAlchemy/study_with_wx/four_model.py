"""
sqlacodegen自动同步数据库中表生成model代码
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import Table

# 指定表，导出model
'''
cmd 命令行输入：
sqlacodegen mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test outfile=models.py
'''

# 例如：同步test.jlz_test表的数据，执行下面的命令
'''
sqlacodegen mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test --outfile=models_test_jlztest.py --tables jlz_test
--outfile 指定导出模块名称models_test_jlztest.py
--tables 指定导出的表名称，多个表用逗号隔开，不指定导出全部表
'''

# 使用autoload = True
'''
另一种方法，让模型代码跟数据库表字段关联起来，__table__中使用autoload = True 会自动加载model的Column,
使用这种方法时，在构建model之前，Base类要与engine进行绑定
'''

engine = create_engine('mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test')
Base = declarative_base()
metadata = Base.metadata
metadata.bind = engine

class JLZTestNew(Base):
    __table__ = Table("jlz_test", metadata, autoload=True)

# 上面这种方法，我们看不到代码里面表字段名称，一般不推荐用