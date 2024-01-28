# -*- coding = utf-8 -*-
# @Time : 2022/8/30 16:26
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

import requests
import parsel
import csv


def get_year_data(kw, url_list):
    global title
    global header
    info_list = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    for url in url_list:
        response = requests.get(url=url, headers=headers).text
        selector = parsel.Selector(response)
        header = selector.css('div.inner_box > table > thead > tr > th::text').getall()[0:kw]     # 表头
        trs = selector.css('div.inner_box > table > tr').getall()
        title = selector.css('body > div.area > h1 > span::text').get()
        for tr in trs:
            selector_tr = parsel.Selector(tr)
            td_list = selector_tr.css('td::text').getall()[0:kw]
            info_list.append(td_list)
    return info_list, title, header


def save(info_list, title, header, year):
    print(f'正在保存第{year}年的数据')
    f = open(f'[{year}]{title}.csv', encoding='utf-8-sig', mode='a', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    for info in info_list:
        csv_writer.writerow(info)


def get_year(id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    url = f'http://quotes.money.163.com/trade/lsjysj_{id}.html?year=2022&season=1'
    response = requests.get(url=url, headers=headers).text
    selector = parsel.Selector(response)
    year_list = selector.css('#date > select:nth-child(1) > option::text').getall()
    return year_list


def get_urls(year):
    """
    获取一年所有季度的url
    :param year: 一个年份
    :return: 一个年份所有季度的url
    """
    url_list = []
    for season in range(1, 5):
        turl = f'http://quotes.money.163.com/trade/lsjysj_{id}.html?year={year}&season={season}'
        url_list.append(turl)
    return url_list


def main(id, kw):
    year_list = get_year(id=id)
    for year in year_list:
        url_list = get_urls(year=year)
        info_list, title, header = get_year_data(kw=kw, url_list=url_list)
        save(info_list=info_list, title=title, header=header, year=year)


if __name__ == '__main__':
    kw = 5          # 提取的字段数
    id = 601567
    main(id=id, kw=kw)
    # main(url=url, kw=kw)
