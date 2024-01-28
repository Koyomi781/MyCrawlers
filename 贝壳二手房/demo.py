# -*- coding = utf-8 -*-
# @Time : 2022/8/28 19:52
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


def get_imgurl(info_url, proxies):
    """
    获取每个图片的url
    :param info_url: 每个详情页的url
    :return: 所有图片url列表
    """
    tname_list = []
    img_url_list = []
    option = webdriver.ChromeOptions()
    option.add_argument(f"--proxy-server={proxies}")
    option.add_argument('--headless')
    driver = webdriver.Chrome(options=option)
    time.sleep(2)
    driver.get(info_url)
    driver.implicitly_wait(10)
    divs = driver.find_elements(By.CSS_SELECTOR, 'div.daikan_content > div.daikan_list')
    for div in divs:
        data = div.find_element(By.CSS_SELECTOR, 'div.item_title > div:nth-child(3)').get_attribute('data-list')
        url = re.findall('"img":"(.*)!', data)[0]
        name = div.find_element(By.CSS_SELECTOR, 'div.item_title > a.itemAgentName.LOGCLICK.CLICKDATA').text
        img_url_list.append(url)
        tname_list.append(name)
    return tname_list, img_url_list


def dowloadimg(tname_list, img_url_list, proxies):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    if 'data' not in os.listdir():
        os.mkdir('data')

    for name, img_url in zip(tname_list, img_url_list):
        # print(f'正在保存[{name}]的信息')
        img_data = requests.get(url=img_url, headers=headers, proxies=proxies).content
        with open(f'data/{name}.png', mode='wb') as f:
            f.write(img_data)



def main(main_url, proxies):
    page = get_pages(main_url=main_url)
    url_list = get_infourl(main_url=main_url, page=page)
    all = len(url_list)
    n = 1
    for url in url_list:
        print(f'当前进度:{n}/{all}')
        tname_list, img_url_list = get_imgurl(info_url=url, proxies=proxies)
        dowloadimg(tname_list=tname_list, img_url_list=img_url_list, proxies=proxies)
        n += 1
    time.sleep(0.5)


if __name__ == '__main__':
    main_url = 'https://su.ke.com/ershoufang/dongshan1/'
    proxies = ''
    main(main_url=main_url, proxies=proxies)











