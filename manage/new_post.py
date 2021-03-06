import json
import time

import os.path
from xpinyin import Pinyin

from common import file, console
from manage import get

system_info = json.loads(file.read_file("./config/system.json"))

def get_name(name_input):
    p = Pinyin()
    name = name_input.replace(" ", "-")
    name = get.filter_name(name)
    return p.get_pinyin(name)

def new_post_init(config, independent=False):
    title = config["title"]
    name = get.filter_name(config["name"])
    if not os.path.exists("./document/{}.md".format(name)):
        editor = system_info["Editor"]
        os.system("{0} ./document/{1}.md".format(editor, name))
    post_info = {"name": name, "title": title, "time": time.time()}
    if not os.path.exists("./document/{}.md".format(name)):
        console.log("Error", "Cannot find [./document/{}.md] file".format(name))
        return
    if not independent:
        excerpt = get.get_excerpt("./document/{}.md".format(name))
        post_info["excerpt"] = excerpt

    write_json = post_info
    page_config = "./document/{}.json".format(name)

    if not independent:
        write_json = json.loads(file.read_file("./config/page.json"))
        write_json.insert(0, post_info)
        page_config = "./config/page.json"

    file.write_file(page_config, json.dumps(write_json, indent=4, sort_keys=False, ensure_ascii=False))

    console.log("Success", "Create a new article successfully!")
