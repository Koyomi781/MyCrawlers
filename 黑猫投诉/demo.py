# -*- coding = utf-8 -*-
# @Time : 2022/8/25 14:14
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import re
import csv
import random
import parsel


def craw(url):
    headers = {
        'cookie': 'UOR=cn.bing.com,finance.sina.com.cn,; SINAGLOBAL=183.198.48.156_1649924918.777761; U_TRS1=0000008f.4dc259.62ddfbce.0567a2f3; SCF=AqLUA2-hf11g447Gnk5JGt5fzzkh2OLVU6jDMZZLSZiAEoPsq0utiKy1TKS4FBNXF_ILcsMcf1CTWl-z_07MAAk.; TOUSU-SINA-CN=; SUB=_2A25OA1kwDeRhGeFI71oS9ivMyjSIHXVtec34rDV_PUNbm9ANLVajkW9NfRjsWz7ufEGT4ERO7c2b0SA9e3Pgjme4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFyh6g5.fyVBspcYE_LDbD35NHD95QNSoBRe0qfeh2RWs4DqcjPi--NiKLhiKLsi--fiK.Ni-20S02fS02t; ALF=1692949728; U_TRS2=0000008a.1e066202.63072961.d6f3bc7f; Apache=454155050471.2011.1661416428499; FSINAGLOBAL=183.198.48.156_1649924918.777761; ULV=1661416430009:3:1:1:454155050471.2011.1661416428499:1649925183916',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
    }
    response = requests.get(url=url, headers=headers).text
    question = re.findall('<li><label>投诉问题：</label>(.*)</li> ', response)[0]       # 投诉问题
    date = re.findall('<span class="u-date">发布于 (.*)</span>', response)[0]          # 发布日期
    company = re.findall('data-sudaclick="complaint_company">(.*)</a>', response)[0]  # 投诉对象
    ask = re.findall('<li><label>投诉要求：</label>(.*)</li>', response)[0]             # 投诉要求

    selector = parsel.Selector(response)
    contents = selector.css('div.ts-d-item').getall()

    content_1 = re.findall('<p>([\s\S]*?)</p>', contents[-1])[-2]
    content = re.sub('\n', '', content_1)                                             # 投诉内容
    csv_writer.writerow([question, company, date, ask, content])
    print(question, company, date, ask)
    time.sleep(random.randint(0, 2))


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://tousu.sina.com.cn/company/view/?couid=6475684251")
    driver.maximize_window()
    print('请先登录')

    time.sleep(10)
    print('开始翻页')
    n = 1
    while n <= 50:
        js = "var q=document.documentElement.scrollTop=1000000000000000000000000000000"
        driver.execute_script(js)
        time.sleep(2)
        n += 1

    href_list = []
    seletors = driver.find_elements(By.CSS_SELECTOR, 'div.blk-l > div:nth-child(3) > div a.box:nth-child(2)')
    for seletor in seletors:
        href = seletor.get_attribute('href')
        href_list.append(href)
    print(len(href_list))

    f = open('南京银行.csv', encoding='utf-8-sig', mode='a', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['投诉问题', '投诉对象', '发布日期', '投诉要求', '投诉内容'])
    for url in href_list:
        craw(url)
















