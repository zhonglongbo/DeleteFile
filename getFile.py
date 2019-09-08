# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime, timedelta


def getArgs():
    for i in range(1, len(sys.argv)):
        print('参数 %s: %s' % (i, sys.argv[i]))
    return str(sys.argv)


path = getArgs()[1]


def getFile(path):
    print(path)
    list = []
    for fpathe, dirs, fs in os.walk(path):
        for f in fs:
            list.append(os.path.join(fpathe, f))
    return list


def getRecentFile(path):
    list = getFile(path)
    list.sort(key=lambda fn: os.path.getmtime(path + fn) if not os.path.isdir(path + fn) else 0)
    # 获取文件时间
    d = datetime.datetime.fromtimestamp(os.path.getmtime(path + list[-1]))
    print('最后改动的文件是' + list[-1] + "，时间：" + d.strftime("%Y-%m-%d %H-%M-%S"))


def rmFile(path):
    list = getFile(path)
    recent_time = getRecentFile(path)
    for i in list:
        if os.path.getmtime(list.index(i)) - recent_time > timedelta(days=30):
            print list.index(i), os.path.getmtime(list.index(i))

if __name__ == '__main__':
    getArgs()
    rmFile(path)