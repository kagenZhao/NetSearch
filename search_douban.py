import requests
from tools import *
from urllib.parse import quote


class DouBanSearch(BaseSearch):
    def __init__(self, query):
        super(DouBanSearch, self).__init__(query)
        self.reqeust_url = "https://movie.douban.com/j/subject_suggest?q=" + str(self.query)

    def runDefault(self):
        result_arr = []
        args = Args("https://movie.douban.com/subject_search?search_text=%s&cat=1002" % quote(self.query), self.query)
        result_arr.append(Item(args.copy_text,
                               args.open_url,
                               '豆瓣搜索 "%s"' % self.query,
                               "douban_icon",
                               args))
        return result_arr

    def run(self):
        headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
        r = requests.get(self.reqeust_url, headers=headers)
        result_arr = []
        for item in r.json():
            item_type = item["type"]
            args = Args(item["url"], item["title"])
            img_name = dowloadImage(item["img"])
            if item_type == "movie":
                result_arr.append(Item('%s (%s)(%s)' % (item["title"], item["sub_title"], item["year"]),
                                       args.open_url,
                                       '查看 "%s" 的影评' % item["title"],
                                       "douban_icon",
                                       args,
                                       download_icon=img_name))
            elif item_type == "celebrity":
                result_arr.append(Item('%s (%s)' % (item["title"], item["sub_title"]),
                                       args.open_url,
                                       '查看 "%s" 的主页' % item["title"],
                                       "douban_icon",
                                       args,
                                       download_icon=img_name))
        return result_arr
