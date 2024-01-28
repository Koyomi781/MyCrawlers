# -*- coding = utf-8 -*-
# @Time : 2022/10/21 17:03
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm
import random

import pandas as pd
import requests
import urllib.parse
import csv
import time

def get_id(kw):
    url = f'https://rest.uniprot.org/uniprotkb/search?fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Corganism_name%2Clength&query=%28{kw}%29%20AND%20%28reviewed%3Atrue%29%20AND%20%28model_organism%3A9606%29'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
    }
    try:
        response = requests.get(url=url, headers=headers, timeout=20).json()
        try:
            upt = response['results'][0]['primaryAccession']
        except:
            upt = '/'
    except:
        upt = '/'
    return upt


def main():
    df = pd.read_csv('data.csv')
    df_to_dit = df.to_dict()
    f = open('info.csv', mode='a', encoding='UTF-8', newline='')
    csv_writer = csv.writer(f)
    ingredient = list(df['ingredient'].values)
    n = 1
    for igt in ingredient:
        try:
            kw = urllib.parse.quote(igt)
            upt = get_id(kw=kw)
        except:
            upt = '/'
        print(n, igt, upt)
        csv_writer.writerow([igt, upt])
        n += 1
        time.sleep(1)


if __name__ == '__main__':
    main()