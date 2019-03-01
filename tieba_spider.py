"""
https://tieba.baidu.com/f?kw=%E4%B8%89%E5%92%8C%E5%A4%A7%E7%A5%9E&pn=50
"""
import requests


class BaiduSpider(object):
    """
    百度贴吧爬虫
    """

    def __init__(self):
        # 固定url
        self.base_url = "https://tieba.baidu.com/f?"
        # 请求报头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }
        self.keyword = input("请输入查询关键字：")
        self.start_page = int(input("请输入查询起始页码："))
        self.end_page = int(input("请输入查询结束页码："))


    def send_request(self, params):
        response = requests.get(self.base_url, params=params, headers=self.headers, timeout=3)
        result = response.content
        return result

    @staticmethod
    def params_response(self):
        pass

    def save_data(self, filename, result):
        print("[INFO] : {}".format(filename))
        with open(filename, "wb") as f:
            f.write(result)
    
    def main(self):
        # 迭代起始页到结束页
        for page in range(self.start_page, self.end_page + 1):
            pn = (page - 1) * 50
            params = {
                "kw": self.keyword,
                "pn": pn
            }
            try:
                result = self.send_request(params)
                filename = self.keyword + str(page) + ".html"
                self.save_data(filename, result)
            except Exception as e:
                print("[ERROR] : {}".format(e))


if __name__ == "__main__":
    spider = BaiduSpider()
    spider.main()