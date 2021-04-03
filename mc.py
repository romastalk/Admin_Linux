#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# Import the necessary packages
import cursesmenu as cm
# from cursesmenu.items import *

import paramiko

# Create the menu
menu = cm.CursesMenu("Admin Linux", "Subtitle")

# Create some items
# read PC list from file
def read():
    pc_dict = {}
    with open('info', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line:
            pc_details = line.split()
            pc_dict[pc_details[0]] = {'ip': pc_details[1], 'mac': pc_details[2]}

    return pc_dict

def ssh_ls_example():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='192.168.210.11', port=22, username='user', password='user2020')
# MenuItem is the base class for all items, it doesn't do anything when selected

menu_item = cm.items.FunctionItem("Подключение ", ssh_ls_example, [])

ip = "192.168.210.11"

def ping(ip):
    import os
    hostname = ip
    response = os.system("ping -c 4 " + hostname)
    if response == 0:
        print("Success")
    else:
        print("Not Success")




# A FunctionItem runs a Python function when selected
function_item = cm.items.FunctionItem("Ping " + ip, ping, [ip])

# A CommandItem runs a console command
command_item = cm.items.CommandItem("Run a console command",  "info.txt")

pc_dict = read()
pc_list = []#[f"PC #{i} IP: {pc_dict[i]['ip']} MAC: {pc_dict[i]['mac']}" for i in range(1, len(pc_dict) + 1)]

selection_menu = cm.SelectionMenu("")
for pc, detail in pc_dict.items():
    selection_menu.append_item(cm.items.CommandItem(f"PC #{pc} IP: {detail['ip']} MAC: {detail['mac']}", f"wakeonlan {detail['mac']}"))

# A SelectionMenu constructs a menu from a list of strings

# A SubmenuItem lets you add a menu (the selection_menu above, for example)
# as a submenu of another menu
submenu_item = cm.items.SubmenuItem("Выбор ПК для включения", selection_menu, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(menu_item)
menu.append_item(function_item)
menu.append_item(command_item)
menu.append_item(submenu_item)




# Finally, we call show to show the menu and allow the user to interact
menu.show()
cm.clear_terminal()
