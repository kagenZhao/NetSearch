import requests
from tools import *
from urllib.parse import quote


class GoogleSearch(BaseSearch):
    def __init__(self, query, proxy_address):
        super(GoogleSearch, self).__init__(query)
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
            args = Args("https://www.google.com/search?q=%s" % quote(item[0]), item[0])
            result_arr.append(Item(args.copy_text,
                                   args.open_url,
                                   "Enter to search this by Google",
                                   args))
        return result_arr
