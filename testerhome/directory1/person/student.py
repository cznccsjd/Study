#coding:utf-8

from person import Person
class Student(Person):

    def __init__(self, name, sex, province, grade):
        super(Student,self).__init__(name,sex,province)     #super()方法继承父类
        # Person.__init__(self,name,sex,province)         #直接用Person类来继承
        self.grade = grade
        # self.name = 'i am not %s'% name

    def get_grade(self):
        return self.grade

    # 静态方法
    @staticmethod
    def set_name(newName):
        print '设置的新名字是',newName
        Person().newName = newName
        # return newName

    def get_name(self):
        """
        重写父类的方法，实际上就是多态
        :return:
        """
        print "i am class Student"
        print "Stundet方法中,name的名字",self.name


    def get_newName(self):
        print self.newName






if __name__ == "__main__":
    ss = Student("zhangs","male","hunan",3)
    # print ss.get_grade()
    # print ss.get_name()

    ss.set_name("hanmeimei")
    ss.get_newName()