

import sys
from search_baidu import BaiduSearch
from search_taobao import TaobaoSearch
from search_google import GoogleSearch
from search_jingdong import JingDongSearch
from tools import BaseSearch


if __name__ == '__main__':
    query_type = sys.argv[1]
    query = " ".join(sys.argv[2:])
    if query_type == "baidu":
        BaiduSearch(query, "Baidu").send_back()
    elif query_type == "taobao":
        TaobaoSearch(query, "Taobao").send_back()
    elif query_type == "google":
        proxy_address = sys.argv[2]
        query = " ".join(sys.argv[3:])
        GoogleSearch(query, proxy_address, "Google").send_back()
    elif query_type == "jingdong":
        JingDongSearch(query, "JingDong").send_back()
    else:
        BaseSearch(query, "Default").send_back()
