#coding:utf-8
'''
config.ini文件学习
'''
import os
import time
import configparser

# 第一步，创建conf对象
conf = configparser.ConfigParser()

# 第二步，添加section、options的值
conf.add_section("add")
conf.set("add","addFirst","./thisIsMyFirstAdd")     #option
conf.set("add","addSecond","SecondLines")

conf.add_section("study")
conf.set("study","add","this line is add by process")

# 第三步，写入文件
with open("config.ini","w") as conffile:
    conffile.write(conffile)
