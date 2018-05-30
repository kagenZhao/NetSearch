import json
import sys
import os
from xml.etree import ElementTree as ET

class Args:
    def __init__(self, open_url, copy_text):
        self.open_url = open_url
        self.copy_text = copy_text


class Item:
    def __init__(self, title, url, subtitle, icon, arg):
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.arg = arg
        self.icon = icon

    def xml(self):
        item_root = ET.Element("item",
                               uid=self.url,
                               arg=self.arg.open_url + "<|>" + self.arg.copy_text,
                               audocomplete=self.arg.copy_text)
        ET.SubElement(item_root, "title").text = self.title
        ET.SubElement(item_root, "text", type="copy").text = self.arg.copy_text
        ET.SubElement(item_root, "text", type="largetype").text = self.title
        ET.SubElement(item_root, "subtitle", mod="alt").text = 'Copy "%s" to clipboard' % self.arg.copy_text
        ET.SubElement(item_root, "subtitle").text = self.subtitle
        ET.SubElement(item_root, "icon").text = "%s/images/source/%s.png" % (os.path.dirname(__file__), self.icon)
        return item_root


        # return {"quicklookurl": self.url,
        #         "arg": self.arg.open_url + "<|>" + self.arg.copy_text,
        #         "autocomplete": "",
        #         "uid": self.url,
        #         "title": self.title,
        #         "subtitle": self.subtitle,
        #         "type": "default",
        #         "icon": "%s/images/source/%s.png" % (os.path.dirname(__file__), self.icon),
        #         "valid": True}


class BaseSearch:
    def __init__(self, query):
        self.items = ET.Element("items")
        self.query = query

    def runDefault(self):
        return []

    def run(self):
        return []

    def setup(self, items):
        self.items.clear()
        for item in items:
            self.items.append(item.xml())

    def send_back(self):
        default_arr = self.runDefault()
        default_arr.extend(self.run())
        self.setup(default_arr)
        sys.stdout.write(ET.tostring(self.items, encoding='unicode', method='xml'))
        sys.stdout.flush()

