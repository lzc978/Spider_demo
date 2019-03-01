import sys
import time

import requests


def send_request(keyword):
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "275",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "tvfe_boss_uuid=fdabda8ec17e137c; RK=AR0C7YpPWJ; mobileUV=1_15b4b943b61_95e4c; pgv_pvi=2738445312; pac_uid=1_978940294; eas_sid=O1R5M3q4j0z54009t3p1N6G0R2; ptcz=058154a19c221164ee78e81dc266354fe0b73cf0743d92b7ccacaccfe32727e3; pgv_pvid=297027592; o_cookie=978940294; ptui_loginuin=190064345; fy_guid=4d45ddf8-0c67-41ca-85d9-51efe63a1bdb; qtv=a3b176d483442da4; qtk=q0QMZSCt5TrX9lMHzP7T+shuoJPqF2AYpbOc0WmnK9c7RqzlJrQK3uB8o5mhzKwfIct5qOiEYj8jtrjVb41fSApRgjnje9CU1fc6IjKewErt1Iw3Z0lR7HMhFJYLX1CPf2jrFxKNZu6ZebWlBexolw==; pgv_info=ssid=s9952684092; ts_last=fanyi.qq.com/; ts_refer=www.baidu.com/link; ts_uid=7767932671; openCount=1; gr_user_id=dba8f209-b863-4452-ab75-255be17b5a84; 9c118ce09a6fa3f4_gr_session_id=98b7884d-6730-4566-9490-57f5febb6adf; grwng_uid=e17e4ad0-7514-4ed1-9643-ec6b5e576c3b; 9c118ce09a6fa3f4_gr_session_id_98b7884d-6730-4566-9490-57f5febb6adf=true",
        "Host": "fanyi.qq.com",
        "Origin": "https://fanyi.qq.com",
        "Referer": "https://fanyi.qq.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    url = "https://fanyi.qq.com/api/translate"

    data = {
        "source": "auto",
        "target": "zh",
        "sourceText": keyword,
        "qtv": "a3b176d483442da4",
        "qtk": "q0QMZSCt5TrX9lMHzP7T+shuoJPqF2AYpbOc0WmnK9c7RqzlJrQK3uB8o5mhzKwfIct5qOiEYj8jtrjVb41fSApRgjnje9CU1fc6IjKewErt1Iw3Z0lR7HMhFJYLX1CPf2jrFxKNZu6ZebWlBexolw==",
        "sessionUuid": "translate_uuid{}".format(str(int(time.time() * 1000))),  # 添加时间戳(破解时间戳防盗链)
    }
    response = requests.post(url, data=data, headers=headers, timeout=3)
    result = response.json()
    print(result["translate"]["records"][0]["targetText"])

if __name__ == "__main__":
    send_request(sys.argv[1])