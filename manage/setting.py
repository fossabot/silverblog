#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os
import time

from common import whiptail, file

dialog = whiptail.Whiptail()
dialog.height = 15
dialog.title = "SilverBlog settings tool"
system_config = {
    "Project_Name": "",
    "Project_Description": "",
    "Project_URL": "",
    "Author_Image": "",
    "Author_Name": "",
    "Author_Introduction": "",
    "Theme": "",
    "API_Password": "",
    "Paging": 10,
    "Time_Format": "%Y-%m-%d",
    "Rss_Full_Content": True,
    "Editor": "nano",
    "i18n": "en-US"
}
if os.path.exists("./config/system.json"):
    system_config = json.loads(file.read_file("./config/system.json"))

def setting_menu():
    while True:
        menu_list = ["Use the Setup Wizard", "Set up basic information", "Set up author information",
                     "Theme package manager", "Other settings",
                     "Exit"]
        result = dialog.menu("Please select an action", menu_list)
        if result == "Exit":
            exit(0)
        if result == "Use the Setup Wizard":
            setup_wizard()
            exit(0)
        if result == "Set up basic information":
            project_info()
        if result == "Set up author information":
            author_info()
        if result == "Theme package manager":
            theme_manage()
        if result == "Other settings":
            other_info()
        save_config()
        time.sleep(0.5)
def save_config():
    file.write_file("./config/system.json", json.dumps(system_config, indent=4, sort_keys=False, ensure_ascii=False))

def theme_manage():
    from manage import theme
    dialog.title = "Theme package manager"
    menu_list = ["Install the theme", "Use the existing theme", "Upgrade existing Theme",
                 "Uninstall existing Theme"]
    result = dialog.menu("Please select an action", menu_list)
    theme_name = ""
    org_list = None
    if result == "Install the theme":
        install_menu = ["View list", "Enter the theme package name"]
        result = dialog.menu("Please select an action", install_menu)
        if result == "View list":
            org_list = theme.get_orgs_list()
            item_list = list()
            for item in org_list:
                item_list.append(item["name"])
            theme_name = dialog.menu("Please select the theme you want to install:", item_list)
        if result == "Enter the theme package name":
            theme_name = dialog.prompt("Please enter the theme package name:")
        if len(theme_name) != 0:
            theme_name = theme.install_theme(theme_name, org_list)
            if dialog.confirm("Do you want to enable this theme now?", "no"):
                system_config["Theme"] = theme_name
                if os.path.exists("./templates/{}/i18n".format(theme_name)):
                    system_config["i18n"] = setting_i18n(theme_name)
        return
    directories = theme.get_local_theme_list()
    theme_name = dialog.menu("Please select the theme to be operated:", directories)
    if result == "Use the existing theme":
        system_config["Theme"] = theme_name
        if os.path.exists("./templates/{}/i18n".format(theme_name)):
            system_config["i18n"] = setting_i18n(theme_name)
    if result == "Upgrade existing Theme":
        theme.upgrade_theme(theme_name)
    if result == "Uninstall existing Theme":
        theme.remove_theme(theme_name)


def setting_i18n(theme_name):
    dir_list = os.listdir("./templates/{0}/i18n".format(theme_name))
    show_list = list()
    for item in dir_list:
        if item.endswith(".json"):
            show_list.append(item.replace(".json", ""))
    return dialog.menu("Please select the i18n to be operated:", show_list)

def setup_wizard():
    project_info()
    author_info()
    other_info()
    if system_config["Theme"] == "":
        from manage import theme
        local_theme_list = theme.get_local_theme_list()
        if len(local_theme_list) != 0:
            system_config["Theme"] = dialog.menu("Please select the theme to be operated:", local_theme_list)
            return
        org_list = theme.get_orgs_list()
        item_list = list()
        for item in org_list:
            item_list.append(item["name"])
        theme_name = dialog.menu("Please select the theme you want to install:", item_list)
        system_config["Theme"] = theme.install_theme(theme_name, org_list)
    save_config()

def show_prompt(items):
    for item in items:
        system_config[item["name"]] = dialog.prompt("Please enter the {}:".format(item["info"]),
                                                    system_config[item["name"]])

def project_info():
    items = [{"name": "Project_Name", "info": "blog name"}, {"name": "Project_Description", "info": "blog description"},
             {"name": "Project_URL", "info": "blog access URL"}]
    show_prompt(items)
    new_password = dialog.prompt("Please enter the remote management tool password:", system_config["API_Password"],
                                 True)
    if len(new_password) != 0:
        import hashlib
        system_config["API_Password"] = json.dumps(
            {"hash_password": hashlib.md5(new_password.encode('utf-8')).hexdigest()})

def author_info():
    items = [{"name": "Author_Name", "info": "author name"},
             {"name": "Author_Introduction", "info": "author introduction"}]
    show_prompt(items)
    if dialog.confirm("Use Gravatar?", "no"):
        from manage import get
        system_config["Author_Image"] = get.get_gravatar(system_config["Author_Name"])
        return
    system_config["Author_Image"] = dialog.prompt("Please enter the author image:", system_config["Author_Image"])

def other_info():
    system_config["Paging"] = int(dialog.prompt("Please enter the paging:", str(system_config["Paging"])))
    items = [{"name": "Time_Format", "info": "time format"},
             {"name": "Editor", "info": "editor"}]
    show_prompt(items)
    system_config["Rss_Full_Content"] = dialog.confirm("Output full text Rss?", "yes")
