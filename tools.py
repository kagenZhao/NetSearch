import json
import sys
from urllib.parse import quote


class Item:
    def __init__(self, url, title, destination):
        self.url = url % quote(title)
        self.title = title
        self.destination = destination

    def dic(self):
        return {"quicklookurl": self.url,
                "arg": self.url + " " + self.title,
                "autocomplete": "",
                "uid": self.url,
                "title": self.title,
                "subtitle": "Enter to search this by " + self.destination,
                "type": "default",
                "valid": True}


class BaseSearch:
    def __init__(self, query, destination):
        self.items = []
        self.query = query
        self.destination = destination

    def run(self):
        return []

    def setup(self, items):
        for item in items:
            self.items.append(item.dic())

    def send_back(self):
        self.setup(self.run())
        sys.stdout.write(json.dumps({"items": self.items}, ensure_ascii=False))
