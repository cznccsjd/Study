#coding:utf-8
'''
数据格式转换文件
'''

import re, time

class Trans():

    def strtolist(self, names, sign1=','):
        '''
        将中文str转换为list
        :param names: 输入的中文字符串
        :param sign1: 通过split(sign1)，将中文词组单独拿出来
        :return:
        '''
        tmp = []
        name = re.sub(r'\[|\]|\\|\'', '', names)
        if (len(name)) == 0:
            pass
        elif type(name) == str:
            items = name.split(sign1)
            for item in items:
                item = re.sub(r'\[|\]|\\|\'', '', item)
                tmp.append(item)
        elif type(name) == list:
            tmp = name
        else:
            pass
        return tmp


    def restring(self, names):
        '''
        将re.sub()过滤的词组转换成符合条件的格式，str，eg：aa|bb|cc
        :return:
        '''
        tmp = ''
        if type(names) == str:
            pass  # 没想好怎么处理，找到分隔符，然后添加'|'即可
        elif type(names) == list:
            for name in names:
                tmp += name
                tmp += '|'
            tmp = tmp[:-1]
        else:
            pass  # 其他的先不处理？后续碰倒再优化
        return tmp


    def strtodict(self, names, sign1=';', sign2='='):
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

    def tupletolist(self, tuple):
        '''
        将pymysql返回的tuple，去掉()，变为通用的list
        :param tuple:
        :param sign1:
        :return:
        '''
        list = []
        string = str(tuple)
        tmplist = re.sub('\(|\)','',string)
        strlist = re.sub(',,',',',tmplist)
        if strlist[-1] == ',':
            strlist = strlist[:-1]
        strs = strlist.split(',')
        for i in strs:
            # ii = int(i)
            list.append(i)
        return list

    def stringtodict(self, names, sign1=';', sign2='='):
        '''
        将字符串转换为dict
        :param names: 输入的字符串
        :param sign1:第一次分隔的符号
        :param sign2:第二次分割的分号
        :return:转换完成的dict
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

    def dicttostring(self, dict, sign1=',', sign2=':'):
        strdict = str(dict)
        strdicttmp = re.sub("\{|\}|\'|\"", "", strdict)
        strtmp = re.sub(sign1, ';', strdicttmp)
        string = re.sub(sign2, '=', strtmp)
        return string

if __name__ == '__main__':
    # Trans().tupletolist(tuple=((2603,), (3111,), (3126,), (3164,)))
    Trans().dicttostring({"pp":1,'b':'aa'},',',':')