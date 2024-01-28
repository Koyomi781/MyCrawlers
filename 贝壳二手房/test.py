# -*- coding = utf-8 -*-
# @Time : 2022/8/29 12:18
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import parsel
import time
import os
import re
import json


def get_infourl(main_url, page):
    """
    获取每一个单位的url
    :param main_url: 主页
    :param page: 需要爬取的页数
    :return: url_list
    """
    url_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    for i in range(1, page+1):
        url = f'{main_url}/pg{i}/'
        response = requests.get(url=url, headers=headers).text
        selector = parsel.Selector(response)
        taget_url = selector.css('li.clear > a::attr(href)').getall()
        for t_utl in taget_url:
            print(t_utl)
            url_list.append(t_utl)
    return url_list


def get_pages(main_url):
    """
    获取需要爬取的页数
    :param main_url:输入的网址
    :return: pages
    """
    driver = webdriver.Chrome()
    driver.get(main_url)
    time.sleep(1)

    As = driver.find_elements(By.CSS_SELECTOR, 'div.page-box.fr > div > a')[-1].text
    if As == '下一页':
        pages = driver.find_element(By.CSS_SELECTOR, 'div.page-box.fr > div > a:nth-child(5)').text
    else:
        pages = As
    return int(pages)


def get_img_urls(url, proxies):
    img_url_list = []
    tname_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    n = 1
    while n <= 5:
        response = requests.get(url=url, headers=headers, proxies=proxies).text
        data_agent = re.findall('class="ke-agent-data" data-agent=\'(.*)\'', response)[0]
        json_data = json.loads(data_agent)
        tname = json_data['name']
        if tname not in tname_list:
            img_url = json_data['primaryProof']['img']
            tname_list.append(tname)
            img_url_list.append(img_url)
        n += 1
    return img_url_list, tname_list


def dowloadimg(tname_list, img_url_list, proxies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    for name, img_url in zip(tname_list, img_url_list):
        # print(f'正在保存[{name}]的信息')
        if name in os.listdir('data'):
            continue
        img_data = requests.get(url=img_url, headers=headers, proxies=proxies).content
        with open(f'data/{name}.png', mode='wb') as f:
            f.write(img_data)


def main(main_url, api):
    if 'data' not in os.listdir():
        os.mkdir('data')
    pages = get_pages(main_url=main_url)
    url_list = get_infourl(main_url=main_url, page=pages)
    all = len(url_list)
    n = 1
    for url in url_list:
        print(f'当前进度:{n}/{all}')
        proxies = get_proxies(api=api)
        img_url_list, tname_list = get_img_urls(url=url, proxies=proxies)
        dowloadimg(tname_list=tname_list, img_url_list=img_url_list, proxies=proxies)
        n += 1


def get_proxies(api):
    # x = requests.get(url='http://api.tianqiip.com/white/add?key=koyomi&brand=2&sign=87dcafe5f2c7038649f011bf3a1bc432&ip=27.191.242.180')
    data = requests.get(url=api).json()['data'][0]
    proxy = data['ip'] + ':' + str(data['port'])
    proxies = {
        'http://': proxy,
        'https://': proxy
    }
    return proxies


if __name__ == '__main__':
    main_url = 'https://su.ke.com/ershoufang/wuzhong/'
    api = 'http://api.tianqiip.com/getip?secret=16p2p590mgzb2gn2&num=1&type=json&port=1&time=3&sign=87dcafe5f2c7038649f011bf3a1bc432'
    get_proxies(api=api)
    main(main_url=main_url, api=api)



