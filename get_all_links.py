import random
import requests
import json
import time
import pymongo


client = pymongo.MongoClient('localhost', 27017)
unsplash = client['unsplash']
alls = unsplash['alls']


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.802417300.1520735444; _gid=GA1.2.208065288.1521895241; _sp_ses.0295=*; googtrans=/en/zh-CN; _sp_id.0295=6fee24f5-b308-428b-b343-312af2e7276d.1520735445.3.1521896945.1520738935.10412ab4-828f-4d3e-9925-d8dd3b8ff93d'
}
# http://cn-proxy.com/ 每天更新
proxy_list = [
    'http://39.134.68.24:80',
    'http://61.160.190.146:8090',
    'http://114.55.0.166:8090',
    'http://39.134.68.19:80',
    'http://120.77.201.46:8080',
    'http://59.56.74.205:7777',
    'http://221.130.253.135:8090'

]
proxy_ip = random.choice(proxy_list)
proxies = {
    'http': proxy_ip
}


def get_urls():
    for num in range(101, 301):
        # time.sleep(3)
        url = 'https://api.unsplash.com/photos/?client_id=fa60305aa82e74134cabc7093ef54c8e2c370c47e73152f72371c828daedfcd7&page={}&per_page=30'.format(str(num))
        print(url)
        res = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        all_urls = json.loads(res.text)
        print(len(all_urls))
        for i in all_urls:
            author = i['user'].get('first_name')
            url = i['urls'].get('regular')
            date = i.get('created_at')
            h = i.get('height')
            w = i.get('width')
            print(author)
            print(url)
            print(h)
            print(w)
            print(date)
            data = {
                'author': author,
                'url': url,
                'time': date,
                'h': h,
                'w': w
            }
            alls.insert_one(data)
