#coding:utf-8

import time
from datetime import date
from datetime import datetime
from datetime import timedelta

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
    # print(date.today())
    # print(type(date.today()))
    # 下面的写法，等同于上面的写法，date.fromtimestamp()，返回时间戳对应的当地时间
    # print(date.fromtimestamp(time.time()))
    # print(type(date.fromtimestamp(time.time())))

    # 返回对应于预期格列高利历序号的日期，其中公元1年1月1晶的序号为1。
    # print(date.fromordinal(2))

    # 返回一个对应于以YYYY - MM - DD格式给出的date_string的date对象
    # print(date.fromisoformat("2020-11-19"))
    # print(type(date.fromisoformat('2020-11-19')))

    # 这是date.isoformat()的逆操作。 它只支持YYYY - MM - DD格式。
    # print(date.isoformat('2020-11-19'))       这里有Bug，需要一个datetime.date格式，实际上我传递的是str

    # 获取min, max, 最小的间隔
    # print(date.min)
    # print(date.max)
    # print(date.resolution)

    # 在最大年和最小年里面，返回一个年，具体用法没搞懂
    # print(date.year)
    # print(date.month)

    # date.replace()返回一个具有同样值的日期
    # d = date(2020, 11, 20)
    # print(d.replace(day=30))

    # date.timetuple(),返回一个 time.struct_time，即 time.localtime() 所返回的类型。
    # print(date.timetuple(date.today()))
    # print(date.timetuple(date(2020, 11, 20)))
    # print(type(date.timetuple(date.today())))

    # date.weekday()返回一个整数，代表星期几，0为星期一
    # print(date(2020, 11, 20).weekday())
    # date.isoweekday()返回一个整数，代表星期几，1为星期一
    # print(date(2020, 11, 20).isoweekday())

    # date.isocalendar(),返回一个由三部分组成的 named tuple 对象: year, week 和 weekday。
    # print(date(2020, 11, 20).isocalendar())

    # date.isoformat(),返回一个以 ISO 8601 格式 YYYY-MM-DD 来表示日期的字符串:
    # print(date(2020, 11, 20).isoformat())
    # print(type(date(2020, 11, 20).isoformat()))

    # date.__str__()，对于日期对象 d, str(d) 等价于 d.isoformat()
    # print(date(2020, 11, 20).__str__())
    # print(type(date(2020, 11, 20).__str__()))

    # date.ctime()，返回一个表示日期的字符串:
    # print(date(2020, 11, 20).ctime())
    # print(type(date(2020, 11, 20).ctime()))

    # date.strftime(), 创建一个显示格式字符串所控制的表示时间的字符串
    # print(date(2020, 11, 20))
    # print(type(date(2020, 11, 20)))
    # print(date(2020, 11, 20).strftime('%Y%m%d'))
    # print(type(date(2020, 11, 20).strftime('%Y%m%d')))

    # datetime.strptime(),根据表示日期和时间的字符串和相应的格式字符串来创建一个 datetime 对象。
    # print(datetime.strptime('2020-11-20', '%Y-%m-%d'))
    # print(type(datetime.strptime('2020-11-20', '%Y-%m-%d')))
    pass

def test_datetime():
    # print(datetime(2020, 11, 20))
    # print(type(datetime(2020, 11, 20)))
    pass

# test_timedelta()
# test_date()
test_datetime()