# -*- coding: utf-8 -*-
# @Time    : 2023/12/13 20:26
# @Name    : test.py
# @email   : liu78103@gmail.com
# @Author  : 刘鑫路

import requests
import fake_useragent
import time

while True:
    url = 'https://app.gsxt.gov.cn/gsxt/corp-query-entprise-info-primaryinfoapp-entbaseInfo-37B4115839A9D8AAF485CC84DAABFEE287C721C721C7A2E204DF39799F799F79A248AECB7C9ADA3C30D6305515CE-1702468861422.html?nodeNum=130000&entType=9500&sourceType=W'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    response = requests.post(url=url, headers=headers)
    print(response.text)
    time.sleep(1)