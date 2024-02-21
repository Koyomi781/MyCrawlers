# -*- coding = utf-8 -*-
# @Time : 2022/10/21 12:38
# @File : auto_start.py
# @Software: PyCharm

import requests
import urllib.parse
import pprint


# keyword = 'Prostaglandin G/H synthase 1'
keyword = urllib.parse.quote('Beta-lactamase')
keyword.replace('/', '%2F')
print(keyword)

url = f'https://rest.uniprot.org/uniprotkb/search?fields=accession%2Creviewed%2Cid%2Cprotein_name%2Cgene_names%2Corganism_name%2Clength&query=%28{keyword}%29%20AND%20%28reviewed%3Atrue%29%20AND%20%28model_organism%3A9606%29'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'
}
response = requests.get(url=url, headers=headers).json()
print(response)
for i in response['results']:
    primaryAccession = i['primaryAccession']
    print(primaryAccession)