import requests
from tools import *
from urllib.parse import quote


class TaobaoSearch(BaseSearch):
    def __init__(self, query):
        super(TaobaoSearch, self).__init__(query)
        self.reqeust_url = "https://suggest.taobao.com/sug?code=utf-8&q=" + str(self.query)

    def run(self):
        r = requests.get(self.reqeust_url)
        json_dic = json.loads(r.text)
        result_arr = []
        for item in json_dic["result"]:
            args = Args("https://s.taobao.com/search?q=%s" % quote(item[0]), item[0])
            result_arr.append(Item(args.copy_text,
                                   args.open_url,
                                   "Enter to search this by TaoBao",
                                   args))
        return result_arr
