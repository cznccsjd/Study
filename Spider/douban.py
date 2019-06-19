#coding:utf-8
'''
实现功能：
1、豆瓣小组关键字搜索（北京租房）
2、去除不符合要求的小组
3、返回小组名称和小组url
PS：返回dict类型，key=url, values=组名
'''

import requests,time,configparser,os
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
        dictC = {}
        dictC['url1'] = 'https://www.douban.com/group/search'
        dictC['headers'] = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
        dictC['sleep'] = 3
        # 浏览器拷贝过来的cookie是str，需要转换为dict
        cookie = {}
        # cookie = 'll="108288"; bid=R3URBd6PEUM; __utmc=30149280; __utmz=30149280.1560747609.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="180074916:wCXkvYfVx4c"; ck=Lybj; push_noty_num=0; push_doumail_num=0; __utmv=30149280.18007; douban-fav-remind=1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1560750952%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D9q6dhqbiZH3h_jH1-GvwAPZpyuRs_NOdxgxIT0wZ_ai%26wd%3D%26eqid%3Dfceb3c2601ea806c000000025d071e4f%22%5D; _pk_id.100001.8cb4=094e9890c37d59d8.1560747606.2.1560750952.1560748010.; _pk_ses.100001.8cb4=*; __utma=30149280.1329075807.1560747609.1560747609.1560750952.2; __utmt=1; __utmb=30149280.8.4.1560750952'
        if len(cookie) == 0:
            coo = {}
            dictC['cookie'] = coo
        elif type(cookie) == str:
            items = cookie.split(";")
            coo = {}
            for item in items:
                kv = item.split("=")
                coo[kv[0]] = kv[1]
            dictC['cookie'] = coo

        dictC['city'] = '北京'
        dictC['notArea'] = ['朝阳','望京','丰台','通州','大兴','燕郊','顺义','CBD','芍药居','惠新西街南口','双井','八通','国贸','宋家庄','酒仙桥','十里堡','双桥','潘家园','褡裢坡','石景山','劲松']
        dictC['Area'] = ['回龙观','龙泽','霍营','平西府','育新','育知路','西三旗','上地','清河','西二旗']
        # dict['group'] = {'https://www.douban.com/group/beijingzufang/': '北京租房', 'https://www.douban.com/group/26926/': '北京租房豆瓣', 'https://www.douban.com/group/zhufang/': '北京无中介租房', 'https://www.douban.com/group/279962/': '北京租房（非中介）', 'https://www.douban.com/group/sweethome/': '北京租房（密探）', 'https://www.douban.com/group/opking/': '北京个人租房 （真房源|无中介）', 'https://www.douban.com/group/252218/': '北京租房专家', 'https://www.douban.com/group/625354/': '北京租房（真的没有中介）小组', 'https://www.douban.com/group/257523/': '北京租房房东联盟(中介勿扰)', 'https://www.douban.com/group/jumei/': '北京租房', 'https://www.douban.com/group/bjfangchan/': '租房在北京 @北京租房', 'https://www.douban.com/group/bjzf/': '北京租房', 'https://www.douban.com/group/550436/': '☀北京租房大全【推荐★★★★★】', 'https://www.douban.com/group/349665/': '北京租房【宝贝】', 'https://www.douban.com/group/549574/': '北京租房', 'https://www.douban.com/group/zufangbeijing/': '北京租房', 'https://www.douban.com/group/465554/': '北京 租房 房东 直租（非中介）', 'https://www.douban.com/group/haidianzufang/': '北京海淀租房', 'https://www.douban.com/group/527998/': '北京求室友（租房）', 'https://www.douban.com/group/259273/': '北京租房生活', 'https://www.douban.com/group/516673/': '租房（北京、上海、广州、深圳）', 'https://www.douban.com/group/ziruyoujia/': '自如友家【北京租房、合租、拼房】', 'https://www.douban.com/group/450859/': '北京昌平回龙观周边租房小组', 'https://www.douban.com/group/bjzft/': '北京租房团（不欢迎中介）', 'https://www.douban.com/group/334449/': '北京租房合租房', 'https://www.douban.com/group/atlaslj/': '北京租房联盟', 'https://www.douban.com/group/325060/': '北京基友G们来租房', 'https://www.douban.com/group/254559/': '北京租房', 'https://www.douban.com/group/374051/': '北京租房小组！！', 'https://www.douban.com/group/FZG/': '北京租房无中介联盟', 'https://www.douban.com/group/tiantongyuan/': '北京天通苑租房', 'https://www.douban.com/group/xiangtuo/': '北京租房', 'https://www.douban.com/group/468187/': '北京租房&西二旗单间合租房', 'https://www.douban.com/group/bjjob4/': '北京日租房', 'https://www.douban.com/group/zusoufun/': '北京租房（找室友）', 'https://www.douban.com/group/bjganbei/': '北京租房帮', 'https://www.douban.com/group/263734/': '北京租房，不要中介', 'https://www.douban.com/group/425817/': '北京租房&找房子搬家 小组', 'https://www.douban.com/group/474785/': '北京昌平回龙观租房', 'https://www.douban.com/group/154136/': '北京靠谱租房', 'https://www.douban.com/group/358010/': '北京租房【小李先森】', 'https://www.douban.com/group/592738/': '北京租房信息-推荐度★★★★★', 'https://www.douban.com/group/422484/': '北京租房（踢开中介）', 'https://www.douban.com/group/589927/': '北京中关村租房（限女神一位）', 'https://www.douban.com/group/308428/': '北京圈—招聘租房交友二手打折兼职', 'https://www.douban.com/group/577834/': '北京租房信息', 'https://www.douban.com/group/401281/': '北京租房', 'https://www.douban.com/group/626908/': '北京回龙观西二旗龙泽租房', 'https://www.douban.com/group/65239/': '北京海淀短期租房', 'https://www.douban.com/group/beijingrizu/': '北京日租房', 'https://www.douban.com/group/379809/': '北京租房小组', 'https://www.douban.com/group/579174/': '北京短租房', 'https://www.douban.com/group/587010/': '北京租房，合租，整租', 'https://www.douban.com/group/425860/': '北京租房小组', 'https://www.douban.com/group/370806/': '北京租房', 'https://www.douban.com/group/509975/': '北京北师大 北邮人租房', 'https://www.douban.com/group/331294/': '北京租房小组', 'https://www.douban.com/group/482087/': '北京十号线租房', 'https://www.douban.com/group/zhongjiesb/': '北京无中介租房小组', 'https://www.douban.com/group/633410/': '北京租房（一居室整租）不合租', 'https://www.douban.com/group/278959/': '北京租房信息可以在这里发布嘛', 'https://www.douban.com/group/423071/': '北京房东直租~租房无中介~', 'https://www.douban.com/group/564671/': '豆瓣.北京寒暑假求职过渡.短租房', 'https://www.douban.com/group/562077/': '看房狗北京租房', 'https://www.douban.com/group/yangmaojuan/': '北京租房@羊毛卷之家@', 'https://www.douban.com/group/xichengzufang/': '北京西城租房（推荐度★★★★★', 'https://www.douban.com/group/581616/': '北京房东直租房', 'https://www.douban.com/group/lesrenting/': '拉拉@北京联合租房', 'https://www.douban.com/group/459437/': '北京短租房日租房', 'https://www.douban.com/group/493671/': '北京租房生活', 'https://www.douban.com/group/526134/': '北京租房（我爱我家 全优房源）', 'https://www.douban.com/group/405345/': '北京租房居委会', 'https://www.douban.com/group/512143/': '北京无中介租房小组', 'https://www.douban.com/group/522650/': '北京链家租房小组', 'https://www.douban.com/group/504399/': '北京房东直接租房', 'https://www.douban.com/group/527777/': '北京求租房', 'https://www.douban.com/group/qunarhouse/': '去哪儿北京租房', 'https://www.douban.com/group/SYAD/': '北京租房【不限女】小组', 'https://www.douban.com/group/497311/': '~【北京】带着宠物来租房~', 'https://www.douban.com/group/276176/': '北京出租房（请自觉统一标题格式）', 'https://www.douban.com/group/changpingzufang/': '北京昌平租房（推荐度★★★★★）', 'https://www.douban.com/group/410479/': '北京外来人口租房小组', 'https://www.douban.com/group/544504/': '北京拉拉租房les', 'https://www.douban.com/group/480684/': '与豆友合租 | 北京租房', 'https://www.douban.com/group/376344/': '北京二房东租房小组', 'https://www.douban.com/group/376461/': '北京南二、三环租房联盟', 'https://www.douban.com/group/539511/': '北京租房（避开中介）', 'https://www.douban.com/group/242806/': '北京租房！找小伙伴们一起住一房间', 'https://www.douban.com/group/585214/': '北京豆瓣租房小组', 'https://www.douban.com/group/beijing-zufang/': '北京租房找室友--爱合住', 'https://www.douban.com/group/461893/': '豆瓣北京租房', 'https://www.douban.com/group/633786/': '北京常营租房', 'https://www.douban.com/group/605273/': '北京租房@一朵云上住', 'https://www.douban.com/group/581097/': '北京租房小分队', 'https://www.douban.com/group/605011/': '北京租房在看房狗', 'https://www.douban.com/group/620813/': '北京直租房分租小组', 'https://www.douban.com/group/450630/': '北京链家官方租房', 'https://www.douban.com/group/484464/': '北京无中介租房购房', 'https://www.douban.com/group/612714/': '北京外国人租房室友小组', 'https://www.douban.com/group/564141/': '【无中介租房】北京租房拒绝中介', 'https://www.douban.com/group/467851/': '北京同志租房', 'https://www.douban.com/group/99372/': '北京海淀租房 海淀区租房', 'https://www.douban.com/group/280198/': '北京租房家族', 'https://www.douban.com/group/141170/': '北京租房', 'https://www.douban.com/group/536777/': '考研租房|北京高校租房|考研合租', 'https://www.douban.com/group/443927/': '北京搬家租房小组', 'https://www.douban.com/group/368441/': '北京租房那点事', 'https://www.douban.com/group/280800/': '北京租房', 'https://www.douban.com/group/382509/': '北京租房，合租房，买卖。。。', 'https://www.douban.com/group/289305/': '北京租房', 'https://www.douban.com/group/613276/': '北京租房搬家', 'https://www.douban.com/group/493993/': '北京搬家和租房', 'https://www.douban.com/group/468001/': '北京租房(无中介）', 'https://www.douban.com/group/312287/': '大学生北京租房那点事', 'https://www.douban.com/group/530865/': '北京租房女生小组', 'https://www.douban.com/group/225714/': '北京-我们--只--租房东房！', 'https://www.douban.com/group/516374/': '北京带狗租房', 'https://www.douban.com/group/551004/': '偶寓——北京合租租房（无中介）', 'https://www.douban.com/group/579144/': '北京小件搬家小组兼租房小组', 'https://www.douban.com/group/xyq198663/': '北京租房', 'https://www.douban.com/group/540222/': '北京东城租房', 'https://www.douban.com/group/585528/': '租房（北京，上海，广州，深圳）', 'https://www.douban.com/group/605717/': '北京地铁13号线立水桥站附近租房', 'https://www.douban.com/group/580598/': '北京租房&中介勿扰', 'https://www.douban.com/group/yezhufangyuan/': '北京租房路标', 'https://www.douban.com/group/hdzufang/': '北京海淀租房', 'https://www.douban.com/group/388408/': '北京租房', 'https://www.douban.com/group/495801/': '北京安心租房', 'https://www.douban.com/group/495442/': '北京租房小组', 'https://www.douban.com/group/545029/': '北京租房（豆友推荐）', 'https://www.douban.com/group/482790/': '北京租房，合租（非中介）', 'https://www.douban.com/group/cbdzufang/': '北京租房联盟', 'https://www.douban.com/group/592327/': '北京个人租房', 'https://www.douban.com/group/510879/': '北京租房', 'https://www.douban.com/group/549122/': '北京租房【中介勿来】', 'https://www.douban.com/group/zufang010/': '北京租房', 'https://www.douban.com/group/388123/': '北京租房', 'https://www.douban.com/group/539132/': '北京租房', 'https://www.douban.com/group/523342/': '北京租房（房东）', 'https://www.douban.com/group/599182/': '蘑菇租房-北京', 'https://www.douban.com/group/287454/': '北京租房那点事儿', 'https://www.douban.com/group/510963/': '北京租房', 'https://www.douban.com/group/523034/': '北京无中介租房', 'https://www.douban.com/group/498931/': '北京搬家和租房加租车☂☂☂', 'https://www.douban.com/group/426114/': '▶自如友家◀-北京租房|合租|', 'https://www.douban.com/group/498838/': '北京精彩日租短租房，住宿！', 'https://www.douban.com/group/587991/': '北京租房@个人转租房源', 'https://www.douban.com/group/536847/': '北京租房【无中介】', 'https://www.douban.com/group/499605/': '北京搬家和租房加租车', 'https://www.douban.com/group/564274/': '北京月付租房', 'https://www.douban.com/group/505959/': '北京无中介租房', 'https://www.douban.com/group/510539/': '北京租房', 'https://www.douban.com/group/488098/': '北京租房', 'https://www.douban.com/group/470225/': '北京租房---热鱼站', 'https://www.douban.com/group/535947/': '北京无中介租房2', 'https://www.douban.com/group/511226/': '【北京租房小组】', 'https://www.douban.com/group/477786/': '北京租房信息共享', 'https://www.douban.com/group/565789/': '北京租房很容易', 'https://www.douban.com/group/382399/': '北京租房8090', 'https://www.douban.com/group/557923/': '北京情侣租房', 'https://www.douban.com/group/513378/': '北京个人租房无中介', 'https://www.douban.com/group/zunar_beijing/': '北京租房（租哪儿）', 'https://www.douban.com/group/457216/': '北京租房（独户型或公寓）', 'https://www.douban.com/group/558676/': '北京租房不限男生', 'https://www.douban.com/group/521113/': '北京租房租客联盟', 'https://www.douban.com/group/498108/': '北京无中介租房', 'https://www.douban.com/group/549341/': '北京租房通', 'https://www.douban.com/group/524318/': '北京高品质租房小组', 'https://www.douban.com/group/466397/': '北京业主直租房', 'https://www.douban.com/group/511471/': '北京公租房', 'https://www.douban.com/group/65453/': '北京海淀日租房', 'https://www.douban.com/group/559146/': '北京诚信租房', 'https://www.douban.com/group/410662/': '北京大学生租房共享', 'https://www.douban.com/group/298934/': '北京租房', 'https://www.douban.com/group/419097/': '北京1租房', 'https://www.douban.com/group/472715/': '北京合租租房信息共享'}
        return dictC

        #######后期导入并完善configparser模块
        # curdir = os.getcwd()
        # dir = os.path.join(curdir, 'douban_config.ini')
        # conf = configparser.ConfigParser()
        # conf.read(dir)
        # sessions = conf.get('result','group')

    def search(self):
        '''
        执行搜索动作，获取相应后的小组名称和url
        :return:
        '''
        urls = {}   # 定义一个字典存储BeautifulSoup处理后的豆瓣租房小组的标题和url
        conf = self.config

        for num in range (0, 220, 20):      #通过豆瓣页面查询到的，当start>200时，会跳转到登录页面了
            url, data = Douban().searchUrl(num)
            try:
                s = requests.sessions.session()
                s.keep_alive = False
                rSearch = requests.get(url, data, headers = conf['headers'], cookies = conf['cookie'])
                # 增加请求间歇时间，防止被封IP
                sleep = conf['sleep']
                time.sleep(sleep)
            except Exception:   #这里except所有异常，有点过分了啊，后续改进
                urls = conf['group']            #这里有问题的，获取到的值不是dict
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
        print('组group,url收集成功：',time.strftime('%H:%M:%S',time.localtime()))
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
            searchdata = {'start':num, 'cat': '1019', 'q': '北京租房'}      #cat=1019是直接通过豆瓣页面获取到
            return searchurl, searchdata

    def searchResult(self,title):
        '''
        将不符合规则的响应结果去除
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