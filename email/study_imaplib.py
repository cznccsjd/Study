#coding:utf-8
"""
学习IMAP文件
"""

from imaplib import IMAP4
from imaplib import IMAP4_SSL

# The IMAP4 class supports the with statement.
# When used like this, the IMAP4 LOGOUT command is issued automatically when the with statement exits. E.g.:
# with IMAP4("mail.51talk.com") as M:
#     print(M.noop())

m = IMAP4_SSL(host='mail.51talk.com')
# 登录
m.login(user='zhoujinlong', password='@Nisheng76')
# Select a mailbox. Returned data is the count of messages in mailbox (EXISTS response). The default mailbox is 'INBOX'.
# If the readonly flag is set, modifications to the mailbox are not allowed.
print(m.select())

# Append message to named mailbox
# print(m.append())

# Checkpoint mailbox on server.
print(m.check())

# print(m.list())

typ, data = m.search(None, 'ALL')
print(data)