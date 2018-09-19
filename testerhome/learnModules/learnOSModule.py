#!/usr/bin/env python
#coding:utf-8
"""
学习OS模块
"""
import os
# os.listdir():返回指定目录下的所有文件和目录名，不包括子目录
print '\nos.listdir()：\n',os.listdir('/home/13220164847')

# os.getcwd(): 返回当前Python进程正在工作的目录
print 'os.getcwd()：',os.getcwd()

# • os.stat（file）:获得文件属性，文件大小，创建时间，最后访问时间等
print 'os.stat("learnOSModule.py"):',os.stat('learnOSModule.py')

# • os.removedirs（“/home/test/”）:删除多个目录
os.mkdir ('/home/13220164847/test_rm')
os.removedirs('/home/13220164847/test_rm')

# • os.system():运行shell命令
os.system('ls -al')

# • os.path.join(path,name):连接目录与文件名或目录

# • os.mkdir(name):创建目录
os.mkdir ('/home/13220164847/test_rm')

# • os.path.basename(path):返回文件名
os.path.basename('/home/13220164847')

#文件、目录遍历器
for root, dirs, files in os.walk('/logs'):      #遍历/logs文件夹
    for subDirName in dirs:     #循环遍历子文件夹名称（不包含子目录【这句话不懂什么意思】）
        print 'subDirs:',(os.path.join(root,subDirName))
    for subFile in files:       #循环遍历该文件夹（root）中所有文件的名称（不包含子目录【这句话不懂什么意思】）
        print 'subFiles:', subFile
print 'root:', root     #当前正在遍历的文件夹本身的地址


'''
练习题
'''
# • 查找/tomcat/log/ 目录下的log文件，如果文件最后修改时间是在1小时之前，把次文件打包压缩，备份到/home/back/log 目录下
"""
实现的功能：
1、找到/logs/nginxlogs目录下所有的log文件；
2、如果文件最后修改的时间是1小时之前，把文件打包，备份到/tmp/jlz/cptest路径下
"""
import os,time

for root, dirs, files in os.walk('/logs/nginxlogs'):
    for file in files:
        ab = os.path.join(root,file)
        #如果文件名包含log字样，就认定为log文件，肯定不严谨，需要怎么判断呢？？？？
        if "log" in file:
            if os.stat(ab).st_mtime <= time.time() - 3600:
                os.system("tar -zcvf "+ab+".tar.gz "+ab)
                os.system("cp "+ab+".tar.gz"+" /tmp/jlz/cptest")



# • 在Linux下每隔1分钟检查一下tomcat进程是不是在运行，如果tomcat进程退出了，立即启动tomcat进程




# • 搜索目录/home/tools/下所有已test开头，py结尾的文件(包括子目录的), 把文件全路径输出到一个列表里面打印出来