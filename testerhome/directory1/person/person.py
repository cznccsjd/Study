#coding:utf-8

class Person(object):

    total_person = 0
    def __init__(self, name, sex, province):
        print "Init the class"
        self.name = name
        self.sex = sex
        self.province = province
        Person.total_person += 1

    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex

    