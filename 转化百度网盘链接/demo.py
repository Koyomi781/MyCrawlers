# -*- coding = utf-8 -*-
# @Time : 2023/2/22 12:49
# @Author : 刘鑫路
# @File : app.py
# @Software: PyCharm

from selenium import webdriver
import pandas as pd


def set_cookies():
    driver.get('https://www.zx-cc.net/')
    input('登录后按回车')
    x = driver.get_cookies()
    for cookie in x:
        cookie_dict = {
            'domain': 'www.zx-cc.net',
            'name': cookie.get('name'),
            'value': cookie.get('value')
        }
        driver.add_cookie(cookie_dict)


def get_url(furl):
    driver.get(furl)
    return driver.current_url


def main():
    df = pd.read_excel('data.xlsx', index_col=0, sheet_name='zxcc', usecols="A:B")
    data = pd.DataFrame(df)
    print(df)
    length = len(df)
    # columns_list = df.columns.values
    # i = 0
    # for item in columns_list:
    #     print(f'[{i}]{item}')
    #     i += 1
    # x = input("请输入源地址列名所对应的序号：")
    # y = input("请输入百度链接需要填入的序号：")

    for i in range(0, length - 1):
        print(f'{i}/{length-1}')
        furl = df.iloc[i, 0]
        print(furl)
        if furl == '':
            i += 1
        else:
            try:
                bd_url = get_url(furl=furl)
                data.iloc[i, 1] = ''
                data.iloc[i, 1] = bd_url
            except:
                i += 1
    data.to_excel('info.xlsx', sheet_name='zxcc', index=False,)


if __name__ == '__main__':
    option = webdriver.ChromeOptions()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=option)
    # set_cookies()
    # option.add_argument('--headless')
    main()

