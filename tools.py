import json
import sys


class Args:
    def __init__(self, open_url, copy_text):
        self.open_url = open_url
        self.copy_text = copy_text


class Item:
    def __init__(self, title, url, subtitle, arg):
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.arg = arg

    def dic(self):
        return {"quicklookurl": self.url,
                "arg": self.arg.open_url + "<|>" + self.arg.copy_text,
                "autocomplete": "",
                "uid": self.url,
                "title": self.title,
                "subtitle": self.subtitle,
                "type": "default",
                "valid": True}


class BaseSearch:
    def __init__(self, query):
        self.items = []
        self.query = query

    def runDefault(self):
        return []

    def run(self):
        return []

    def setup(self, items):
        self.items.clear()
        for item in items:
            self.items.append(item.dic())

    def send_back(self):
        default_arr = self.runDefault()
        default_arr.extend(self.run())
        self.setup(default_arr)
        sys.stdout.write('\r' + json.dumps({"items": self.items}, ensure_ascii=False))
        sys.stdout.flush()

