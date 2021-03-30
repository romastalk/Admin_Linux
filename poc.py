#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import paramiko


def ssh_ls_example():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='192.168.210.11', port=22, username='user', password='user2020')
    stdin_raw, stdout_raw, stderr_raw = client.exec_command('ls')
    exit_code = stdout_raw.channel.recv_exit_status()

# выключение пк sudo shutdown now + парва админа, включение ls

    stdout = []
    for line in stdout_raw:
        stdout.append(line.strip())

    stderr = []
    for line in stderr_raw:
        stderr.append(line.strip())

    print(stdout)

    client.close()
    del client, stdin_raw, stdout_raw, stderr_raw

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


wake_on_lan(example_mac)
# ctr+/ комментарий
ping (hostname)
