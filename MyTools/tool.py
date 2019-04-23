# coding:utf-8
# usr/bin/python

import datetime
# import logging
import os
import uuid
import json
import time
import socket
import redis

import pymysql


def get_gostname():
    """获取主机名"""
    return socket.gethostname()


def get_hostip():
    """获取本机IP"""
    return socket.gethostbyname(get_gostname())


# 1.json与python的相互转换
def josn_loads(data):
    return json.loads(data)


def json_dumps(data):
    return json.dumps(data)


# 2.json文件格式的处理
class JsonFileTool(object):
    def __init__(self):
        pass


# 3.获取系统时间
def get_sys_time():
    """系统时间"""
    return int(time.time())


# 4.获取开机时间
def get_offet_time():
    with open('/proc/uptime', 'r') as f:
        data = f.read()
        return data


# 5.时间戳转字符串时间
def timestamp_to_datetime(timestamp):
    if not timestamp:
        return ''
    timeArray = time.localtime(timestamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


# 6.字符串时间转时间戳
def datetime_to_timestamp(str_t1):
    if not str_t1:
        return 0
    ts_t1 = time.mktime(time.strptime(str_t1, "%Y-%m-%d %H:%M:%S"))
    return int(ts_t1)


# 7.日志工具
# def get_log():
#     logger = logging.getLogger(__name__)
#
#     logger.setLevel(level=logging.INFO)
#     formatter = logging.Formatter('执行时间:%(asctime)s  文件名:%(filename)s - 日志级别:%(levelname)s - 错误内容:%(message)s')
#
#
#     handler = logging.FileHandler(os.path.join(r"E:\DevelopCode\python","log.txt"))
#     handler.setLevel(logging.INFO)
#     handler.setFormatter(formatter)
#
#     console = logging.StreamHandler()
#     console.setLevel(logging.INFO)
#     console.setFormatter(formatter)
#
#
#     logger.addHandler(handler)
#     logger.addHandler(console)

# 8.函数执行时间装饰器\

def count_time(func):
    """统计函数执行时间"""

    def int_time(*args, **kwargs):
        start_time = datetime.datetime.now()  # 程序开始时间
        func()
        over_time = datetime.datetime.now()  # 程序结束时间
        total_time = (over_time - start_time).total_seconds()
        print('程序共计%s秒' % total_time)

    return int_time


# 9.单例模式装饰器
def Singleton(cls):
    """单例模式装饰器"""
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


# 11.rsa加密解密
class RsaObject(object):
    def __int__(self):
        pass


class MysqlObject(object):

    def __init__(self,host,port,user,passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.conn = pymysql.connect(host='127.0.0.1',
                               port=3306,
                               user='root',
                               passwd='199331',
                               db='test',
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.conn.cursor()

    def ping(self):
        return self.conn.ping(reconnect=True)

    def read(self, *args):
        params = [*args]
        count = self.cursor.execute('sql', params)
        data = self.cursor.fetchall()
        self.conn.commit()
        return count, data

    def __del__(self):
        self.cursor.close()
        self.conn.close()

# 13.redis操作工具
class RedisObject(object):
    def __int__(self, host='localhost', port=6379, password=None):
        self.host = host
        self.port = port
        self.password = password
        self.r = redis.Redis(host=self.host, password=self.password, port=self.port, decode_responses=True)

    def set(self, key, value):
        """
        ex，过期时间（秒）
        px，过期时间（毫秒）
        nx，如果设置为True，则只有name不存在时，当前set操作才执行
        xx，如果设置为True，则只有name存在时，当前set操作才执行
        :param key:
        :param value:
        :return:
        """
        self.r.set(key, value, ex=None, px=None, nx=False, xx=False)

    def setnx(self, key, value):
        """
        添加:只有key不存在时，执行设置操作
        :param key:
        :param value:
        :return:
        """
        self.r.setnx(key, value)

    def setex(self, key, value, time):
        """
        设置过期时间
        :param key:
        :param value:
        :param time: 过期时间,秒
        :return:
        """
        self.r.setnx(key, value)

    def read(self, key):
        return self.r.get(key)

    def delete(self, key):
        self.r.delete(key)


def get_uuid():
    """获取唯一字符串"""
    return uuid.uuid1()


def get_datetime_now():
    """获取年月日时间"""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    a = get_offet_time()
    print(a, type(a))
