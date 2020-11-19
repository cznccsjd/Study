#coding:utf-8

import time
from datetime import timedelta
from datetime import date

# 下面的例子演示了如何对 days, seconds 和 microseconds 以外的任意参数执行“合并”操作并标准化为以上三个结果属性:
def test_timedelta():
    delta = timedelta(
        days = 50,
        seconds = 27,
        microseconds = 10,
        milliseconds = 29000,
        minutes = 5,
        hours = 8,
        weeks = 2
    )
    print(delta)
    # 运行结果为：64 days, 8:05:56.000010


def test_date():
    # 返回当前的本地时间
    print(date.today())
    print(type(date.today()))
    # 下面的写法，等同于上面的写法，date.fromtimestamp()，返回时间戳对应的当地时间
    print(date.fromtimestamp(time.time()))
    print(type(date.fromtimestamp(time.time())))

    # 返回对应于预期格列高利历序号的日期，其中公元1年1月1晶的序号为1。   PS：具体的传值，我还真不知道。。。
    print(date.fromordinal(2020))

    # 返回一个对应于以YYYY - MM - DD格式给出的date_string的date对象
    print(date.fromisoformat("2020-11-19"))
    print(type(date.fromisoformat('2020-11-19')))

    # 这是date.isoformat()的逆操作。 它只支持YYYY - MM - DD格式。
    # print(date.isoformat('2020-11-19'))       这里有Bug，需要一个datetime.date格式，实际上我传递的是str

    # 获取min, max, 最小的间隔
    print(date.min)
    print(date.max)
    print(date.resolution)

    # 在最大年和最小年里面，返回一个年，具体用法没搞懂
    # print(date.year)
    # print(date.month)


# test_timedelta()
test_date()