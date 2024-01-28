# -*- coding = utf-8 -*-
# @Time : 2022/10/14 23:32
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm
import requests
import parsel
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


def first_urls(url, headers):
    furl_list = []
    ftitle_list = []
    response = requests.get(url=url, headers=headers)
    selector = parsel.Selector(response.text)
    lis = selector.css('ul.lst > li')
    for li in lis:
        href = li.css('a::attr(href)').get()
        turl = f'https://www.netcarshow.com{href}'
        first_title = li.css('a::text').get()
        furl_list.append(turl)
        ftitle_list.append(first_title)
    return furl_list, ftitle_list

def sec_urls(furl, headers):
    surl_list = []
    stitle_list = []
    response = requests.get(url=furl, headers=headers)
    selector = parsel.Selector(response.text)
    lis = selector.css('ul.lst > li')
    for li in lis:
        href = li.css('a::attr(href)').get()
        turl = f'https://www.netcarshow.com{href}'
        stitle = li.css('a::text').get()
        stitle_list.append(stitle)
        surl_list.append(turl)
    return stitle_list, surl_list

def img_urls(surl, headers):
    urls = []
    response = requests.get(url=surl, headers=headers)
    with open('1.html', mode='w', encoding='utf-8', newline='') as f:
        f.write(response.text)
        f.close()
    drive.get(os.path.abspath('1.html'))
    time.sleep(0.5)
    divs = drive.find_elements(By.CSS_SELECTOR, '#gh > div > div.Pi')
    for div in divs:
        href = div.find_element(By.CSS_SELECTOR, 'a:nth-child(1)').get_attribute('href')
        urls.append(href)
    urls.pop()
    return urls

def main():
    url = 'https://www.netcarshow.com/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
        'referer': 'https://www.netcarshow.com/'
    }
    furl_list, ftitle_list = first_urls(url=url, headers=headers)
    i = 0
    All = len(furl_list)
    for furl, ftitle in zip(furl_list, ftitle_list):
        stitle_list, surl_list = sec_urls(furl=furl, headers=headers)
        for stitle, surl in zip(stitle_list, surl_list):
            urls = img_urls(surl=surl, headers=headers)
            l = []
            print(f'正在保存 {ftitle}-{stitle}')
            for iurl in urls:
                l.append(ftitle)
                l.append(stitle)
                l.append(iurl)
                csv_writer.writerow(l)
                l = []
        print(f'{i}/{All}')
        i += 1


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    drive = webdriver.Chrome(options=option)
    f = open('data.csv', mode='a', encoding='utf-8', newline='')
    csv_writer = csv.writer(f)
    main()