"""
表之间一对一关系
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, ForeignKey, create_engine

'''
父表类中通过relationship()方法来引用子表的类集合
在子表类中通过 foreign key（外键）引用父表类
'''

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", uselist=False, backref='parent')
    # 在父表类中通过 relationship() 方法来引用子表的类集合

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    # 在子表类中通过 foreign key(外键)引用父表的参考字段

if __name__ == '__main__':
    DB_URI = 'mysql+pymysql://root:123456@localhost:10086/test'
    engine = create_engine(DB_URI)
    Base.metadata.create_all(engine)    # 将模型映射到数据库中