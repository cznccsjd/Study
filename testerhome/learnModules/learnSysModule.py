#!/usr/bin/env python
#coding:utf-8
"""
学习sys模块
"""
import sys
# • sys.path 返回当前PYTHONPATH的列表
print 'sys.path:',sys.path

# • sys.argv 获取命令行参数
# print 'sys.argv:',sys.argv[0]
# 这篇文章说的很透彻了，https://www.cnblogs.com/aland-1415/p/6613449.html

# • sys.exit 退出当前python进程


# • sys.platform 获取当前系统平台，如：win32、Linux等
print 'sys.platform当前平台是：',sys.platform

# • sys.stdin 标准输入流


# • sys.stdout 标准输出流

# • sys.stderr 标准错误流

'''
练习题
'''
# • 启动一个python脚本run.py, 传入参数为/home/tools/src, 把/home/tools/src加入到python path里面，打印出前后的pythopath列表信息。
# 如果此目录下没有任何py 文件，程序异常退出
# • 把上面的脚本出信息通过sys.stdout 重定向到log.txt

#!/usr/bin/env python
#coding:utf-8
"""
# • 启动一个python脚本run.py, 传入参数为/home/tools/src, 把/home/tools/src加入到python path里面，打印出前后的pythopath列表信息。
如果此目录下没有任何py 文件，程序异常退出
"""
import sys,os

def addPath():
    print 'src路径：\n'
    src = sys.stdin.readline()[:-1]

    #输出信息过sys.stdout 重定向到log.txt
    temp = sys.stdout   #先保存原始的stdout
    sys.stdout = open(r'D:\\logs.txt','w+')

    path1 = sys.path
    print 'sys.path：\n',path1
    if src in path1:
        print '%s已经在环境变量sys.path里面了\n' % src
    else:
        sys.path.append(src)
        print '%s添加后的环境变量sys.path：%s\n' %(src, sys.path)

    #当前目录没有py文件，退出
    count = 0
    for root, dirs, files in os.walk(src):
        for file in files:
            if file[-2:] == 'py':
                count += 1
    if count == 0:
        print '%s没有py文件，退出'% src
        sys.exit()

    sys.stdout = temp   #恢复映射关系，往文件写入log日志

if __name__ == '__main__':
    addPath()



