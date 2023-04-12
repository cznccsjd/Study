#coding:utf-8

import json
from datetime import datetime, date


class ModelExt(object):
    """
    copy from csdn:https://blog.csdn.net/stone0823/article/details/112344065
    Model extension, implementing `__repr__` method which returns all the class attributes
    """
    def __repr__(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]

        return json.dumps(fields, cls=DateFormate)

# 额外处理dict中的datetime格式数据，否则会报错：TypeError: Object of type datetime is not JSON serializable
class DateFormate(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder().default(obj)
