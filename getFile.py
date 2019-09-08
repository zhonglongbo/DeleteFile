# -*- coding: utf-8 -*-
import datetime
import os
import sys
import time


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
    return os.path.getmtime(list[1]), list[1]


def rmFile(path):
    list = getFile(path)
    recent_time, recent_file = getRecentFile(path)
    print(recent_file, datetime.datetime.fromtimestamp(int(recent_time)).strftime("%Y-%m-%d %H:%M:%S"))
    for i in list:
        if recent_time - os.path.getmtime(list[list.index(i)]) > time:
            print("result", list[list.index(i)],
                  datetime.datetime.fromtimestamp(int(os.path.getmtime(list[list.index(i)]))).strftime(
                      "%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    rmFile(path)
