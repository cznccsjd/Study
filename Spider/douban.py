#coding:utf-8
'''
实现功能：
1、豆瓣小组关键字搜索（北京租房）
2、去除不符合要求的小组
3、返回小组名称和小组url
PS：返回dict类型，key=url, values=组名
'''

import requests,time,configparser,os, re
from bs4 import BeautifulSoup

class Douban():
    def __init__(self):
        pass

    @property
    def config(self):
        '''
        配置，参数化，便于后续新增配置文件
        :return:
        '''
        curdir = os.getcwd()
        dir = os.path.join(curdir, 'douban_config.ini')
        conf = configparser.RawConfigParser()  # 使用RawConfigParser()规避读取cookie时，%引发的报错
        conf.read(dir, encoding='utf-8')
        dictC = {}
        url = conf.get('explore', 'group')
        url1 = re.sub('\'|\"','',url)

        dictC['url1'] = url
        headers = conf.get('explore', 'headers')
        header = Douban().dict(headers,':','')
        dictC['headers'] = header
        sleep = conf.get('explore', 'timesleep')
        dictC['sleep'] = int(sleep)
        cookies = conf.get('explore', 'cookie')
        cookie = Douban().dict(cookies,';','=')
        dictC['cookie'] = cookie
        city = conf.get('filter', 'city')
        dictC['city'] = re.sub('\'|\"','',city)

        notArea = conf.get('filter', 'dislikearea')
        dictC['notArea'] = Douban().cnlist(notArea)
        Area = conf.get('filter', 'likearea')
        dictC['Area'] = Douban().cnlist(Area)
        titlelimit = conf.get('filter', 'titlelimit')
        dictC['titlelimit'] = Douban().cnlist(titlelimit)
        dictC['date'] = conf.get('explore', 'datetime')
        dictC['groupmaxnum'] = conf.get('explore', 'groupnum')
        dictC['titlemaxmun'] = conf.get('explore', 'titlenum')
        dictC['errorNum'] = 0
        return dictC

    def cnlist(self,names, sign1=','):
        '''
        将中文str转换为list
        :param names: 输入的中文字符串
        :param sign1: 通过split(sign1)，将中文词组单独拿出来
        :return:
        '''
        tmp = []
        name = re.sub(r'\[|\]|\\|\'', '', names)
        if(len(name)) == 0:
            pass
        elif type(name) == str:
            items = name.split(sign1)
            for item in items:
                item = re.sub(r'\[|\]|\\|\'','',item)
                tmp.append(item)
        elif type(name) == list:
            tmp = name
        else:
            pass
        return tmp

    def restr(self, names):
        '''
        将re.sub()过滤的词组转换成符合条件的格式，str，eg：aa|bb|cc
        :return:
        '''
        tmp = ''
        if type(names) == str:
            pass    #没想好怎么处理，找到分隔符，然后添加'|'即可
        elif type(names) == list:
            for name in names:
                tmp += name
                tmp += '|'
            tmp = tmp[:-1]
        else:
            pass        #其他的先不处理？后续碰倒再优化
        return tmp

    def dict(self, names, sign1=';', sign2='='):
        '''
        将字符串转换为dict
        :param names: 输入的字符串
        :param sign1:
        :param sign2:
        :return:
        '''
        tmp = {}
        name = re.sub('\{|\}|\'|\"', '', names)

        if len(name) == 0:
            pass
        elif type(name) == str:
            items = name.split(sign1)
            if len(items) > 2:
                for item in items:
                    kv = item.split(sign2)
                    tmp[kv[0]] = kv[1]
            else:
                tmp[items[0]] = items[1]
        elif type(name) == dict:
            tmp = name
        else:
            pass
        return tmp

    def search(self):
        '''
        执行搜索动作，获取相应后的小组名称和url
        :return:
        '''
        urls = {}   # 定义一个字典存储BeautifulSoup处理后的豆瓣租房小组的标题和url
        conf = self.config
        errorNum = conf['errorNum']
        maxgroups = conf['groupmaxnum']
        maxgroup = int(maxgroups)
        if maxgroup <= 200:
            maxgroup += 20
        else:
            maxgroup = 220  #通过豆瓣页面查询到的，当start>200时，会跳转到登录页面了

        for num in range (0, maxgroup, 20):
            url, data = Douban().searchUrl(num)
            try:
                s = requests.sessions.session()
                s.keep_alive = False
                rSearch = requests.get(url, data, headers = conf['headers'], cookies = conf['cookie'])
                # 增加请求间歇时间，防止被封IP
                sleep = conf['sleep']
                time.sleep(sleep)
            except Exception as e:   #这里except所有异常，有点过分了啊，后续改进
                # urls = conf['group']            #这里有问题的，获取到的值不是dict
                errorNum += 1
                conf['errorNum'] = errorNum
                print("%s,第%d次报错，url：%s,原因：%s" % (time.strftime('%H:%M:%S', time.localtime()), errorNum, url, e))
                continue
            # 判断是不是被豆瓣封了，判断的有问题，理论上走不到这里，优化上面的except
            if rSearch.status_code != 200:
                print('天了噜，豆瓣的响应居然是%d，快看看是不是cookie不生效了！！！' % rSearch.status_code)
                continue

            # 使用BeautifulSoup4处理requests返回的结果，找到全部的标题和url
            soup = BeautifulSoup(rSearch.text,'lxml')
            titles = soup.select('div.title > h3 > a')
            links = soup.select('div.title > h3 > a')

            for title, link in  zip(titles, links):
                title = title.text
                link = link.get('href')
                ret = Douban().searchResult(title)

                if ret:
                    urls[link] = ret      #豆瓣租房小组的组名可能有重复，用来做dict的value；小组的url肯定是唯一的，用来做dict的key
        print('小组url收集成功：',time.strftime('%H:%M:%S',time.localtime()))
        return urls

    def searchUrl(self,num=0):
        '''
        拼接get请求的url和传输的params
        :param num: 起始页面，默认为0
        :return: 返回请求时的url和传递的参数
        '''
        while(num >= 0):
            conf = self.config
            searchurl = conf['url1']
            searchdata = {'start':num, 'cat': '1019', 'q': '北京租房'}      #cat=1019是直接通过豆瓣页面获取到               ###这里参数化一下，就能应用到整个豆瓣小组了
            return searchurl, searchdata

    def searchResult(self,title):
        '''
        将不符合规则的响应结果去除，这是用for循环来筛选。也可以用正则表达式，参考doSearch.py
        :return:
        '''
        conf = self.config
        str = conf['city']
        strNos = conf['notArea']
        strArea = conf['Area']

        while(str in title):
            num = 0
            for strNo in strNos:
                if strNo in title:
                    break
                else:
                    num += 1

            if num == len(strNos):
                return title
            else:
                break

if __name__ == '__main__':
    Douban().search()
    # Douban().config()
    # Douban().searchUrl(0)
    # Douban().searchResult(title='北京')
