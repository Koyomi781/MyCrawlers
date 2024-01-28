
import urllib.parse
import requests
import time
import re
import csv


def get_data(key_world, page):
    f = open('HM数据.csv', mode='a', encoding='utf-8-sig', newline='')
    fieldnames = ['标题', '作者', '发布时间', '播放量', '点赞量', '评论量', '收藏量']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()

    for i in range(1, page+1):
        url = f'https://api.bilibili.com/x/web-interface/search/all/v2?__refresh__=true&_extra=&context=&page={i}&page_size=42&order=&duration=&from_source=&from_spmid=333.337&platform=pc&highlight=1&single_column=0&keyword={key_world}&preload=true&com2co=true'
        headers = {
            'cookie': '_uuid=B2E85B104-18C3-210E2-6C108-ED6A424D41CD30194infoc; buvid3=16B5678C-2B7E-4B34-9E95-38B7E191576A167641infoc; rpdid=|(J~k|JmJkR)0J\'uYJY~|ml|u; LIVE_BUVID=AUTO1016373090094953; video_page_version=v_old_home; CURRENT_BLACKGAP=0; CURRENT_QUALITY=80; nostalgia_conf=-1; buvid_fp_plain=undefined; is-2022-channel=1; DedeUserID=178360345; DedeUserID__ckMd5=86e0d314766084c0; b_ut=5; blackside_state=0; fingerprint3=e48b28cf359008df614de86e0489f8e4; hit-dyn-v2=1; i-wanna-go-back=2; SESSDATA=43b3aa99%2C1674185597%2Cb662e%2A71; bili_jct=085410fd6a91d4cffc19bd51961fe6d6; fingerprint=1fbc3bdbe161dc2422a85ebc1a8d7bc6; buvid_fp=1fbc3bdbe161dc2422a85ebc1a8d7bc6; buvid4=27194272-B7C3-530C-E91A-9CBEEDFA483F12547-022012117-Gql7v0cPJj1O%2BXdMYnty1w%3D%3D; PVID=2; bp_video_offset_178360345=686440055715135526; innersign=0; b_lsid=8CA3104CA_18233C9454F; b_timer=%7B%22ffp%22%3A%7B%22333.851.fp.risk_16B5678C%22%3A%2218233C94961%22%2C%22333.337.fp.risk_16B5678C%22%3A%2218233C965B1%22%7D%7D; CURRENT_FNVAL=80; sid=6ri2gqhu',
            'referer': 'https://search.bilibili.com/all?keyword=HM%E6%8A%B5%E5%88%B6%E6%96%B0%E7%96%86%E6%A3%89&from_source=webtop_search&spm_id_from=333.851',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.71'
        }
        response = requests.get(url=url, headers=headers).json()
        json_data = response['data']['result'][-1]['data']
        for data in json_data:
            arcurl = data['arcurl']     # 详情页
            author = data['author']     # 作者
            play = data['play']     # 播放量
            like = data['like']     # 点赞量
            review = data['review']  # 评论量
            favorites = data['favorites']    # 收藏量
            pubdate = data['pubdate']
            timeArray = time.localtime(pubdate)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)  # 发布时间
            title_1 = data['title']
            title = re.sub('<.*?>', '', title_1)
            # print(author, title, play, like, review, favorites, otherStyleTime)
            # with open('315老坛酸菜.csv', mode='a', encoding='utf-8-sig', newline='') as f:
            #     csv_writer = csv.writer(f)
            #     csv_writer.writerow([title, author, otherStyleTime, play, like, review, favorites])
            dic = {
                '标题': title,
                '作者': author,
                '发布时间': otherStyleTime,
                '播放量': play,
                '点赞量': like,
                '评论量': review,
                '收藏量': favorites
            }
            csv_writer.writerow(dic)


if __name__ == '__main__':
    page = int(input('请输入要爬取的页数，每页42条数据：'))
    world = input('请输入要搜索的关键词：')
    keyword = urllib.parse.quote(world)
    get_data(keyword, page)


