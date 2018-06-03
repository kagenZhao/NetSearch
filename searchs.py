

import sys
from search_baidu import BaiduSearch
from search_taobao import TaobaoSearch
from search_google import GoogleSearch
from search_jingdong import JingDongSearch
from search_cococapods import CocoapodsSearch
from search_douban import DouBanSearch
from tools import BaseSearch


if __name__ == '__main__':
    query_type = sys.argv[1]
    query = " ".join(sys.argv[2:])
    if query_type == "baidu":
        BaiduSearch(query).send_back()
    elif query_type == "taobao":
        TaobaoSearch(query).send_back()
    elif query_type == "google":
        proxy_address = sys.argv[2]
        query = " ".join(sys.argv[3:])
        GoogleSearch(query, proxy_address).send_back()
    elif query_type == "jingdong":
        JingDongSearch(query).send_back()
    elif query_type == "cocoapods":
        CocoapodsSearch(query).send_back()
    elif query_type == "douban":
        DouBanSearch(query).send_back()
    else:
        BaseSearch(query).send_back()
