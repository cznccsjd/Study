#coding:utf-8
"""
由于python虚拟机是单线程（GIL）的原因，只有线程在执行I/O密集型的应用时才能更好地发挥Python的并发性（对比计算密集型应用，
它只需要做轮询），因此让我们看一个I/O密集型的例子，然后作为进一步的练习。尝试将其移植到Python3中，以让你对向Python3移植的处理
有一定认识。
"""

from atexit import register    #atexit.register()函数来告知脚本何时结束
from re import compile
from threading import Thread
from time import ctime, sleep
import requests

# str = "<title>Python数据科学手册 (豆瓣)</title>"
REGEX = compile('<title>.+</title>')
AMZN = 'https://book.douban.com/subject/'
ISBNs = {
    '3049219': '计算机',
    '4822685': '编码',
    '1148282': '计算机程序的构造和解释',
    '5333562': '深入理解计算机系统',
    '1230413': '深入理解计算机系统',
    '6855803': '奇点临近'
}

class OneThread():
    def get_ranking(self, isbn):
        url = AMZN + isbn
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
        page = requests.get(url, headers=header)
        data = page.text
        sleep(2)
        return REGEX.findall(data)[0]

    def _show_ranking(self, isbn):
        print("- %r full title is %s" %(ISBNs[isbn], self.get_ranking(isbn)))

    def _main(self):
        print("At %s on Douban..." %(ctime()))
        for isbn in ISBNs:
            # 单线程模式，直接顺序调用
            # print('*********单线程模式运行中：\n')
            # self._show_ranking(isbn)

            # 多线程模式，直接派生线程，然后立即启动线程
            print('*********多线程模式运行中：\n')
            Thread(target=self._show_ranking, args=(isbn,)).start()

    @register
    def _atexit():
        print("all DONE at:", ctime())

if __name__ == '__main__':
    # 没有采用多进程方案，其实还是单线程程序
    One = OneThread()
    One._main()