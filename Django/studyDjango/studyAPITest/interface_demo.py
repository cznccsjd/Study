#coding:utf-8
from zope.interface import Interface
from zope.interface.declarations import implementer

# 定义接口
class IHost(Interface):
    def goodmorning(self, host):
        """Say good morning to host"""

@implementer(IHost) #继承接口
class Host:
    def goodmoring(self, guest):
        """Say good morning to guest"""
        return "Good moring, %s!" % guest

if __name__ == '__main__':
    p = Host()
    hi = p.goodmoring('Tom')
    print(hi)