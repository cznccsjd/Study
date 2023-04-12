"""
新增数据
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SQLAlchemy.study_with_wx.one_createDB import JlzTest

engine = create_engine('mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test')
# 把当前引擎绑定给这个会话
Session = sessionmaker(bind=engine)
# 实例化
session = Session()

# 创建一个jlztest对象
# jlztest_obj = JlzTest(name='test', result='test_by_sqlchemy')
# session.add(jlztest_obj)    # 添加到session
# session.commit()    # 提交到数据库


# 批量创建数据
session.add_all([
    JlzTest(name='test1', result='test_by_sqlchemy'),
    JlzTest(name='test2', result='test_by_sqlalchemy')
])
session.commit()