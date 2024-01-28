# -*- coding = utf-8 -*-
# @Time : 2022/11/24 18:42
# @Author : 刘鑫路
# @File : demo.py
# @Software: PyCharm

import parsel
import requests

url = 'http://www.12371.cn/special/gzsw/'
headers = {
    'Cookie': 'cna=qhoGHASQXDYCAXu1sLYaErC5',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
}
response = requests.get(url=url, headers=headers)
response.encoding = 'utf-8'
selector = parsel.Selector(response.text)
lis = selector.css('ul.showMoreNChildren > li > a').getall()
print(lis)
print(len(lis))