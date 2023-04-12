"""
Column 对应表里面的每个字段
url:https://mp.weixin.qq.com/s?__biz=MzI5ODU1MzkwMA==&mid=2247490597&idx=1&sn=53270a63bdd0d520f56aa2e78df1f0fb&chksm=eca55b66dbd2d270b5e8d8fae133526e3e9817ffcb2b4265d45449e1fb0dba400c025e8bd7c6&scene=178&cur_album_id=2485908147048742913#rd
"""
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, create_engine

Base = declarative_base()

class UserCard(Base):
    """银行卡基本信息"""
    __tablename__ = 'usercard'      # 数据库表名

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    tel = Column(String(30), unique=True)
    age = Column(Integer, name="my_age", default=0)

    def __repr__(self):
        return f"<UserCard(id={self.id}, name={self.name}, " \
               f"tel={self.tel}, age={self.age})>"

if __name__ == '__main__':
    DB_URI = 'mysql+pymysql://root:123456@localhost:10086/test'
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)    # 将模型映射到数据库中