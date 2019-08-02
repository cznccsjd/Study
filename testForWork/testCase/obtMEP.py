#coding:utf-8
'''
测试体验课分配模型3,的造数据脚本
'''

stu_id = 800033014
stu_mep = 67
stu_grade = 2
app_id = 51007616

# 初始化学生的mep和grade_type（手动插入数据）
sqlStuMep = "INSERT INTO teanew.user_trial_rate (user_id, mep, grade_type, appoint_id) VALUES (%d, %d, %d, %d);" %(stu_id, stu_mep, stu_grade, app_id)



# 初始化老师的mep和grade_type（手动插入数据）


# 初始化free_appoint_in_ac表[刷课表]，写入学生的mep和grade_type




