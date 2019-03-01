import json

import requests


def send_request():
    'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0'

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags="
    page = 0
    while True:
        params = {"start": page}
        response = requests.get(url, params=params, headers=headers)
        result = json.loads(response.content)
        if not result:
            break
        for movie in result.get("data"):
            print(*movie["directors"])  # 解包可以保证同一个列表的元素在同一行
        page += 20
    
    # page = 0
    # params = {"start": page, "limit": 100}
    # response = requests.get(url, params=params, headers=headers)
    # movies = response.json()
    # count = 0
    # for movie in movies.get("data"):
    #     count += 1
    #     # for name in movie["directors"]:
    #     #     print(name, end="\t")
    #     print(*movie["directors"])  # 解包可以保证同一个列表的元素在同一行
    #     # [print(name) for name in movie["directors"]]
    # print(count)

if __name__ == "__main__":
    send_request()
