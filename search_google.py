import requests
import json
from tools import BaseSearch
from tools import Item


class GoogleSearch(BaseSearch):
    def __init__(self, query, proxy_address, destination):
        super(GoogleSearch, self).__init__(query, destination)
        self.proxy_address = proxy_address
        self.reqeust_url = "https://www.google.com/complete/search?client=psy-ab&hl=zh-CN&q=" + str(self.query)

    def run(self):
        proxy_dict = None
        if self.proxy_address:
            proxy_dict = {
                "http": self.proxy_address,
                "https": self.proxy_address
            }
        r = requests.get(self.reqeust_url, proxies=proxy_dict)
        json_dic = json.loads(r.text)
        result_arr = []
        for item in json_dic[1]:
            result_arr.append(
                Item("https://www.google.com/search?q=%s", item[0], self.destination))
        return result_arr
