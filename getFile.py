# -*- coding: utf-8 -*-
import os
import sys
import time
from datetime import datetime, timedelta


def getArgs():
    if len(sys.argv) < 3:
        raise Exception("参数格式错误", "path time")
    return sys.argv


path = getArgs()[1]
time = float(int(getArgs()[2]) * 24 * 3600)


def getFile(path):
    list = []
    for fpathe, dirs, fs in os.walk(path):
        for f in fs:
            list.append(os.path.join(fpathe, f))
    return list


def getRecentFile(path):
    list = getFile(path)
    dir_list = sorted(list, key=lambda list: os.path.getmtime(list))
    return os.path.getmtime(list[-1])


def rmFile(path):
    list = getFile(path)
    print(list)
    recent_time = getRecentFile(path)
    print(recent_time)
    for i in list:
        if os.path.getmtime(list[list.index(i)]) - recent_time > time:
            print("result", list.index(i), os.path.getmtime(list.index(i)))


if __name__ == '__main__':
    rmFile(path)
