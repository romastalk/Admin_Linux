#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import cursesmenu as cm

import paramiko

menu = cm.CursesMenu("Linux Admin Automation", "Меню", show_exit_option=False)

def read():
    pc_dict = {}
    with open('info', 'r') as file:
        lines = file.readlines()

    for line in lines:
        if line:
            pc_details = line.split()
            pc_dict[pc_details[0]] = {'ip': pc_details[1], 'mac': pc_details[2]}
    print(pc_dict)
    return pc_dict

pc_dict = read()
pc_list = []

selection_menu_wake = cm.SelectionMenu("")
selection_menu_ping = cm.SelectionMenu("")
for pc, detail in pc_dict.items():
    selection_menu_wake.append_item(cm.items.CommandItem(f"PC #{pc} IP: {detail['ip']} MAC: {detail['mac']}", f"wakeonlan {detail['mac']}"))
    selection_menu_ping.append_item(cm.items.CommandItem(f"PC #{pc} IP: {detail['ip']} MAC: {detail['mac']}", f"ping -c 4 {detail['ip']}"))

wake_submenu = cm.items.SubmenuItem("Включить ПК из списка", selection_menu_wake, menu)

ping_submenu = cm.items.SubmenuItem("Статус ПК", selection_menu_ping, menu)

command_item = cm.items.CommandItem("Выполнить скрипт", "info.txt")

menu.append_item(wake_submenu)
menu.append_item(ping_submenu)
menu.append_item(command_item)
menu.append_item(cm.items.MenuItem(text="Выход", should_exit=True))

menu.show()
cm.clear_terminal()
