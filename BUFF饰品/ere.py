
import requests
from mainwin import *
from PySide2.QtWidgets import QApplication, QMainWindow
import sys
import os
from threading import Thread
import time


class Mainwin(QMainWindow):
    def __init__(self):
        super().__init__()
        if 'data' not in os.listdir():
            os.mkdir('data')
        self.cation = os.getcwd()  # 获取当前文件路径
        self.proxies = {'http': 'http://127.0.0.1:7890', 'https': 'http://127.0.0.1:7890'}
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('饰品')
        self.ui.save.clicked.connect(self.get_item_list)   # 保存按钮
        self.cursot = self.ui.text.textCursor()             # 提示框
        self.show()

    # 打开保存路径
    def openfile(self):
        os.startfile(self.cation + '//data')

    # 打印提示
    def printf(self, mes):
        self.ui.text.append(mes)
        self.ui.text.moveCursor(self.cursot.End)

    def get_item_list(self):
        headers = {
            'Cookie': '_ga=GA1.1.1145133898.1677651733; locale=en; DJSP_UUID=1869bd5f2a23fea9b2099c17; SCRIPT_VERSION=29.31.02; Hm_lvt_1cb9c842508c929123cd97ecd5278a28=1677651734,1677652757; JSESSIONID=F644DF87551A63C5EBA3BEF779899E7D; DJSP_USER=fELYbixIZp%2BDvhTL2YPxaNi%2FXZvXEoFoB1fZO%2FsNtYlmRLfGDjJH7bxvZ%2FO4diGctSADtTstAs44fo1S6aVpc30psH7M2mjdSnHEpK0fyO0%3D; Hm_lpvt_1cb9c842508c929123cd97ecd5278a28=1677653040; _ga_TDF3LV246N=GS1.1.1677651733.1.1.1677653040.0.0.0',
            'Referer': 'https://www.etopfun.com/en/store/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57'
        }
        response = requests.get('https://www.etopfun.com/api/ingotitems/realitemback/orderlist.do?appid=730&page=1&rows=60&mark_name=&exterior=&quality=&rarity=&hero=&lang=en', proxies=self.proxies, headers=headers)
        pages = response.json()['datas']['pager']['pages']
        item_list = []
        for i in range(1, pages+1):
            url = f'https://www.etopfun.com/api/ingotitems/realitemback/orderlist.do?appid=730&page={i}&rows=60&mark_name=&exterior=&quality=&rarity=&hero=&lang=en'
            response = requests.get(url=url, proxies=self.proxies, headers=headers)
            lists = response.json()['datas']['list']
            for item in lists:
                name = item['name']
                ingot = item['ingot']
                buff = f'https://buff.163.com/api/market/goods?game=csgo&page_num=1&search={name}&use_suggestion=0&_=1677654234581'
                headers2 = {
                    'cookie': '_ntes_nuid=044fc29fb6c228b64b3eab8cf4dceb5c; _ns=NS1.2.1615389503.1637460795; Device-Id=gXePD7uyyI5aQ0qCIjAE; _ga=GA1.2.2074291467.1651754919; NTES_P_UTID=C9MwE0PZsiNIMuNlk7cpSUQwyl0DIT46|1653283165; vjuids=3305d552f.182fbee1175.0.2cfa32e041fdb; vjlast=1662084060.1662084060.30; vinfo_n_f_l_n3=754aba44480edfc9.1.4.1649468585258.1664156136927.1664156263663; _ntes_nnid=044fc29fb6c228b64b3eab8cf4dceb5c,1668299820008; Locale-Supported=zh-Hans; game=csgo; NTES_YD_SESS=Lp8gtKOlHQmL06QPIk8RlxfIH.pSLmRpkZs0yIjWTTzDv4jcvh2dqAq195U11qZfKkJk16b8A9n1n2jW5913XVTpdNuf4ghOPcxatp.wU0eXYsjQnI9.Rd4QZynKNVS4sL2cF5.STqFCF48ghvtHSNxh8A9QpTmzVSJCorwGFZShXVFwzRRpfPSpUF89Pv7fg7LJ.3DcAi8k4vSsdhc0sS0vAOJNt.X21uX8Zp8uEryOK; S_INFO=1677654182|0|0&60##|15373505183; P_INFO=15373505183|1677654182|1|netease_buff|00&99|null&null&null#heb&130600#10#0|&0||15373505183; remember_me=U1102510716|GWSW14sMLdGC1ThYhLoej2FkRYqxVcsg; session=1-jmcRaNSzHs6X8_d9C-HW9Ap5-4pdo54vgStis7nrUMNP2037933348; csrf_token=IjZmNmNmZDhkZDY2N2VkNGY0ZDc5MjE4ZTBmMTVkMDE0ZTU1ZjQyY2Qi.FuCKYA.nTqjoD-Qbxeij8LmTmA53aEJYBs'
                }
                r = requests.get(url=buff, proxies=self.proxies, headers=headers2)
                sell_min_price = r.json()['data']['items'][0]['sell_min_price']
                List = [name, ingot, sell_min_price]
                print(List)
                item_list.append(List)
                time.sleep(0.8)
        return item_list

    def main(self):
        item_list = self.get_item_list()
        print(item_list)

    def main_threading(self):
        thread = Thread(
            target=self.main,
        )
        thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Mainwin()
    sys.exit(app.exec_())