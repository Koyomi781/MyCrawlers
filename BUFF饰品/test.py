# -*- coding = utf-8 -*-
# @Time : 2023/3/1 16:10
# @Author : 刘鑫路
# @File : app.py
# @Software: PyCharm
import requests
buff = f'https://buff.163.com/api/market/goods?game=csgo&page_num=1&search=★ Hand Wraps | CAUTION! (Factory New)&use_suggestion=0&_=1677654234581'
headers2 = {
    'cookie': '_ntes_nuid=044fc29fb6c228b64b3eab8cf4dceb5c; _ns=NS1.2.1615389503.1637460795; Device-Id=gXePD7uyyI5aQ0qCIjAE; _ga=GA1.2.2074291467.1651754919; NTES_P_UTID=C9MwE0PZsiNIMuNlk7cpSUQwyl0DIT46|1653283165; vjuids=3305d552f.182fbee1175.0.2cfa32e041fdb; vjlast=1662084060.1662084060.30; vinfo_n_f_l_n3=754aba44480edfc9.1.4.1649468585258.1664156136927.1664156263663; _ntes_nnid=044fc29fb6c228b64b3eab8cf4dceb5c,1668299820008; P_INFO=15373505183|1677654182|1|netease_buff|00&99|null&null&null#heb&130600#10#0|&0||15373505183; remember_me=U1102510716|GWSW14sMLdGC1ThYhLoej2FkRYqxVcsg; session=1-zEOtYLAtlEzbxVBSEZtPG3mF87omZ9JJnoniksIpLC4k2037933348; Locale-Supported=zh-Hans; game=csgo; csrf_token=IjExNjNiMzIwNzY5MjdiMGY1MjA5OWRjZmRiYjI4NzkzYmNjNmJiYzMi.FuC_dQ.myVdKk2Dvguf0h7n9LQEY1CM89w'
}
r = requests.get(url=buff, headers=headers2)
print(r.text)
sell_min_price = r.json()['data']['items'][0]['sell_min_price']
print(sell_min_price)