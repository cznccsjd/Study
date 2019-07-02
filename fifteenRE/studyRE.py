#coding:utf-8
'''
正则表达式RE学习文件
'''
import re

############ group()和groups() #####################
'''
group()方法或者返回所有匹配对象或是跟据要求返回某个特定子组；
groups()则很简单，返回一个包含唯一或者所有子组的元组
'''
# 匹配abc-123这种类型
# patt = '\w+-\d+'
# m = re.match(patt, 'abc-123')
# if m is not None:print(m.group())
#上面的正则表达式不能匹配abc-xyz类型
# m = re.match('(\w\w\w-\d\d\d)','abc-123')
# if m is not None:print(m.group())
#
# m = re.match('\w\w\w-\d\d\d','abc-xyz')
# if m is not None:print(m.group())

# m = re.match('(\w\w\w)-(\d\d\d)','abc-123')
# print(m.group())
# print(m.group(1))
# print(m.group(2))
# print(m.groups())
# print(type(m.group()),type(m.group(1)),type(m.groups()))

# 加深理解
# m = re.match('ab','ab')     #无子组
# print('m.group',m.group())        #完全匹配
# print('m.groups',m.groups())        #所有匹配的子组，在这里没有

# m = re.match('(ab)', 'ab')      #有一个子组
# print('m.group',m.group())        #完全匹配
# print('m.groups',m.groups())        #所有匹配的子组，在这里有一个数值
# print('m.group(1)',m.group(1))


# m = re.match('(a)(b)', 'ab')        #有两个子组
# print('m.group',m.group())        #完全匹配
# print('m.groups',m.groups())        #所有匹配的子组，在这里有一个数值
# print('m.group(1)',m.group(1))


# m = re.match('(a(b))', 'ab')
# print('m.group',m.group())        #完全匹配
# print('m.groups',m.groups())        #所有匹配的子组，在这里有一个数值
# print('m.group(1)',m.group(1))

##############  match()匹配字符串  #################
'''
match(pattern,string,flags=0)
match()函数尝试从字符串的开头开始对模式进行匹配。如果匹配成功，就返回一个匹配对象，而如果匹配失败了，就返回None。
'''
# m = re.match('foo','fooghf')
# if m is not None:
#     print(m.group())
#     print(m)


##############  search()  ############################
'''
search()在一个字符串中查找一个模式搜索与匹配的比较）
要搜索的模式出现在一个字符串中间的几率要比出现在字符串开头的几率要大一些。这正是search()派上用场的时候。
search和match的工作方式一样，不同之处在于search会检查参数字符串任意位置的地方给定正则表达式模式的匹配情况。
如果搜索到成功的匹配，会返回一个匹配对象，否则返回None。
'''
# m = re.match('foo','seafood')
# if m is not None:
#     print('match()',m.group())    #match匹配失败,match是从字符串的开头开始匹配，中间的匹配不到
#
# n = re.search('foo','seefood')
# if n is not None:
#     print('search()',n.group())   #search匹配成功，search是在字符串中间也可以被匹配到


############### 匹配多个字符串(|)  ########################
# bt = 'bat|bet|bit'      #正则表达式：bat, bet, bit
# m = re.match(bt, 'bat')     #'bat'是匹配的
# if m is not None:print('match匹配bat',m.group())
#
# m = re.match(bt, 'blt')
# if m is not None:print('match匹配blt',m.group())   #没有匹配blt
#
# m = re.match(bt, 'he bit me')   #不匹配字符串
# if m is not None:print('match匹配he bit me',m.group())
#
# m = re.search(bt, 'he bit me')   #搜索到bit
# if m is not None:print('search搜索he bit me',m.group())

###########  匹配任意单个字符(.)  ###################
# anyend = '.end'
# m = re.match(anyend,'bend')     #句点匹配'b'，.匹配任何字符（换行除外），此处.匹配了b
# if m is not None:print('match匹配bend',m.group())
#
# m = re.match(anyend,'end')      #匹配不到任何字符，因为.点需要匹配个任意字符
# if m is not None:print('match匹配end',m.group())
#
# m = re.match(anyend, '\nend')       #匹配不到，因为.点不能匹配换行
# if m is not None:print('match匹配\nend',m.group())
#
# m = re.search(anyend, 'The end')        #可以匹配到
# if m is not None:print('search搜索The end',m.group())

###################  创建字符集和([])  ####################
# m = re.match('[cr][23][dp][o2]', 'c3po')
# if m is not None:print('[cr][23][dp][o2]match"c3po"',m.group())
#
# m = re.match('[cr][23][dp][o2]', 'c2do')
# if m is not None:print('[cr][23][dp][o2]match"c2do"',m.group())
#
# m = re.match('r2d2|c3po','c2do')
# if m is not None:print('r2d2|c3po match c2do',m.group())
#
# m = re.match('r2d2|c3po','r2d2')
# if m is not None:print('r2d2|c3po match r2d2',m.group())


################# 重复、特殊字符和子组  #########################
#匹配电子邮件 xxx@xxx.com
# patt = '\w+@\w+\.com'       #最基础的匹配

# 除此之外增加匹配xxx@xxx.xxx.com
# patt = '\w+@(\w+\.)?\w+\.com'
#
# m = re.match(patt, 'test@sina.com')
# if patt is not None:print(m.group())

# 如果存在特殊字符”-“ xxx@xxx-xxx.com
# patt = '\w+@((\w+)-(\w+)\.)?(\w+)-(\w+)+\.com'
# m = re.match(patt, 'test@te-st.te-st.com')
# if m is not None:print(m.group())


############ 从字符串的开头或者结尾匹配及在单词边界上的匹配  ######################
# m = re.search('^The', 'The end.')       #从开头匹配
# if m is not None:print('^开头',m.group())

# m = re.search('^The', 'end. The')       #不在开头，匹配不到
# if m is not None:print(m.group())

# m = re.search(r'\bthe', 'bite the dog')         #在词边界
# if m is not None:print(m.group())

# m = re.search(r'\bthe', 'bitethe dog')      #the不在单次开头，匹配不到
# if m is not None:print(m.group())

# m = re.search(r'\Bthe', 'bitethe dog')      #匹配不在单次开头的，可以匹配到
# if m is not None:print(m.group())


############### 用findall（）找到每个出现的匹配部分  #####################
'''
findall()总返回一个列表，如果没有找到匹配的部分，返回空列表 
'''
# print(re.findall('car', 'car'))
# print(re.findall('car','scary'))
print(re.findall('car','carry the barcardi to the car'))



####################  用sub()和subn()进行搜索和替换  ###########################
'''
sub()和subn()，都是将某字符串中所有匹配正则表达式模式的部分进行替换。
用来替换的部分通常是一个字符串，也可能是一个函数，该函数防止一个用来替换的字符串；
subn()还返回一个表示替换次数的数字，替换后的字符串和表示替换次数的数字作为一个元组的元素返回
'''
# print(re.sub('X', 'Mr. Smith', 'attn:X\n\nDear X,\n'))          #区分大小写的
# print(re.subn('X', 'Mr. Smith', 'attn:X\n\nDear X,\n'))


###############  用split()分割（分割模式）  #######################################
'''
根据正则表达式模式分割字符串
'''
# print(re.split(':','stri1:str2:str3'))
# f = open('whodata.txt','r')
# for eachLine in f.readlines():
#     # print(re.split('\s\s+',eachLine))       #结果会输出\n，这是不需要的，可以优化
#     print(re.split('\s\s+|\n',eachLine))
# f.close()