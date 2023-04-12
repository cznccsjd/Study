"""
表之间一对一关系，查询数据
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SQLAlchemy.study_with_wx.five_one import Card, CardDetail

DB_URI = 'mysql+pymysql://root:123456@localhost:10086/test'
engine = create_engine(DB_URI)

Session = sessionmaker(bind=engine)
session = Session()

r1 = session.query(Card).filter(Card.card_user == 'yoyo').first()
print(r1)

# 正向查询，主表查副表
print(r1.card_detail)
print(r1.card_detail.mail)
print('\n')

# 反向查询，通过副表查询主表
# 先查询关联表数据
r2 = session.query(CardDetail).filter(CardDetail.mail == '123@qq.com').first()
print(r2)
# 反向查询主表
print(r2.card)      # relationship通过backref='detail'属性关联到主表
print(r2.card.card_user)