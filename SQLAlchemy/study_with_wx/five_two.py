"""
表之间一对一关系，添加数据
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SQLAlchemy.study_with_wx.five_one import Card, CardDetail

DB_URI = 'mysql+pymysql://root:123456@localhost:10086/test'
engine = create_engine(DB_URI)
# 把当前引擎绑定给这个会话
Session = sessionmaker(bind=engine)
# 实例化
session = Session()

card = Card(card_id='123454321',
            card_user='yoyo',
            tel='10086')
session.add(card)
session.flush()     # flush方法会生成Primary Key，得到card的id

detail = CardDetail(mail='123@qq.com',
                    city='上海市',
                    address='徐汇区',
                    card_id=card.id)
session.add(detail)
session.commit()    # 提交

