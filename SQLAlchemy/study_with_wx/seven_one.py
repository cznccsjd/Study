"""
新增数据
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SQLAlchemy.study_with_wx.seven_column import UserCard

engine = create_engine('mysql+pymysql://root:123456@localhost:10086/test')
Session = sessionmaker(bind=engine)
session = Session()

# 如果name不传，报错 sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) (1048, "Column 'name' cannot be null")
# obj = UserCard(tel='10086', age=20)

# name传空，也会抛出异常，呀，为什么提交成功了，不是不能为null吗
# obj = UserCard(name='', tel='10086', age=20)

# 正常添加数据
# obj = UserCard(name='yoyo', tel='100861', age=20)

# tel不唯一的时候，报错 sqlalchemy.exc.IntegrityError: (pymysql.err.IntegrityError) (1062, "Duplicate entry '10086' for key 'usercard.tel'")
# obj = UserCard(name='yoyoyo', tel='10086', age=20)

# age不传递，默认为0
obj = UserCard(name='yo', tel='10010')
session.add(obj)
session.commit()