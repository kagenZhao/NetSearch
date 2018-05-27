import requests
import json
from tools import BaseSearch
from tools import Item


class JingDongSearch(BaseSearch):
    def __init__(self, query, destination):
        super(JingDongSearch, self).__init__(query, destination)
        self.reqeust_url = "https://dd-search.jd.com/?terminal=pc&newjson=1&ver=2&zip=1&curr_url=www.jd.com%2F&key=" + str(self.query)

    def run(self):
        headers = {
            "Referer": "https://www.jd.com/"
        }
        r = requests.get(self.reqeust_url, headers=headers)
        json_arr = json.loads(r.text)
        result_arr = []
        for item in json_arr:
            if "key" in item:
                result_arr.append(
                    Item("https://search.jd.com/Search?keyword=%s", item["key"], self.destination))
        return result_arr
