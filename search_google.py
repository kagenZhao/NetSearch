import requests
from tools import *
from urllib.parse import quote


class GoogleSearch(BaseSearch):
    def __init__(self, query, proxy_address):
        super(GoogleSearch, self).__init__(query)
        self.proxy_address = proxy_address
        self.reqeust_url = "https://www.google.com/complete/search?client=psy-ab&hl=zh-CN&q=" + str(self.query)

    def runDefault(self):
        result_arr = []
        args = Args("https://www.google.com/search?q=%s" % quote(self.query), self.query)
        result_arr.append(Item(args.copy_text,
                               args.open_url,
                               "Enter to search this by Google",
                               "google_icon",
                               args))
        return result_arr

    def run(self):
        proxy_dict = None
        if self.proxy_address:
            proxy_dict = {
                "http": self.proxy_address,
                "https": self.proxy_address
            }
        r = requests.get(self.reqeust_url, proxies=proxy_dict)
        json_arr = json.loads(r.text)[1]
        result_arr = []
        for item in json_arr:
            args = Args("https://www.google.com/search?q=%s" % quote(item[0]), item[0])
            result_arr.append(Item(args.copy_text,
                                   args.open_url,
                                   "Enter to search this by Google",
                                   "google_icon",
                                   args))
        return result_arr
