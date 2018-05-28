import requests
import re
from tools import *
from urllib.parse import quote


class BaiduSearch(BaseSearch):
    def __init__(self, query):
        super(BaiduSearch, self).__init__(query)
        self.reqeust_url = "https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su?json=1&bs=s&wd=" + str(self.query)

    def run(self):
        r = requests.get(self.reqeust_url)
        pattern = re.compile("^window\.baidu\.sug\((.*?)\);$")
        match = pattern.match(r.text)
        json_dic = json.loads(match.group(1))
        result_arr = []
        for item in json_dic["s"]:
            args = Args("https://www.baidu.com/s?ie=UTF-8&wd=%s" % quote(item), item)
            result_arr.append(Item(args.copy_text,
                                   args.open_url,
                                   "Enter to search this by Baidu",
                                   args))

        return result_arr
