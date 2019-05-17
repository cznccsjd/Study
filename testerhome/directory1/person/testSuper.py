#coding:utf-8
"""
学习继承super()
注意，pause只能应用于新类，不能应用于经典类，如下面代码所示，class A 是经典类（继承object），class B/C均为新类，继承与class A
"""

class A(object):
    def go(self):
        print "Go A go!"

    def stop(self):
        print "Stop A stop!"

    def pause(self):
        print "Pause A pause!"

class B(A):
    def go(self):
        super(B, self).go()
        print "this is B go!"

class C(A):
    def stop(self):
        super(C,self).stop()
        print "this is C stop!"

    def go(self):
        super(C,self).go()
        print "this is C go!"

class D(B,C):
    def go(self):
        super(D,self).go()
        print "this is D go!"

    def stop(self):
        super(D,self).stop()
        print "this is D stop!"

    def pause(self):
        super(D,self).pause()
        print "this is D pause!"

if __name__ == '__main__':
    # A().pause()
    # B().go()
    # B().stop()
    # B().pause()
    # C().go()
    # C().stop()
    # C().pause()
    # D().go()
    # D().stop()
    D().pause()