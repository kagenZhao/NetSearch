import json
import sys
import os
from xml.etree import ElementTree as ET
import requests
from PIL import Image
from io import BytesIO

class Args:
    def __init__(self, open_url, copy_text):
        self.open_url = open_url
        self.copy_text = copy_text


class Item:
    def __init__(self, title, url, subtitle, icon, arg, download_icon=None):
        self.url = url
        self.title = title
        self.subtitle = subtitle
        self.arg = arg
        self.icon = icon
        self.download_icon = download_icon

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
        if not self.download_icon:
            ET.SubElement(item_root, "icon").text = "%s/images/source/%s.png" % (os.path.dirname(__file__), self.icon)
        else:
            ET.SubElement(item_root, "icon").text = "%s/images/download/%s" % (os.path.dirname(__file__), self.download_icon)
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


def dowloadImage(url):
    img_name = (''.join(os.path.basename(url).split('.')[:-1])) + ".png"
    img_path = '%s/images/download/%s' % (os.path.dirname(__file__), img_name)
    if os.path.exists(img_path):
        return img_name
    img_response = requests.get(url)
    img = Image.open(BytesIO(img_response.content))
    img_width = img.size[0]
    img_height = img.size[1]
    img_width_half = img_width / 2.0
    img_height_half = img_height / 2.0
    img_min_size = min(img_width, img_height)
    img_min_size_half = img_min_size / 2.0
    img_new_size = (img_width_half - img_min_size_half, img_height_half - img_min_size_half, img_width_half + img_min_size_half, img_height_half + img_min_size_half)
    new_img = img.crop(img_new_size)
    new_img.save(img_path)
    return img_name
