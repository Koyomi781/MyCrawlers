# -*- coding = utf-8 -*-
# @Time : 2022/10/30 13:26
# @Author : 刘鑫路
# @File : 1.py
# @Software: PyCharm

import datetime

def calculate(t1, t2):
    if t1 < t2:
        second = (t2 - t1).seconds
        minute = second / 60
    else:
        second = (t1 - t2).seconds
        minute = second / 60
    return minute


if __name__ == '__main__':
    t1 = input("请输入t1(格式: 时:分):")
    t2 = input("请输入t2(格式: 时:分):")
    t1 = datetime.datetime.strptime(t1, "%H:%M")
    t2 = datetime.datetime.strptime(t2, "%H:%M")
    result = calculate(t1, t2)
    print(f"t1与t2之间相差{int(result)}分钟")
