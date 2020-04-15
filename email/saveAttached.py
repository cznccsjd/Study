#coding:utf-8
'''
保存指定的邮件附件，目前还不能复用，仅满足我自己的需求
'''
import os, re, poplib
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

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

if __name__ == '__main__':
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
    # 账户信息
    email = ''
    password = ''
    pop3_server = ''

    # 检测账户信息
    if not email:
        print('邮箱账户名不能为空！！')
        os._exit(0)
    elif not password:
        print('邮箱密码不能为空！！')
        os._exit(1)
    elif not pop3_server:
        print('邮箱服务器不能为空!!')
        os._exit(0)

    # 连接到POP3服务器，带SSL的：
    server = poplib.POP3_SSL(pop3_server)
    # 可以打开或者关闭调试信息
    server.set_debuglevel(0)
    # POP3服务器的欢迎文字
    print(server.getwelcome())
    # 身份认证
    server.user(email)
    server.pass_(password)
    # stat()返回邮件数量和占用空间
    msg_count, msg_size = server.stat()
    print('message count:',msg_count)
    print('message size:',msg_size)

    # 把附件下载到本地,基于自身实际情况，倒序查找
    for i in range(msg_count,0,-1):
        resp, byte_lines, octets = server.retr(i)
        # 转码
        str_lines = []
        for x in byte_lines:
            str_lines.append(x.decode())
        # 拼接邮件内容
        msg_content = '\n'.join(str_lines)
        # 把邮件内容解析为Message对象
        msg = Parser().parsestr(msg_content)
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
        # 删除邮件，直到运行server.quit()之后，才会被删除
        server.dele(i)

        print('subject:', headers['Subject'])
        print('from:', headers['From'])
        print('to:', headers['To'])
        if 'cc' in headers:
            print('cc:', headers['Cc'])
        print('date:', headers['Date'])
        print('attachments:', attachments)
        print('--------------------')

    server.quit()