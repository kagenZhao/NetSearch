import requests
import re
import json
from tools import BaseSearch
from tools import Item


class BaiduSearch(BaseSearch):
    def __init__(self, query, destination):
        super(BaiduSearch, self).__init__(query, destination)
        self.reqeust_url = "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?json=1&bs=s&wd=" + str(self.query)

    def run(self):
        r = requests.get(self.reqeust_url)
        pattern = re.compile("^window\.baidu\.sug\((.*?)\);$")
        match = pattern.match(r.text)
        json_dic = json.loads(match.group(1))
        result_arr = []
        for item in json_dic["s"]:
            result_arr.append(
                Item("https://www.baidu.com/s?ie=UTF-8&wd=%s", item, self.destination))
        return result_arr
