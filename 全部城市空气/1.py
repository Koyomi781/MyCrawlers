# -*- coding = utf-8 -*-
# @Time : 2022/11/22 14:55
# @Author : 刘鑫路
# @File : 1.py
# @Software: PyCharm

from selenium import webdriver
import time
import requests
import parsel

def get_data(city):
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=option)
    driver.get(f'https://www.aqistudy.cn/historydata/{city}')
    time.sleep(5)
    html_data = driver.page_source
    selector = parsel.Selector(html_data)
    trs = selector.css('div.container > div.row > div.col-md-8.col-sm-8.col-xs-12.col-lg-9 > table > tbody > tr').getall()
    for tr in trs[1:]:
        print(tr)
        # tr_info = parsel.Selector(tr)
        # tds = tr_info.css('td::text').get()
        # print(tds)


def get_citys():
    url = 'https://www.aqistudy.cn/historydata/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.52'
    }
    response = requests.get(url=url, headers=headers).text
    selector = parsel.Selector(response)
    city_list = selector.css('div.all > div.bottom > ul > div:nth-child(2) > li > a::attr(href)').getall()
    return city_list


if __name__ == '__main__':
    city_list = get_citys()
    print(city_list)
    for city in city_list:
        print(city)
        get_data(city)
        break