# -*- coding = utf-8 -*-
# @Time : 2022/9/18 17:16
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

import requests
import pandas as pd
import json
import parsel
import re
import csv
import time
import random


def get_data(url):
    """
    获取响应
    :param url:传入详情页url
    :return: json_data 字典信息
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42'
    }
    response = session.get(url=url, headers=headers).text
    selector = parsel.Selector(response)

    try:
        script = re.findall('\<script type="application\/ld\+json"\>([\s\S]*?)</script>', response)[0]
    except:
        pass
    sc = re.sub('\n', '', script)
    json_data = json.loads(sc)

    # __________________获取数据
    try:
        area = re.findall('<span class="pl">制片国家/地区:</span>(.*)<br/>', response)[0]     # 制片国家/地区:
    except:
        area = '/'
    try:
        lau = re.findall('<span class="pl">语言:</span>(.*)<br/>', response)[0]                # 语言
    except:
        lau = '/'
    try:
        date_ar = re.findall('<span property="v:initialReleaseDate".*>(.*)</span>', response)[0]
        try:
            date = date_ar.split('(')[0]        # 上映日期
            cont = date_ar.split('(')[1]
            contry = cont.replace(')', '')      # 对应国家
        except:
            date = date_ar
            contry = area
    except:
        date = '-'
        contry = '-'

    try:
        other = re.findall('<span class="pl">又名:</span> (.*)<br/>', response)[0]            # 别名
    except:
        other = '-'
    try:
        IMDb = re.findall('<span class="pl">IMDb:</span> (.*)<br>', response)[0]             # IMDb
    except:
        IMDb = '-'

    try:
        title = re.findall('<span property="v:itemreviewed">(.*)</span>', response)[0]
        year = re.findall('<span class="year">\((.*)\)</span>', response)[0]
    except:
        title = '-'
        year = '-'

# 种类
    try:
        sort = re.findall('<span property="v:genre">(.*?)</span> ', response)
        genre = '/'.join(sort)
        try:
            if sort == None:
                genre_list = json_data['genre']
                genre = ','.join(genre_list)
        except:
            genre = '-'

    except:
        genre = '-'

# 导演
    try:
        directors = selector.css('#info > span:nth-child(1) > span.attrs a::text').getall()
        director = '/'.join(directors)
        try:
            if director == None:
                directors = json_data['director']
                dir_list = []
                for direct in directors:
                    name = direct['name'].split(' ')[0]
                    dir_list.append(name)
                director = '/'.join(dir_list)
        except:
            director = '-'
    except:
        director = '-'

# 演员
    try:
        actors = selector.css('#info > span.actor > span.attrs a::text').getall()
        actor = '/'.join(actors)
        try:
            if actors == None:
                actors = json_data['actor']
                ac_list = []
                for act in actors:
                    name_2 = act['name'].split(' ')[0]
                    ac_list.append(name_2)
                actor = '/'.join(ac_list)
        except:
            actor = '-'
    except:
        actor = '-'

# 编剧
    try:
        authors = selector.css('#info > span:nth-child(3) > span.attrs a::text').getall()
        author = '/'.join(authors)
        try:
            if authors == None:
                authors = json_data['author']
                at_list = []
                for aut in authors:
                    name_1 = aut['name'].split(' ')[0]
                    at_list.append(name_1)
                author = '/'.join(at_list)
        except:
            author = '-'
    except:
        author = '-'

    # 评分人数，和评分
    try:
        ratingValue = selector.css('div.rating_self.clearfix > strong::text').get()
        ratingCount = selector.css('div.rating_sum > a > span::text').get()
        try:
            if ratingValue == None:
                aggregateRating = json_data['aggregateRating']
                ratingValue = aggregateRating['ratingValue']
                ratingCount = aggregateRating['ratingCount']
        except:
            ratingValue = '-'
            ratingCount = '-'
    except:
        ratingValue = '-'
        ratingCount = '-'
    # title = json_data['name']                              # 电影名字
    # time = json_data['datePublished'].split('-')[0]        # 时间
    #
    # # 导演
    # directors = json_data['director']
    # dir_list = []
    # for direct in directors:
    #     name = direct['name'].split(' ')[0]
    #     dir_list.append(name)
    # director = '/'.join(dir_list)
    #
    # # 编剧
    # authors = json_data['author']
    # at_list = []
    # for aut in authors:
    #     name_1 = aut['name'].split(' ')[0]
    #     at_list.append(name_1)
    # author = '/'.join(at_list)
    #
    # # 主演
    # actors = json_data['actor']
    # ac_list = []
    # for act in actors:
    #     name_2 = act['name'].split(' ')[0]
    #     ac_list.append(name_2)
    # actor = '/'.join(ac_list)
    #
    # # 类型
    # genre_list = json_data['genre']
    # genre = ','.join(genre_list)
    #
    # aggregateRating = json_data['aggregateRating']
    # ratingValue = aggregateRating['ratingValue']    # 评分
    # ratingCount = aggregateRating['ratingCount']    # 评分人数
    info_list = [title, year, director, author, actor, genre, area, lau, date, contry, other, IMDb, ratingValue, ratingCount]

    return info_list


def get_url():
    df = pd.read_csv('data.csv')
    df_to_dit = df.to_dict()
    url_list = list(df['url'].values)
    return url_list


if __name__ == '__main__':
    url_list = get_url()
    All = len(url_list)
    session = requests.session()
    session.cookies.set('authentication', 'bid=KFRjKJ-9YuQ; ll="118093"; _vwo_uuid_v2=D67611027F0FCCD2A0A9EC91B8880842B|3bda578d422f84108c9eb4bf9c23dade; douban-fav-remind=1; ct=y; push_noty_num=0; push_doumail_num=0; dbcl2="262866269:3H5d6uNYqcA"; __utmv=30149280.26286; ap_v=0,6.0; __utma=30149280.525609298.1649156481.1663501642.1663546005.14; __utmz=30149280.1663546005.14.9.utmcsr=cn.bing.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1663546421%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.1383108815.1649156481.1663501642.1663546421.12; __utmb=223695111.0.10.1663546421; __utmz=223695111.1663546421.12.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ck=gyuJ; __utmc=30149280; __utmt=1; __utmb=30149280.10.10.1663546005; __utmc=223695111; _pk_id.100001.4cf6=2f3ecd0faf6fb802.1649156481.12.1663547005.1663504797.')
    f = open('info.csv', encoding='utf-8-sig', mode='a', newline='')
    csv_writer = csv.writer(f)
    head = ['电影名字', '时间', '导演', '编剧', '主演', '类型', '制片国家/地区', '语言', '上映时间', '上映时间对应国家', '别名', 'IMDB号', '豆瓣评分', '评分人数']
    csv_writer.writerow(head)
    i = 1
    for url in url_list:
        print(f'当前进度{i}/{All}')
        info_list = get_data(url=url)
        csv_writer.writerow(info_list)
        i += 1
        time.sleep(random.random())




