# -*- coding = utf-8 -*-
# @Time : 2022/11/24 16:43
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

def TXTRead_Writeline():
    ms = open("demo.txt")   # 读取文件
    for line in ms.readlines():     # 逐行写入

        with open("test.doc", "a", encoding='UTF-8') as mon:

            mon.write(line)


if __name__ == '__main__':
    TXTRead_Writeline()