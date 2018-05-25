#coding:utf-8
"""
从互联网上抓取一个web页面并暂时存储到一个本地文件中用户分析的简单脚本。
这类程序能用来测试web站点页面的完整性或者能监测一个服务器的负载（通过测量可链接性或者下载速度）
process()函数可以做我们想要的任何事，表现出无限种用途。
我们为这个练习选择的用法是显示从web页面上获取的第一和最后的非空格行。（现实中这个特别的例子没多少用处，只是利用这段代码举一反三）
这段脚本下载了一个web页面（默认为本地的万维网服务器）并显示了HTML文件的第一个以及最后一个非空格行。由于download()函数的双默认参数允许用不同的urls或者指定不同的处理函数来进行覆盖，灵活性得到了提高

hahahaahhaha，没看明白这个代码是干嘛的！！！
"""
#!/usr/bin/env python

from urllib import urlretrieve

def firstNonBlank(lines):
    for eachLine in lines:
        if not eachLine.strip():
            continue
        else:
            return eachLine

def firstLast(webpage):
    f = open(webpage)
    lines = f.readlines()
    f.close()
    print firstNonBlank(lines)
    lines.reverse()
    print firstNonBlank(lines)

def download(url = 'http://www', process = firstLast):
    try:
        retval = urlretrieve(url)[0]
    except IOError:
        retval = None
    if retval:  #do some processing
        process(retval)

if __name__ == '__main__':
    download("crm.51talk.com")