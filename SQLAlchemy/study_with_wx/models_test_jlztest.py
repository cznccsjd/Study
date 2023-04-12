# coding: utf-8
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import DATETIME, INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class JlzTest(Base):
    __tablename__ = 'jlz_test'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(25, 'utf8mb4_bin'))
    result = Column(String(30, 'utf8mb4_bin'))
    add_time = Column(DATETIME(fsp=6))
