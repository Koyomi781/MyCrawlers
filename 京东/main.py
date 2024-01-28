
import requests
import parsel

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42',
    'Referer': 'https://item.jd.com/100000177760.html#comment'}
urls = ['https://list.jd.com/list.html?cat=9987%2C653%2C655&page={}&s=117&click=0'.format(i) for i in range(1, 2)]
for url in urls:
    res = requests.get(url=url, headers=headers)
    selector = parsel.Selector(res.text)
    price = selector.css('div.p-price > strong > i::text').get()
    xinghao = selector.css('div.p-name.p-name-type-3 > a > em::text').get()
    peizhi = selector.css('div.p-name.p-name-type-3 > span::text').get()
    pingjianumber = selector.css('div.p-commit > strong::text').get()
    dianpumingchen = selector.css('div.p-shop > span > a::text').get()
    products = []
    print(price, xinghao, peizhi, pingjianumber, dianpumingchen)
    print(peizhi)
    print(pingjianumber)
    break
