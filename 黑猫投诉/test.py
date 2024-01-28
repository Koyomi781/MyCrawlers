# -*- coding = utf-8 -*-
# @Time : 2022/8/25 17:46
# @Author : 刘鑫路
# @File : auto_start.py
# @Software: PyCharm

import requests
import re
import parsel

url = 'https://tousu.sina.com.cn/complaint/view/17360898294/'
headers = {
    'cookie': 'UOR=cn.bing.com,finance.sina.com.cn,; SINAGLOBAL=183.198.48.156_1649924918.777761; U_TRS1=0000008f.4dc259.62ddfbce.0567a2f3; SCF=AqLUA2-hf11g447Gnk5JGt5fzzkh2OLVU6jDMZZLSZiAEoPsq0utiKy1TKS4FBNXF_ILcsMcf1CTWl-z_07MAAk.; TOUSU-SINA-CN=; SUB=_2A25OA1kwDeRhGeFI71oS9ivMyjSIHXVtec34rDV_PUNbm9ANLVajkW9NfRjsWz7ufEGT4ERO7c2b0SA9e3Pgjme4; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFyh6g5.fyVBspcYE_LDbD35NHD95QNSoBRe0qfeh2RWs4DqcjPi--NiKLhiKLsi--fiK.Ni-20S02fS02t; ALF=1692949728; U_TRS2=0000008a.1e066202.63072961.d6f3bc7f; Apache=454155050471.2011.1661416428499; FSINAGLOBAL=183.198.48.156_1649924918.777761; ULV=1661416430009:3:1:1:454155050471.2011.1661416428499:1649925183916',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63'
}
response = requests.get(url=url, headers=headers).text
selector = parsel.Selector(response)
contents = selector.css('div.ts-d-item').getall()

content_1 = re.findall('<p>([\s\S]*?)</p>', contents[-1])[-2]
content = re.sub('\n', '', content)