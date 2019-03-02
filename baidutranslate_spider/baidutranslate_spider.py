"""
mobile baidu translate 
移动端百度翻译新增了sign字段，该字段根据前端传入的待翻译内容，由前端js脚本生成一个唯一sign值
"""
__author__ = 'Braveheart'


import random
import json
import re

import requests
import js2py


class BaiduTranslateSpider(object):
    """
    mobile baidu 翻译
    """
    def __init__(self):
        self.url_index = "https://fanyi.baidu.com/"
        self.url_api = "https://fanyi.baidu.com/basetrans"
        # UserAgent池（伪造多个浏览器信息 --轮询?--）
        USER_AGENT_LIST = [
            # iOS 8.0 Safari
            "Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A365 Safari/600.1.4",
            # Android 4.4.4 Chrome
            # "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36"，
            # Android 6.0 Chrome
            # "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36",
            # IOS 11.0 Safari
            "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        ]
        # 随机从列表中选择一个元素并返回
        user_agent = random.choice(USER_AGENT_LIST)
        self.headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "96",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "PSTM=1490856010; BIDUPSID=6386898AEAC684C0252A4C35569A9B1F; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=4760D3D796565AC26DA92A3CD6893A97:FG=1; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1447_21094_28584_28557_28518_28414; delPer=0; PSINO=7; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22it%22%2C%22text%22%3A%22%u610F%u5927%u5229%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1551446524,1551446669,1551499950; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1551446523,1551446669,1551499891,1551499950; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1551501403; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1551501403",
            "Host": "fanyi.baidu.com",
            "Origin": "https://fanyi.baidu.com",
            "Referer": "https://fanyi.baidu.com/",
            "User-Agent": user_agent,
            "X-Requested-With": "XMLHttpRequest",
        }
        self.keyword = input("请输入需要翻译的文本：")

    def send_request(self):
        # get百度翻译主页，是为了得到token
        # req_get = requests.get(self.url_index, headers=self.headers)
        # token = re.search(r"token: '(.*?)',", req_get.text, re.S).group(1)

        # 使用js2py在python中运行js代码并得到sign
        # 实例化js解释对象
        run_js = js2py.EvalJs()
        # 调用js对象编码
        run_js.execute(self.get_js())
        sign = run_js.e(self.keyword)

        data = {
            "query": self.keyword,
            "from": "zh",
            "to": "en",
            "token": "519477ac7aa72b946a3b7d9e3190461e",
            "sign": sign,
        }
        response = requests.post(self.url_api, headers=self.headers, data=data)
        # result = response.json()
        result = json.loads(response.content.decode())
        # print(result)
        return result

    def params_response(self):
        pass

    def save_data(self, result):
        dst = result["trans"][0]["dst"]
        print(dst)
        with open("translate.txt", "a") as f:
            f.write(dst + '\n')

    @staticmethod
    def get_js():
        with open('sign.js', 'r', encoding='utf-8') as f:
            return f.read()

    def main(self):

        result = self.send_request()
        self.save_data(result)

if __name__ == "__main__":
    spider = BaiduTranslateSpider()
    spider.main()