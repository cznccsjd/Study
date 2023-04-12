#coding:utf-8

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class JlzTest(Base):
    __tablename__ = 'jlz_test'

