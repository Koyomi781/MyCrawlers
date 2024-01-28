# -*- coding = utf-8 -*-
# @Time : 2022/11/12 8:04
# @Author : 刘鑫路
# @File : demo.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import csv

def main():
    url = 'https://item.taobao.com/item.htm?spm=a230r.1.14.51.f91165b8eO0ARq&id=658290240704&ns=1&abbucket=14#detail'
    driver.implicitly_wait(5)
    driver.get(url)
    x = input('登录后按回车继续')
    driver.find_element(By.CSS_SELECTOR, '#J_TabBar > li:nth-child(2) > a').click()
    time.sleep(5)
    data_list = []
    for i in range(1, 4):
        lis = driver.find_elements(By.CSS_SELECTOR, 'div.tb-revbd > ul > li')
        for li in lis:
            content = li.find_element(By.CSS_SELECTOR, 'div.J_KgRate_ReviewContent.tb-tbcr-content').text
            print(content)
            comment = [content]
            data_list.append(comment)
        driver.find_element(By.CSS_SELECTOR, 'li.pg-next').click()
        time.sleep(5)
    return data_list

def save():
    f = open('data.csv', mode='a', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(f)
    data_list = main()
    for data in data_list:
        csv_writer.writerow(data)


if __name__ == '__main__':
    option = Options()
    option.add_experimental_option("detach", True)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(chrome_options=option)
    save()