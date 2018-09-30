#!/usr/bin/env python
#coding:utf-8
"""
学习commands和subprocess模块
"""
'''
commands 模块常用方法：Commands一般用在liunx
'''
import commands
# • commands.getoutput(command): 获取命令执行后的输出结果
# print 'commands.getoutput():\n',commands.getoutput('dir')

# • commands.getstatus(command)： 获取命令执行后的返回的状态码  """Return output of "ls -ld <file>" in a string."""
# print 'commands.getstatus():',commands.getstatus('os.py')

# • commands.getstatusoutput(command)：返回一个元组，第一个元素是状态码，第二个元素是输出结果
# print 'commands.getstatusoutput():',commands.getstatusoutput('dir')


'''
subprocess模块常用方法：可用在windows和Linux
'''
import subprocess
# • subprocess.call(command,shell=Ture): 执行windows下命令，返回执行执行状态结果
# a = subprocess.call("ipconfig")
# print 'subprocess.call():',a

# • Subprocess.check_call(command,shell=Ture): 执行windows下命令，返回执行执行状态结果
# b = subprocess.check_call("ipconfig")
# print 'subprocess.check_call():',b

# • Subprocess. check_output(command,shell=Ture): 返回执行命令后的输出
# c = subprocess.check_output("ipconfig")
# print 'subprocess.check_output():',c



"""
练习题
1. 通过windows 下ping命令， 得出www.testerhome.com 的服务器IP 地址
2. 通过python启动一个windows应用程序
3. 在Linux下启动tomcat进程，并判断tomcat启动是否成功
"""
import subprocess,time,commands
def one():
    """
    通过windows 下ping命令， 得出www.testerhome.com 的服务器IP 地址
    :return: 
    """
    ping = subprocess.check_output("ping www.testerhome.com")
    strL = "["
    strR = "]"
    indexL = ping.find(strL)
    indexR = ping.find(strR)
    print ping[indexL+1:indexR]


def two():
    """
    启动Foxmail客户端
    通过python启动一个windows应用程序,windows api插件可以判断进程是否启动成功
    :return: 
    """
    # call()需要写绝对路径，即便已经添加到path变量中了
    subprocess.call(r"D:\Program Files\Foxmail 7.2\Foxmail")
    time.sleep(3)
    # subprocess.call(r"taskkill /f /t /im Foxmail.exe")      #关闭进程，在cmd可以直接运行成功，Python中运行不成功

def three():
    """
    判断nignx进程是否存在，如果存在，kill它
    :return: 
    """
    status, pids = commands.getstatusoutput("ps aux|grep -w 'nginx'|grep -v grep|awk '{print $2}'")
    while status == 0:
        if len(pids) != 0:
            pids = pids.split(" ")
            for pid in pids:
                status = commands.getstatusoutput("kill " + pid)
        else:
            print 'nginx的进程不存在了'
        break

if __name__ == '__main__':
    # one()
    # two()
    three()