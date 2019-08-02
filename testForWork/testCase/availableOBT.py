#coding;utf-8

import pymysql
from testForWork.Common.transdata import Trans

# 代码中获取到的可用的OBT
obtfiles = open(r"D:\Desktop\测试环境能用的OBT老师.txt",encoding='utf-8',mode='r')
obtArrstmp = obtfiles.readlines()
obtfiles.close()
obtArrstmp1 = str(obtArrstmp)
obtArrstmp2 = obtArrstmp1[2:-2]
obtArrs = Trans().strtolist(obtArrstmp2)
obtArrsSet = set(obtArrs)

# 数据库中is_full_time在8,10,201的
conTeanew = pymysql.connect(host="172.16.70.20",user="rd_user",password="NTHXDF7czYwi",port=3306,database='teanew')
conTalk = connTeanew = pymysql.connect(host="172.16.70.20",user="rd_user",password="NTHXDF7czYwi",port=3306,database='talk')
sqlTea = "SELECT talk.id FROM talk.teacher talk INNER JOIN talkplatform_teacher.teacher platform ON talk.id = platform.id where talk.is_full_time in (8,10,201) and talk.status='on' and talk.is_use=1 and talk.is_black=0 ORDER BY talk.id asc;"

cur = conTalk.cursor()
cur.execute(sqlTea)
obtSqltmp = cur.fetchall()
cur.close()

obtSql = Trans().tupletolist(obtSqltmp)
obtSqlSet = set(obtSql)
print(obtArrsSet)
print(obtSqlSet)

# 获取两个名单都存在的老师id
obts = obtSqlSet.intersection(obtArrsSet)
print("最终都存在的数据：",obts)
