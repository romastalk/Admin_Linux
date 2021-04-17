#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import paramiko
from os import system

def connect(ip, username):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, port=22, username=username)
    return client


def exec(client, command):
    print(f'>>>>> Выполняем [{command.strip()}] <<<<<')
    stdin, stdout, stderr = client.exec_command(command, get_pty=True)
    exit_code = stdout.channel.recv_exit_status()
    for line in iter(stdout.readline, ""):
        print(line, end="")
    del stdin, stdout, stderr
    return exit_code


def execute_script(ip, username):
    with open('script', 'r') as file:
        lines = file.readlines()

    client = connect(ip=ip, username=username)

    system('clear')
    for line in lines:
        exec(client, line)
        print()
    client_close(client)
    input("Press 'Enter' to continue...")


def client_close(client):
    client.close()
    del client

example_mac = 'b4:2e:99:85:1e:45'

def wake_on_lan(mac):
    import os
    stream = os.popen('wakeonlan ' + mac)
    output = stream.read()
    print(output)

hostname = "192.168.210.11"

def ping(ip):
    import os
    hostname = "192.168.210.11"
    response = os.system("ping -c 4 " + hostname)
    if response == 0:
        print("Success")
    else:
        print("Not Success")

# if __name__ == "__main__":
#     execute_script(ip="192.168.210.12", username="user", password="user2020")


# client = connect(ip="192.168.210.12", username="user", password="user2020")
# exec(client, "ls")
# client_close(client)

# редактор кода через nano

# ctr+/ комментарий
# ping (hostname)
