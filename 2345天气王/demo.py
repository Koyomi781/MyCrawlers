
import requests
import pandas as pd


def get_table(year, month):
    url = 'https://tianqi.2345.com/Pc/GetHistory'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
    }
    params = {
        'areaInfo[areaId]': 54511,
        'areaInfo[areaType]': 2,
        'date[year]': year,
        'date[month]': month
    }
    response = requests.get(url=url, headers=headers, params=params).json()['data']
    table = pd.read_html(response)[0]
    return table


def main():
    info_list = []
    for year in range(2011,2022):
        for month in range(1, 13):
            print(f'正在爬取第{year}年第{month}月的天气信息')
            table = get_table(year=year, month=month)
            info_list.append(table)
    return info_list


if __name__ == '__main__':
    info_list = main()
    data = pd.concat(info_list)
    data.to_excel('北京市近10年天气数据.xlsx', index=False)
