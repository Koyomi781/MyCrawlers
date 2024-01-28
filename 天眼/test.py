# -*- coding = utf-8 -*-
# @Time : 2022/11/30 17:07
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

import requests

url = 'https://www.tianyancha.com/search?key=%E4%B8%AD%E5%9B%BD%E8%8A%82%E8%83%BD%E7%8E%AF%E4%BF%9D%E9%9B%86%E5%9B%A2%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62'
}
response = requests.get(url=url, headers=headers).text
print(response)