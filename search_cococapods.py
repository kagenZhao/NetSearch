import requests
from tools import *


class CocoapodsSearch(BaseSearch):
    def __init__(self, query):
        super(CocoapodsSearch, self).__init__(query)
        self.reqeust_url = "https://wbhhamhynm-3.algolianet.com/1/indexes/cocoapods/query?x-algolia-agent=Algolia" \
                           "%20for%20vanilla%20JavaScript%203.27.1&x-algolia-application-id=WBHHAMHYNM&x-algolia-api" \
                           "-key=4f7544ca8701f9bf2a4e55daff1b09e9"

    def run(self):
        r = requests.post(self.reqeust_url, data=json.dumps({"params": "query=%s" % self.query}))
        result_list = r.json()["hits"]
        result_arr = []
        for item in result_list:
            name = item["name"]
            version = item["version"]
            summary = item["summary"]
            if 'homepage' in item:
                homepage = item["homepage"]
            args = Args(homepage, "pod '%s', '~>%s'" % (name, version))
            result_arr.append(Item("%s(%s)" % (name, version),
                                   args.open_url,
                                   summary,
                                   "cocoapods_icon",
                                   args))
        return result_arr
