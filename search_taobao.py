import requests
import json
from tools import BaseSearch
from tools import Item


class TaobaoSearch(BaseSearch):
    def __init__(self, query, destination):
        super(TaobaoSearch, self).__init__(query, destination)
        self.reqeust_url = "https://suggest.taobao.com/sug?code=utf-8&q=" + str(self.query)

    def run(self):
        r = requests.get(self.reqeust_url)
        json_dic = json.loads(r.text)
        result_arr = []
        for item in json_dic["result"]:
            result_arr.append(
                Item("https://s.taobao.com/search?q=%s", item[0], self.destination))
        return result_arr
