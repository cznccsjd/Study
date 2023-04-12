"""
表之间一对一关系，示例
ForeignKey 外键关联到父类id，父类名称用小写
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, ForeignKey, create_engine, String

Base = declarative_base()

class Card(Base):
    """银行卡基本信息"""
    __tablename__ = 'card'  # 数据库表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    card_id = Column(String(30))
    card_user = Column(String(10))
    tel = Column(String(30))
    card_detail = relationship("CardDetail",
                               uselist=False,
                               backref='card')

class CardDetail(Base):
    """银行卡 详细信息"""
    __tablename__ = 'carddetail'    # 数据库表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    mail = Column(String(30))
    city = Column(String(10))
    address = Column(String(30))
    card_id = Column(Integer, ForeignKey('card.id'))

if __name__ == '__main__':
    DB_URI = 'mysql+pymysql://root:123456@localhost:10086/test'
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)    # 将模型映射到数据库中