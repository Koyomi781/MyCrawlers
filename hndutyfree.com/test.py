# -*- coding = utf-8 -*-
# @Time : 2022/8/27 9:36
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

import requests
import json
import csv
import threading
import datetime
import tkinter as tk
import tkinter.ttk
import os


def get_response(html_url):
    """
    获取响应
    :param html_url:
    :return: 响应体
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Mobile Safari/537.36 Edg/104.0.1293.63'
    }
    response = requests.get(url=html_url, headers=headers)
    return response


def get_goods_url_list(key):
    """
    传入关键词获取商品详情页的链接
    :param key: 数字关键字
    :return: goods_url_list 所有商品的详情页链接组成的列表
    """
    cate_list = []
    goods_url_list = []
    url_1 = f'https://service.cdfhnms.com/mini/findCategoryListById?categoryId={key}'
    response = get_response(html_url=url_1).text
    selectors = json.loads(response)['data']['children']
    for num_1 in selectors:
        big_cate = selectors[f'{num_1}']['parent']['cnName']  # 大分类
        selector = selectors[f'{num_1}']['children']
        for num_2 in selector:
            ID = selector[f'{num_2}']['parent']['categoryId']
            small_cate = selector[f'{num_2}']['parent']['cnName']  # 小分类
            url_2 = f'https://service.cdfhnms.com/mini/findGoodsList?categoryId={ID}&keyword=&pageSize=1000&goodsId='
            json_data = get_response(html_url=url_2).json()
            goods_list = json_data['data']['list']
            for goods in goods_list:
                goods_id = goods['goodsId']  # 商品id
                cate = big_cate + '>' + small_cate  # 分类
                goods_url = f'https://service.cdfhnms.com/mini/findGoodsDetailByIdAlways?goodsId={goods_id}'
                cate_list.append(cate)
                goods_url_list.append(goods_url)
    return goods_url_list, cate_list


def get_now_time():
    now_time = datetime.date.today()
    return now_time


def get_goods_info(goods_url, sort, file_name):
    """
    根据商品详情页的url获取其详情信息
    :param goods_url: 一个商品的详情页链接
    :param sort: 分类
    :param file_name: 文件名字 用来打开文件
    :return:
    """
    f = open(file_name, mode='a', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(f)
    goods_info = []
    goods_data = get_response(html_url=goods_url).json()['data']
    # 判断有货没货
    count = int(goods_data['count'])
    if count == 1:
        state = '有'
    else:
        state = '无'
    pd_name = goods_data['productName']     # 商品名称
    salesPrice = goods_data['salesPrice']       # 售价
    estimatePrice = goods_data['estimatePrice']     # 预估价
    try:
        brand = goods_data['brand']['chineseName']      # 品牌
    except:
        brand = '无'
    try:
        activityLabels = goods_data['activityLabels'][0]  # 活动
    except:
        activityLabels = '暂无活动'
    # 将获取到的信息放入到列表中方便保存
    goods_info.append(pd_name)          # 商品名称
    goods_info.append(brand)            # 品牌
    goods_info.append(sort)             # 分类
    goods_info.append(state)            # 有货/无货
    goods_info.append(salesPrice)       # 售价
    goods_info.append(estimatePrice)    # 预估价
    goods_info.append(activityLabels)   # 活动
    csv_writer.writerow(goods_info)


def multi(kw, file_name):
    id_dic = {
        '护肤': '1',
        '彩妆': '41',
        '香氛': '66'
    }
    key = id_dic[f'{kw}']   # 数字关键字

    url_list, sort_list = get_goods_url_list(key=key)
    threads = []
    for info_url, sort in zip(url_list, sort_list):
        threads.append(threading.Thread(target=get_goods_info, args=(info_url, sort, file_name)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def main():
    step.insert('insert', '保存中请稍后' + '\n')
    now_time = get_now_time()
    kw = key_word.get()     # 中文关键字
    # 创建data
    if 'data' not in os.listdir():
        os.mkdir('data')
    # 判断
    if f'[{now_time}]{kw}.csv' in os.listdir('data'):
        os.remove(f'data/[{now_time}]{kw}.csv')
    # 创建文件
    file_name = f'data/[{now_time}]{kw}.csv'
    f = open(file_name, mode='w', encoding='utf-8-sig', newline='')
    fieldnames = ['商品名称', '品牌', '分类', '有货/无货', '售价', '预估价', '活动']
    csv_writer = csv.writer(f)
    csv_writer.writerow(fieldnames)
    f.close()

    multi(kw=kw, file_name=file_name)
    step.insert('insert', '保存完成' + '\n')
    root.update()


def thread_it():
    t = threading.Thread(target=main)
    t.setDaemon(True)
    t.start()


# 打开保存路径
def openfile():
    cation = os.getcwd()
    os.startfile(cation + '//data')


# ======开始制作软件==========
root = tk.Tk()
root.title('cdf商品数据获取')
root.geometry('400x170+550+250')

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
save = tk.Button(text='保存', command=lambda: thread_it())
save.grid(row=1, column=3)

# 打开保存位置按钮
op = tk.Button(text='打开保存位置', command=openfile)
op.grid(row=1, column=4)

step = tk.Text(root, width=40, height=5, font=("SimHei", 15))
step.place(x=200, y=110, anchor='center')

# # 提示框
# sign = qt.Label(root, font=("黑体", 15))
# sign.place(x=10, y=70)

root.mainloop()



