#coding:utf-8
"""
pandas模块学习，
相关知识url：https://www.cnblogs.com/misswangxing/p/7903595.html
"""
'''
一、　　Pandas简介

1、Python Data Analysis Library 或 pandas 是基于NumPy 的一种工具，该工具是为了解决数据分析任务而创建的。Pandas 纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。你很快就会发现，它是使Python成为强大而高效的数据分析环境的重要因素之一。

2、Pandas 是python的一个数据分析包，最初由AQR Capital Management于2008年4月开发，并于2009年底开源出来，目前由专注于Python数据包开发的PyData开发team继续开发和维护，属于PyData项目的一部分。Pandas最初被作为金融数据分析工具而开发出来，因此，pandas为时间序列分析提供了很好的支持。 Pandas的名称来自于面板数据（panel data）和python数据分析（data analysis）。panel data是经济学中关于多维数据集的一个术语，在Pandas中也提供了panel的数据类型。

3、数据结构：

Series：一维数组，与Numpy中的一维array类似。二者与Python基本的数据结构List也很相近，其区别是：List中的元素可以是不同的数据类型，而Array和Series中则只允许存储相同的数据类型，这样可以更有效的使用内存，提高运算效率。
Time- Series：以时间为索引的Series。
DataFrame：二维的表格型数据结构。很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器。以下的内容主要以DataFrame为主。
Panel ：三维的数组，可以理解为DataFrame的容器。
Pandas 有两种自己独有的基本数据结构。读者应该注意的是，它固然有着两种数据结构，因为它依然是 Python 的一个库，所以，Python 中有的数据类型在这里依然适用，也同样还可以使用类自己定义数据类型。只不过，Pandas 里面又定义了两种数据类型：Series 和 DataFrame，它们让数据操作更简单了。
'''

##################
#     Series     #
##################
'''
# 1、导入pandas模块并使用别名，以及导入Series模块，以下使用基于本次导入
from pandas import Series
import pandas as pd

# 2、Series
# Series就如同列表一样，一系列数据，每个数据对应一个索引值
# Series 就是“竖起来”的 list
s = Series([1,2,'ww','tt'])     #不是说Series只能允许储存相同的数据类型么？怎么本例中可以是int，也可以是string？？？？
print(s)
print('s的类型：%s',type(s))
# 另外一点也很像列表，就是里面的元素的类型，由你任意决定（其实是由需要来决定）。
# 这里，我们实质上创建了一个 Series 对象，这个对象当然就有其属性和方法了。比如，下面的两个属性依次可以显示 Series 对象的数据值和索引：
print(s.index)
print("Series的值是：%s，值的类型是：%s" % (s.values,type(s.values)))     #获取Series的value

# 列表的索引只能是从 0 开始的整数，Series 数据类型在默认情况下，其索引也是如此。不过，区别于列表的是，Series 可以自定义索引：
print('\n##########')
s2 = Series(['jlz','man',28], index=['name','sex','age'])
print('s2:\n',s2)

# 每个元素都有了索引，就可以根据索引操作元素了。还记得 list 中的操作吗？Series 中，也有类似的操作。先看简单的，根据索引查看其值和修改其值：
print('\n##########')
print(s2['name'])
s2['name'] = 'zjlo'
print(s2['name'])
print('修改后的s2\n',s2)

# 这是不是又有点类似 dict 数据了呢？的确如此。看下面就理解了。

# 读者是否注意到，前面定义 Series 对象的时候，用的是列表，即 Series() 方法的参数中，第一个列表就是其数据值，如果需要定义 index，放在后面，依然是一个列表。除了这种方法之外，还可以用下面的方法定义 Series 对象：
print('\n##########')
sd = {'python':9000,'c++':9001,'c#':9000}
print('sd的值：%s\nsd的类型：%s'%(sd, type(sd)))
s3 = Series(sd)
print('Series(sd)的值：%s\nSeries(sd)的类型：%s'%(s3, type(s3)))

# 现在是否理解为什么前面那个类似 dict 了？因为本来就是可以这样定义的。

# 这时候，索引依然可以自定义。Pandas 的优势在这里体现出来，如果自定义了索引，自定的索引会自动寻找原来的索引，如果一样的，就取原来索引对应的值，这个可以简称为“自动对齐”。
print('\n##########')
print(sd)
s4 = Series(sd, index=['java','c++','c#'])
print(s4)

# 在 Pandas 中，如果没有值，都对齐赋给 NaN。
# Pandas 有专门的方法来判断值是否为空。
print('\n##########')
print('Pandas判断值是否为空\n',pd.isnull(s4))
# 此外，Series 对象也有同样的方法：
print('Series对象判断值是否为空\n',s4.isnull())

# 其实，对索引的名字，是可以从新定义的：
print('\n##########')
print(s4)
s4.index = ['语文','数学','English']
print('索引的名字重新定义：\n',s4)

# 对于 Series 数据，也可以做类似下面的运算（关于运算，后面还要详细介绍）：
print('\n##########')
print(s4)
print('Series数据进行运算：\n',s4 * 2)
print('\n')
print(s4[s4 > 9000])
'''

