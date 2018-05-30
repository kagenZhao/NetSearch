import requests
import re
from tools import *
from urllib.parse import quote


class BaiduSearch(BaseSearch):
    def __init__(self, query):
        super(BaiduSearch, self).__init__(query)
        self.reqeust_url = "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?json=1&bs=s&wd=" + str(self.query)

    def runDefault(self):
        result_arr = []
        args = Args("https://www.baidu.com/s?ie=UTF-8&wd=%s" % quote(self.query), self.query)
        result_arr.append(Item(args.copy_text,
                               args.open_url,
                               "Enter to search this by Baidu",
                               "baidu_icon",
                               args))
        return result_arr

    def run(self):
        r = requests.get(self.reqeust_url)
        pattern = re.compile("^window\.baidu\.sug\((.*?)\);$")
        match = pattern.match(r.text)
        json_arr = json.loads(match.group(1))["s"]
        result_arr = []
        for item in json_arr:
            args = Args("https://www.baidu.com/s?ie=UTF-8&wd=%s" % quote(item), item)
            result_arr.append(Item(args.copy_text,
                                   args.open_url,
                                   "Enter to search this by Baidu",
                                   "baidu_icon",
                                   args))

        return result_arr
