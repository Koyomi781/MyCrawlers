# -*- coding = utf-8 -*-
# @Time : 2022/11/19 13:03
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

import requests
import parsel
import re

def get_from_country():
    url = 'http://www.china6636.com/dc'
    country_list = []
    response = requests.get(url=url, headers=headers).text
    selector = parsel.Selector(response)
    As = selector.css('div.col-md-6 > a').getall()
    for a in As:
        href = re.findall('<a href="(.*)">.*</a>', a)[0]
        title = re.findall('<a href=".*">(.*)到世界各国距离</a>', a)[0]
        li = [href, title]
        country_list.append(li)
    return country_list

def get_info_list(List):
    info_list = []
    for country in List:
        url = f'http://www.china6636.com{country[0]}'
        response = requests.get(url=url, headers=headers).text
        selector = parsel.Selector(response)
        As = selector.css('div.col-md-6 > a').getall()
        for a in As:
            href = re.findall('<a href="(.*)">.*</a>', a)[0]
            From = re.findall('<a href=".*">(.*)到.*</a>', a)[0]
            to = re.findall('<a href=".*">.*到(.*)的距離</a>', a)[0]
            url2 = f'http://www.china6636.com{href}'
            response = requests.get(url=url2, headers=headers).text
            gl = re.findall('<td>(.*)公里</td>', response)[0]
            yl = re.findall('<td>(.*)英里</td>', response)[0]
            hl = re.findall('<td>(.*)海里</td>', response)[0]
            info = [From, to, gl, yl, hl]
            print(From, to, gl, yl, hl)
            info_list.append(info)
        break
    return info_list


if __name__ == '__main__':
    headers = {
        'Referer': 'http://www.china6636.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'
    }
    country_list = get_from_country()
    info_list = get_info_list(List=country_list)
    print(info_list)