##################
#    DataFrame   #
##################
# DataFrame 是一种二维的数据结构，非常接近于电子表格或者类似 mysql 数据库的形式。它的竖行称之为 columns，横行跟前面的 Series 一样，称之为 index，也就是说可以通过 columns 和 index 来确定一个主句的位置。

# 首先导入模块
from pandas import Series, DataFrame
print('\n##########')
data = {"name":['google','baidu','yahoo'],"marks":[100,200,300],"price":[1,2,3]}
print('date的数值：%s，data的类型：%s'%(data, type(data)))
f1 = DataFrame(data)
print('f1的数值：\n%s\nf1的类型：%s' %(f1, type(f1)))
# 这是定义一个 DataFrame 对象的常用方法——使用 dict 定义。字典的“键”（"name"，"marks"，"price"）就是 DataFrame 的 columns 的值（名称），字典中每个“键”的“值”是一个列表，它们就是那一竖列中的具体填充数据。上面的定义中没有确定索引，所以，按照惯例（Series 中已经形成的惯例）就是从 0 开始的整数。从上面的结果中很明显表示出来，这就是一个二维的数据结构（类似 excel 或者 mysql 中的查看效果）。
# 上面的数据显示中，columns 的顺序没有规定，就如同字典中键的顺序一样，但是在 DataFrame 中，columns 跟字典键相比，有一个明显不同，就是其顺序可以被规定，向下面这样做：
print('\n##########')
f2 = DataFrame(data,columns=['name','price','marks'])
print('重新规定顺序后的DataFrame：f2\n',f2)

# 跟 Series 类似的，DataFrame 数据的索引也能够自定义
print('\n##########')
f3 = DataFrame(data,columns=['name','marks','price'],index=['a','b','c'])
print('定义索引后的f3:\n',f3)

# 定义 DataFrame 的方法，除了上面的之外，还可以使用“字典套字典”的方式。
print('\n##########')
newdata = {'lang':{'first':'python','second':'java'},'price':{'first':5000,'second':2000}}
f4 = DataFrame(newdata)
print('使用字典套字典方式定义DataFrame\n',f4)
print('\n使用之前的方法定义DataFrame')
newdata1 = {'lang':['python','java'],'price':[5000,2000]}
f41 = DataFrame(newdata1,index=['first','second'])
print(f41)
# 在字典中就规定好数列名称（第一层键）和每横行索引（第二层字典键）以及对应的数据（第二层字典值），也就是在字典中规定好了每个数据格子中的数据，没有规定的都是空。

# DataFrame 对象的 columns 属性，能够显示素有的 columns 名称。并且，还能用下面类似字典的方式，得到某竖列的全部内容（当然包含索引）：
print('\n##########')
print('123123')
newdata = {"lang":{"firstline":"python","secondline":"java"},"price":{"firstline":8000}}
f42 = DataFrame(newdata)
print(f42)
print("\n")
# f421 = DataFrame(newdata,index=['firstline','secondline','thirdline'])  #这行报错，报错信息：AttributeError: 'list' object has no attribute 'astype'
# print(f421)
print('f3的值\n',f3)
print("f3['name']:\n",f3['name'])

# 下面操作是给同一列赋值
print('\n##########')
print('给同一列赋值\n')
newdata1 = {'username':{'first':'jlz','second':'dadiao'},'age':{'first':28,'second':29}}
f6 = DataFrame(newdata1,columns=['username','age','sex'])
print(f6)
print('\n')
f6['sex'] = 'man'
print(f6)

#给一列单独赋值
# 除了能够统一赋值之外，还能够“点对点”添加数值，结合前面的 Series，既然 DataFrame 对象的每竖列都是一个 Series 对象，那么可以先定义一个 Series 对象，然后把它放到 DataFrame 对象中。如下：
print('\n')
ssex = Series(['男','女'],index=['first','second'])
print('Series ssex的值：\n',ssex)
f6['sex'] = ssex
print('\n给一列单独赋值后\n', f6)

#更精准的修改数据
print('\n')
f6['age']['second'] = 30        #提示SettingWithCopyWarning，链式赋值导致的warning，可参考：https://blog.csdn.net/haolexiao/article/details/81180571
print('更精准的修改数据\n', f6)

