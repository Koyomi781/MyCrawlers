# -*- coding = utf-8 -*-
# @Time : 2022/8/26 20:26
# @File : testdemo.py
# @Software: PyCharm

import requests
import json
import csv
import datetime
import os
import tkinter as tk
import tkinter.ttk
import threading


def get_url(kw, headers):
    global cate
    global productName
    global state
    global salesPrice
    global estimatePrice
    global labels
    categoryId_dic = {
        '护肤': '1',
        '彩妆': '41',
        '香氛': '66'
    }
    categoryId = categoryId_dic[f'{kw}']

    url_list = []
    url_1 = f'https://service.cdfhnms.com/mini/findCategoryListById?categoryId={categoryId}'  # 获取分类下的次分类 （面部护理）
    response = requests.get(url=url_1, headers=headers).text
    selectors = json.loads(response)['data']['children']
    # pprint.pprint(selectors)
    for num_1 in selectors:
        big_cate = selectors[f'{num_1}']['parent']['cnName']  # 大分类
        selector = selectors[f'{num_1}']['children']
        for num_2 in selector:
            small_cate = selector[f'{num_2}']['parent']['cnName']  # 小分类
            cate = big_cate + '>' + small_cate
            ID = selector[f'{num_2}']['parent']['categoryId']
            url_2 = f'https://service.cdfhnms.com/mini/findGoodsList?categoryId={ID}&keyword=&pageSize=1000&goodsId='
            json_data = requests.get(url=url_2, headers=headers).json()
            goods_list = json_data['data']['list']
            title = json_data['data']['title']
            for goods in goods_list:
                productName = goods['productName']  # 商品名称
                salesPrice = goods['salesPrice']  # 原价
                estimatePrice = goods['estimatePrice']  # 预估价
                goodsId = goods['goodsId']  # 商品id
                # goodsurl = f'https://mini.hndutyfree.com.cn/#/pages/publicPages/goodDetails/index?goodsId={goodsId}'
                try:
                    labels = goods['labels'][0]  # 活动
                except:
                    labels = '暂无活动'
                # 判断有货没货
                count = int(goods['count'])
                if count == 1:
                    state = '有'
                else:
                    state = '无'
                # 判断有无预估价
                if int(estimatePrice) == 0:
                    estimatePrice = salesPrice
                # 请求品牌
                url_3 = f'https://service.cdfhnms.com/mini/findGoodsDetailByIdAlways?goodsId={goodsId}'
                url_list.append(url_3)

    return url_list, productName, state, salesPrice, estimatePrice, labels, cate


def craw(url, headers, kw, now_time):
    with open(f'data/[{now_time}]{kw}.csv', mode='a', encoding='utf-8-sig', newline='') as file:
        csv_writer = csv.writer(file)
    try:
        brand = requests.get(url=url, headers=headers).json()['data']['brand']['chineseName']
    except:
        brand = ''

    data = {
        '商品名称': productName,
        '品牌': brand,
        '分类': cate,
        '有货/无货': state,
        '原价': salesPrice,
        '预估价': estimatePrice,
        '活动': labels,
        # '链接': goodsurl
    }
    print(data)
    csv_writer.writerow(data)


def multi(urls, headers, kw, now_time):
    threads = []
    for url in urls:
        threads.append(threading.Thread(target=craw, args=(url, headers, kw, now_time,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def main():
    kw = key_word.get()
    categoryId_dic = {
        '护肤': '1',
        '彩妆': '41',
        '香氛': '66'
    }
    categoryId = categoryId_dic[f'{kw}']
    # 获取当前时间作为文件名
    now_time = datetime.date.today()
    # 创建data
    if 'data' not in os.listdir():
        os.mkdir('data')
    # 判断
    if f'[{now_time}]{kw}.csv' in os.listdir('data'):
        os.remove(f'data/[{now_time}]{kw}.csv')
    # 写入表头
    f = open(f'data/[{now_time}]{kw}.csv', mode='a', encoding='utf-8-sig', newline='')
    fieldnames = ['商品名称', '品牌', '分类', '有货/无货', '原价', '预估价', '活动']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()

    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36 Edg/104.0.1293.63'
    }
    urls = get_url(kw=kw, headers=headers)[0]
    multi(urls=urls, headers=headers, kw=kw, now_time=now_time)


def openfile():
    cation = os.getcwd()
    os.startfile(cation + '//data')


# ======开始制作软件==========
root = tk.Tk()
root.title('cdf商品数据获取')
root.geometry('475x180+550+250')

blank = tk.Label(text=' ')
blank.grid(row=0, column=0)

text = tk.Label(text='请选择分类:', font=("黑体", 15))
text.grid(row=1, column=0)

# 设置下拉选项框
key_word = tk.StringVar()
com = tk.ttk.Combobox(textvariable=key_word)
com["value"] = ("护肤", "彩妆", "香氛")
com.grid(row=1, column=1)

# 设置可变变量，使函数可以调用这个变量

# it = qt.Entry(root, textvariable=key_word)
# it.grid(row=1, column=1)

# 保存按钮
save = tk.Button(text='保存', command=main)
save.grid(row=1, column=3)

# 打开保存位置按钮
op = tk.Button(text='打开保存位置', command=openfile)
op.grid(row=1, column=4)

step = tk.Text(root, width=40, height=5, font=("SimHei", 15))
step.place(x=200, y=110, anchor='center')


root.mainloop()
