
import requests
import re
import parsel
for i in range(0, 4):
    url = f'https://sem.tongji.edu.cn/case/?cat=6&paged={i}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
    }
    response = requests.get(url=url, headers=headers).text
    # print(response)
    hrefs = re.findall('<li><a href="(.*?)"', response)
    for href in hrefs:
        html_data = requests.get(url=href, headers=headers).text
        selector = parsel.Selector(html_data)
        title = selector.xpath('/html/body/div/div[4]/div[1]/h2/text()').get().strip()
        # print(html_data)
        try:
            author_1 = re.findall('<strong>作.*</strong>(.*?)<', html_data)[0]  #作者 里面可能有&nbsp;
            author = re.sub('&nbsp;', '', author_1)
        except:
            author = re.findall('</strong>.*?<span style="line-height: 1.8">(.*?)</span>', html_data)[0]
        try:
            almc = re.findall('<strong>案.名.*</strong>(.*?)<', html_data)[0]   #案例名称
        except:
            almc = selector.xpath('//*[@id="content"]/div[1]/p[2]/span/text()').get()

        alk = re.findall('<strong>案&nbsp.*</strong>(.*?)<', html_data)[0]  #案例库
        rksj = re.findall('<strong>入.*</strong>(.*)<', html_data)[0]    #入库时间
        rksj = re.sub('</span>', '', rksj)
        # zy = re.findall('<p><strong>摘.*</strong>(.*?)</p>', html_data)[0] #摘要 有的没有摘要进行判断
        try:
            zy = selector.xpath('//*[@id="content"]/div[1]/p[5]/text()').get()
        except:
            zy = selector.xpath('//*[@id="content"]/div[1]/p[5]/span/span/text()').get()
            if zy == None:
                # zy = selector.xpath('//*[@id="content"]/div[1]/p[5]/span/span[2]/text()').get()
                zy = str(re.findall('<span style="line-height: 1.8">(.*?)</span>', html_data))
        if zy == None:
            zy = ''
        # Abstract = re.findall('<p><strong>A.*</strong>(.*)</p>', html_data) #Abstract
        # Abstract = selector.xpath('//*[@id="content"]/div[1]/p[6]/text()').get()
        dic = {
            '标题': title,
            '作者': author,
            '案例名称': almc,
            '案例库': alk,
            '入库时间': rksj,
            '摘要': zy,
            # 'Abstract': Abstract
        }
        print(dic)
        # break

