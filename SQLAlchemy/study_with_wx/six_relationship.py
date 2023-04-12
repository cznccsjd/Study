"""
relationship之backref和back_populates参数
"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, ForeignKey

'''
relationship 函数是 sqlalchemy对关系之间提供的一种便利的调用方式, backref参数则对关系提供反向引用的声明。
在最新版本的sqlalchemy中对relationship引进了back_populates参数， 两个参数的效果完全一致。

backref 和 back_populates 两个参数的区别

backref 只需要在 Parent 类中声明 children，Child.parent 会被动态创建。

back_populates 必须在两个类中显式地使用 back_populates，更显繁琐，理解更直观
'''

# relationship使用
'''
relationship 函数是 sqlalchemy对关系之间提供的一种便利的调用方式, backref参数则对关系提供反向引用的声明。
'''
Base = declarative_base()
class Parent(Base):
    __tablename__ = 'parent'
    id = Column(Integer, primary_key=True)
    children = relationship("Child", uselist=False, backref='parent')
    # 在父表类中通过 relationship()方法来引用子表的类集合

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    # 在子表类中通过 foreign key(外键)引用父表的参考字段

'''
如上代码可以通过Parent.children 访问到Child 对象，那么如果得到了Child 对象，如何获取Parent对象呢？
这时候就通过backref参数反向引用到Parent 类。
'''