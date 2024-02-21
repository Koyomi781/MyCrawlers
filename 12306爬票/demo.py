# -*- coding = utf-8 -*-
# @Time : 2022/11/10 15:25
# @File : demo.py
# @Software: PyCharm

from City import city
import requests
from mainui import *
from PySide2.QtWidgets import QApplication, QMainWindow
import sys
import numpy as np
import os


class Mainwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('车票查询')
        if 'data' not in os.listdir():
            os.mkdir('data')
        self.setWindowIcon(QIcon('data/111.ico'))
        self.ui.tableWidget.setColumnCount(12)      # 设置列数
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)      # 整行选中
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)       # 设置不可修改
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)    # 铺满控件
        self.ui.tableWidget.horizontalHeader().setDefaultSectionSize(94)     # 设置列宽
        self.ui.tableWidget.verticalHeader().setVisible(False)              # 隐藏行号
        self.ui.tableWidget.setHorizontalHeaderLabels(['车次', '出发时间', '到达时间', '耗时', '商务座', '一等座', '二等座', '软卧', '动卧', '硬卧', '硬座', '无座'])

        self.ui.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color: rgb(75, 20, 255);font:11pt '黑体';color: white;};")       # 设置表头格式

        # 绑定信号改变事件
        self.ui.GC.stateChanged.connect(lambda: self.write())
        self.ui.D.stateChanged.connect(lambda: self.write())
        self.ui.Z.stateChanged.connect(lambda: self.write())
        self.ui.T.stateChanged.connect(lambda: self.write())
        self.ui.K.stateChanged.connect(lambda: self.write())
        self.ui.pushButton.clicked.connect(self.click)

        self.show()
        # 检查当前信号状态
        self.check()

    def check(self):
        stat = []
        GC = self.ui.GC.isChecked()
        if GC == True:
            stat.append('G')
            stat.append('C')
        D = self.ui.D.isChecked()
        if D == True:
            stat.append('D')
        Z = self.ui.Z.isChecked()
        if Z == True:
            stat.append('Z')
        T = self.ui.T.isChecked()
        if T == True:
            stat.append('T')
        K = self.ui.K.isChecked()
        if K == True:
            stat.append('K')
        return stat

    def get_data(self):
        self.ui.tips.setText('')
        city_code = city()

        from_station = self.ui.from_station.text()
        to_station = self.ui.to.text()
        date = self.ui.date.text()

        # 获取车票信息
        try:
            # url = f"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={city_code[from_station]}&leftTicketDTO.to_station={city_code[to_station]}&purpose_codes=ADULT"
            url = f"https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={city_code[from_station]}&leftTicketDTO.to_station={city_code[to_station]}&purpose_codes=ADULT"
            print('1')
        except:
            self.ui.tips.setText('车站输入有误或无此车站')
            url = f"https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={city_code[from_station]}&leftTicketDTO.to_station={city_code[to_station]}&purpose_codes=ADULT"
        headers = {
            'Cookie': '_uab_collina=165239707992577884851946; JSESSIONID=EF542F2A0E60FD580989DE59C289D051; BIGipServerotn=1106248202.50210.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; BIGipServerpool_passport=31719946.50215.0000; RAIL_EXPIRATION=1652732051129; RAIL_DEVICEID=OaKvFzLuKrATtfWI3_R0pfcu0wNkK4EkAOJZkvBXVNRF1DhbCZjsGXCzRJcJ9jz64QqQ7kebUckkQZw3wUwOccZ7n7Jbogi21Yt3fWdMNr2TD1OG0qKzpINztCUc9Rt6aqG41c0GbUG8T6FJ7M1KbRD3YqoyXEPi; route=6f50b51faa11b987e576cdb301e545c4; _jc_save_fromStation=%u4FDD%u5B9A%u4E1C%2CBMP; _jc_save_toStation=%u6EE6%u6CB3%2CUDP; _jc_save_fromDate=2022-05-13; _jc_save_toDate=2022-05-13; _jc_save_wfdc_flag=dc',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        print(response)
        print(response.text)
        try:
            json_data = response.json()['data']['result']
        except:
            self.ui.tips.setText('超出预定日期！')
            json_data = response.json()['data']['result']
        # 获取车票数据
        data_list = []
        for index in json_data:
            info = index.split('|')
            num = info[3]  # 车次
            sort = num[0]   # 车型
            start_time = info[8]  # 出发时间
            arrive_time = info[9]  # 到达时间
            time_duration = info[10]  # 耗时
            business_seat = info[32] or '--'  # 商务座
            first_class_seat = info[31] or '--'  # 一等座
            second_class_seat = info[30] or '--'  # 二等座
            soft_sleep = info[23] or '--'  # 软卧
            pneumatic_sleep = info[33] or '--'  # 动卧
            hard_seat = info[29] or '--'  # 硬座
            no_seat = info[26] or '--'  # 无座
            info_list = [num, start_time, arrive_time, time_duration, business_seat, first_class_seat, second_class_seat, soft_sleep, pneumatic_sleep, hard_seat, hard_seat, no_seat]
            data_list.append(info_list)
            numpy_array = np.array(data_list)
            np.save('./data/log.npy', numpy_array)

    def click(self):
        # 删除上一次的数据
        if 'log.npy' in os.listdir('data'):
            os.remove('data/log.npy')
        self.get_data()
        self.write()

    def write(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        try:
            data_list = np.load('./data/log.npy')
        except:
            self.ui.tips.setText('无查询结果！')
            self.ui.tableWidget.setRowCount(0)
            self.ui.tableWidget.clearContents()
            data_list = []
        stat = self.check()
        items = []
        if len(stat) != 0:
            for data in data_list:
                if data[0][0] not in stat:
                    continue
                else:
                    items.append(data)
        else:
            items = data_list

        for i in range(len(items)):
            item = items[i]
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.ui.tableWidget.setItem(row, j, item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Mainwin()
    sys.exit(app.exec_())