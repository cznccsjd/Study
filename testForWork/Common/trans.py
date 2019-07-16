#coding:utf-8
'''
数据格式转换文件
'''

import re

def cnlist(self, names, sign1=','):
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


def restr(self, names):
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