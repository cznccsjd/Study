#coding:utf-8
#!/usr/bin/env python

"""
管理用户名和密码的模拟陈登录数据系统；
管理用于登陆的用户信息：登录名字和密码。
登录用户账号建立后，已存在用户可以用登录名字和密码重返系统。新用户不能用别人的登录名建立用户账号
"""

db = {'zhangsan':'123456','lisi':'12345'}

def signup(uname):
    """
    注册
    :return: 
    """
    print"您尚未注册，即将为您注册！\n"
    password = raw_input("请输入注册密码：")
    db[uname] = password
    # print"当前用户库：", db


def signin(uname):
    """
    登录系统
    :return: 
    """
    # print"进入登录系统"
    password = raw_input("请输入密码：")
    if password == db[uname]:
        print "登录成功！"
    else:
        print "登录失败"


uname = raw_input("账号：")

if uname in sorted(db):
    signin(uname)
else:
    signup(uname)
