#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import paramiko

def menu():
    while True:
        print("1-Пинговать / 2-Вкл. ПК")
        type = int(input("Ответ: "))
        if type == 1:
            ping(ip)
        elif type == 2:
            wake_on_lan()
        elif type == 0:
            exit(0)

ip = "192.168.210.11"

def ping(ip):
    import os
    hostname = "192.168.210.11"
    response = os.system("ping -c 4 " + hostname)
    if response == 0:
        print("Success")
    else:
        print("Not Success")

menu()
