# coding: utf-8
from sqlalchemy import CHAR, Column, Date, DateTime, Index, String, TIMESTAMP, Text, text
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

from SQLAlchemy.study_with_csdn_ext import ModelExt

Base = declarative_base()
metadata = Base.metadata


class User(Base, ModelExt):
    __tablename__ = 'user'
    __table_args__ = (
        Index('idx_inviteCostomer_addTime', 'invite_costomer', 'add_time'),
        Index('idx_inviteCostomer_lastTime', 'invite_costomer', 'last_time'),
        Index('idx_customId_isBuy', 'custom_id', 'is_buy')
    )

    id = Column(INTEGER(11), primary_key=True)
    user_name = Column(String(128), nullable=False, index=True)
    username_mask = Column(String(41), nullable=False, server_default=text("''"), comment='加密用户名')
    password = Column(String(48), nullable=False)
    real_name = Column(String(128))
    nick_name = Column(String(32))
    sex = Column(String(6))
    age = Column(TINYINT(4))
    skype_id = Column(String(32), index=True)
    study_goal = Column(String(56))
    country_code = Column(CHAR(6), server_default=text("'86'"), comment='国家区号')
    mobile = Column(String(17), index=True)
    mobile_mask = Column(CHAR(41), nullable=False, server_default=text("''"), comment='加密手机号')
    wechat = Column(String(100), nullable=False, server_default=text("''"), comment='微信号')
    trail_time = Column(DateTime, index=True, comment='Input课程有效期')
    level = Column(TINYINT(6), server_default=text("'0'"), comment='Output课程点数')
    current_level = Column(TINYINT(6))
    is_buy = Column(String(8), server_default=text("'free'"), comment='是否付费')
    buy_time = Column(DateTime, index=True)
    status = Column(String(12))
    add_time = Column(DateTime, index=True)
    ext_id = Column(String(56))
    remark = Column(Text)
    last_time = Column(TIMESTAMP, index=True, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    level_desc = Column(String(8))
    purpose_desc = Column(String(8))
    now_level = Column(TINYINT(4))
    from_ip = Column(String(32), index=True)
    qq = Column(String(16), index=True)
    follow = Column(String(2), server_default=text("'n'"))
    default_teach_type = Column(String(8))
    from_url = Column(String(256), index=True)
    parent_id = Column(INTEGER(11), index=True, server_default=text("'0'"))
    custom_id = Column(INTEGER(11), index=True, server_default=text("'0'"))
    invite_costomer = Column(INTEGER(11), index=True)
    occup = Column(TINYINT(4), server_default=text("'0'"), comment="人群定位(1 => '上班族',2 => '大学生',3 => '中学生',//兼容旧数据    4 => '小学生',    5 => '高中生',6 => '初中生',7 => '幼儿',100 => '其他')")
    grade = Column(TINYINT(1), server_default=text("'0'"), comment='年级：1:一年级 2:二年级  3:三年级 4:四年级 5:五年级 6:六年级 7初一,8初二,9初三,10初四(五四制),11高一,12高二,13高三')
    key_word = Column(String(64))
    province = Column(String(32))
    city = Column(String(32))
    mobile_code = Column(INTEGER(11), server_default=text("'0'"))
    is_check = Column(String(2), server_default=text("'n'"))
    is_trail = Column(String(2), nullable=False, server_default=text("'n'"), comment='是否体验')
    register_from = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    sina_weibo_id = Column(String(32), index=True)
    from_url_id = Column(INTEGER(11), nullable=False, index=True, server_default=text("'0'"))
    test_level = Column(TINYINT(4), server_default=text("'0'"))
    edm_flag = Column(TINYINT(1))
    user_addr = Column(String(256), comment='用户住址')
    post_num = Column(String(16), comment='邮政编码')
    is_bargain = Column(TINYINT(4), nullable=False, comment='å\xad¦å‘˜æ˜¯å\x90¦ç\xad¾å\x90ˆå\x90Œ')
    sign = Column(String(256), comment='ç”¨æˆ·ç\xad¾å\x90\x8d')
    user_type = Column(TINYINT(4), server_default=text("'1'"), comment='人群定位 默认1成人用户 2少儿用户 3成人转少儿用户')
    birthday = Column(Date, index=True, comment='ç”Ÿæ—¥')
    avatar = Column(String(256), comment='头像')
    avatar_oss_fid = Column(String(256), nullable=False, server_default=text("''"), comment='存于阿里云OSS上的头像文件对应的fid')
    is_staff = Column(String(2), server_default=text("'n'"), comment='内部员工账号/测试账号')
    is_new = Column(INTEGER(11))
    mk = Column(String(32), server_default=text("''"), comment='手机加密')
    school_en_course = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='学校开设英语课情况 1：是 2：否')
    learn_foreign_teacher = Column(TINYINT(1), nullable=False, server_default=text("'0'"), comment='外教课经历 1：上过 2：否')
    district = Column(INTEGER(11), nullable=False, server_default=text("'0'"), comment='区')
