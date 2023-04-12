"""
查询数据
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from SQLAlchemy.study_with_wx.one_createDB import JlzTest

engine = create_engine('mysql+pymysql://rd_user:NTHXDF7czYwi@172.16.70.20:3306/test')
# 把当前引擎绑定给这个会话
Session = sessionmaker(bind=engine)
# 实例化
session = Session()

# query()查询
r1 = session.query(JlzTest)
print('query()查询会转换成对应的SQL语句')
print(r1)
print('\n')

r2 = session.query(JlzTest.name)
print('query()可以查询某个字段，多个字段逗号隔开')
print(r2)
print('\n')

# all()查询全部数据
all = session.query(JlzTest).all()
print('all()查询全部的数据')
print(all)
for item in all:
    print(item.name, item.result, item.add_time)
print('\n')

# first()返回查询结果第一个数据
first = session.query(JlzTest).first()
print('first()返回查询结果第一个数据')
print(first)
print('\n')

# filter()筛选过滤
f1 = session.query(JlzTest).filter(JlzTest.name == 'test').first()
print('filter()筛选过滤')
print(f1)
print('\n')

# and和or多条件查询
f2 = session.query(JlzTest.result).filter(JlzTest.add_time >= '2023-03-01').all()
print('and和or多条件查询')
print(f2)
print('\n')

# order_by()排序
f3 = session.query(JlzTest).order_by(JlzTest.add_time.desc()).all()    # desc表示倒序
print('order_by()排序')
print(f3)
print('\n')

# like和in
# 判断等于和不等于可以直接用 == 和 !=
f4 = session.query(JlzTest.name).filter(JlzTest.name.like('%test%')).all()
print('like()模糊匹配')
print(f4)
print('in_()包含')
f5 = session.query(JlzTest.name).filter(JlzTest.name.in_(['test','test1'])).all()
print(f5)
print('\n')

# count()计算个数
f6 = session.query(JlzTest).count()
print('count()计算个数')
print(f6)
f7 = session.query(JlzTest).filter(JlzTest.name.like('%test%')).count()
print('name包含test的个数')
print(f7)
print('\n')

# 切片
# all()返回的是一个list，可以通过切片去一部分数据
f8 = session.query(JlzTest.result).all()[:2]
print(f8)
print('\n')

# delete()删除数据
# 根据查询结果，调用delete()方法删除对应数据，需要执行session.commit()提交事务
session.query(JlzTest).filter(JlzTest.name == 'test10086').delete()
session.commit()

# update()修改数据
# update()方法，需要执行session.commit()提交事务
session.add(JlzTest(name='test10086', result='this is a test message.'))
session.commit()
print('修改前的数据')
u1 = session.query(JlzTest).filter(JlzTest.name == 'test10086').all()
print(u1)
# 修改result
session.query(JlzTest).filter(JlzTest.name=='test10086').update({'result': '这是修改后的内容'})
# 查询修改后的数据
print('修改之后的数据')
u2 = session.query(JlzTest).filter(JlzTest.name == 'test10086').all()
print(u2)