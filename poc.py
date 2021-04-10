#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import paramiko

def connect(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, port=22, username=username, password=password)
    return client

def exec(client, command):
    stdin_raw, stdout_raw, stderr_raw = client.exec_command(command)
    exit_code = stdout_raw.channel.recv_exit_status()
    stdout = []
    for line in stdout_raw:
        stdout.append(line.strip())
    stderr = []
    for line in stderr_raw:
        stderr.append(line.strip())
    print('\n'.join(stdout))
    del stdin_raw, stdout_raw, stderr_raw

# def read():
#     pc_dict = {}
#     with open('info', 'r') as file:
#         lines = file.readlines()
#
#     for line in lines:
#         if line:
#             pc_details = line.split()
#             pc_dict[pc_details[0]] = {'ip': pc_details[1], 'mac': pc_details[2]}
#     print(pc_dict)
#     return pc_dict

# pc_dict = read()
# pc_list = []

def read_script(ip, username, password):
    with open('script', 'r') as file:
        lines = file.readlines()

    client=connect(ip=ip, username=username, password=password)

    for line in lines:
        exec(client, line)
    client_close(client)
# выключение пк sudo shutdown now + парва админа, включение ls

    # stdout = []
    # for line in stdout_raw:
    #     stdout.append(line.strip())
    #
    # stderr = []
    # for line in stderr_raw:
    #     stderr.append(line.strip())
    #
    # print(stdout)

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


read_script(ip="192.168.210.12", username="user", password="user2020")
# read()
# exec(client, "ls")
# client_close(client)

# редактор кода через nano

# ctr+/ комментарий
# ping (hostname)
