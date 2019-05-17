#coding:utf-8
from student import Student

class HighStudent(Student):
    def __init__(self, name, sex, province, grade):
        super(HighStudent,self).__init__(name,sex,province,grade)

    def get_new_name(self):
        pass

if __name__ == "__main__":
    hs = HighStudent("lisi", "man", "hebei",grade=3)
    print hs.get_name()