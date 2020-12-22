#coding:utf-8
"""
使用imaplib，保存指定邮件的附件
"""
import email, os, re
from email.header import decode_header
from email.utils import parseaddr
from imaplib import IMAP4_SSL

def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        if charset == 'gb2312':
            charset = 'gb18030'
        value = value.decode(charset)
    return value

def get_email_headers(msg):
    '''
    获取邮件的From、To、Cc、Subject、Date信息
    :param msg:
    :return:
    '''
    headers = {}
    for header in ['From', 'To', 'Cc', 'Subject', 'Date']:
        value = msg.get(header,'')
        if value:
            if header == 'Date':
                headers['Date'] = value
            if header == 'Subject':
                name = decode_str(value)
                subject = u'%s' % (name)
                headers['Subject'] = subject
            if header == 'From':
                hdr, addr = parseaddr(value)
                name = decode_str(hdr)
                from_addr = u'%s <%s>' % (name, addr)
                headers['From'] = from_addr
            if header == 'To':
                all_cc = value.split(',')
                to = []
                for x in all_cc:
                    hdr, addr = parseaddr(x)
                    name = decode_str(hdr)
                    to_addr = u'%s <%s>' % (name, addr)
                    to.append(to_addr)
                headers['To'] = to
            if header == 'Cc':
                all_cc = value.split(',')
                cc = []
                for x in all_cc:
                    hdr, addr = parseaddr(x)
                    name = decode_str(hdr)
                    cc_addr = u'%s <%s>' % (name, addr)
                    cc.append(to_addr)
                headers['Cc'] = ','.join(cc)
    return headers

def get_email_content(message, savepath, date):
    '''
    下载并保存邮件附件
    :param message:
    :param savepath:
    :param date:
    :return:
    '''
    attachments = []
    for part in message.walk():
        filename = part.get_filename()
        if filename:
            filename = filename[:11]+date+filename[11:]
            filename = decode_str(filename)
            data = part.get_payload(decode=True)
            abs_filename = os.path.join(savepath, filename)
            attach = open(abs_filename, 'wb')
            attachments.append(filename)
            attach.write(data)
            attach.close()
    return attachments

# 邮箱相关配置
host = ""
uname = ""
passwd = ''

# 月份：英文转数字
monthes = {
    'Jan':'01',
    'Feb':'02',
    'Mar':'03',
    'Apr':'04',
    'May':'05',
    'Jun':'06',
    'Jul':'07',
    'Aug':'08',
    'Sep':'09',
    'Oct':'10',
    'Nov':'11',
    'Dec':'12'
}

# 登录邮箱
m = IMAP4_SSL(host)
m.login(uname, passwd)
m.select()

tye, data = m.search(None, 'ALL')
# 既可以用search，也可以用uid，下面的代码，都是针对search()写的
# tye, data = m.uid('SEARCH', None, 'ALL')
# print(data)
datas = data[0].split()
for num in datas[::-1]:
    typ, data = m.fetch(num, '(RFC822)')
    msg = email.message_from_string(data[0][1].decode('utf-8'))
    headers = get_email_headers(msg)
    # 查找运营发送的主题为“SS新工作台数据监控仪表盘”的邮件
    if headers['Subject'] != u'SS新工作台数据监控仪表盘':
        continue

    # 获取邮件的发送日期，格式有两种：1、'Sat, 7 Mar 2018 09:55:25 +0800'；2、'Sat, 11 Apr 2020 10:34:55 +0800'
    # 通过RE，拼装保存后的附件名称，eg:CRM_data_ss200414.csv。其中，200214是自己拼装的
    filedates = headers['Date']
    patmonth = '\s\w{3}\s'
    patyear = '\s\d{4}\s'
    patday = '\s\d{1,2}\s'
    patm = re.search(patmonth,filedates)
    if patm is not None:
        patmon = patm.group()
        patmon = patmon.strip()
        month = monthes[patmon]
    else:
        print('指定邮件的月份获取失败，中止本封邮件附件保存流程')
        continue
    paty = re.search(patyear,filedates)
    patd = re.search(patday,filedates)
    pyear = paty.group().strip()
    pday = patd.group().strip()
    if len(pday) == 1:
        pday = str(0) + pday
    filedate = pyear[2:4] + month + pday
    attachments = get_email_content(msg, r'D:\Documents\work\埋点记录',filedate)
    # 删除邮件
    # m.delete()    #m.delete()实际上没有删除，换成store()
    m.store(num, '+FLAGS', '\\Deleted')

    print('subject:', headers['Subject'])
    print('from:', headers['From'])
    print('to:', headers['To'])
    if 'cc' in headers:
        print('cc:', headers['Cc'])
    print('date:', headers['Date'])
    print('attachments:', attachments)
    print('--------------------')

m.close()