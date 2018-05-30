import requests
from tools import *
from urllib.parse import quote


class JingDongSearch(BaseSearch):
    def __init__(self, query):
        super(JingDongSearch, self).__init__(query)
        self.reqeust_url = "https://dd-search.jd.com/?terminal=pc&newjson=1&ver=2&zip=1&curr_url=www.jd.com%2F&key=" + str(
            self.query)

    def runDefault(self):
        result_arr = []
        args = Args("https://search.jd.com/Search?keyword=%s" % quote(self.query), self.query)
        result_arr.append(Item(args.copy_text,
                               args.open_url,
                               "Enter to search this by JingDong",
                               "jingdong_icon",
                               args))
        return result_arr

    def run(self):
        headers = {
            "Referer": "https://www.jd.com/"
        }
        r = requests.get(self.reqeust_url, headers=headers)
        json_arr = json.loads(r.text)
        result_arr = []
        for item in json_arr:
            if "key" in item:
                args = Args("https://search.jd.com/Search?keyword=%s" % quote(item["key"]), item["key"])
                result_arr.append(Item(args.copy_text,
                                       args.open_url,
                                       "Enter to search this by JingDong",
                                       "jingdong_icon",
                                       args))
        return result_arr
