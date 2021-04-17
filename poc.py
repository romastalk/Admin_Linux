#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import paramiko

def connect(ip, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=ip, port=22, username=username, password=password)
    return client

def exec(client, command):
    print(f'>>>>> Выполняем [{command.strip()}] <<<<<')
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

def execute_script(ip, username, password):
    with open('script', 'r') as file:
        lines = file.readlines()


    client = connect(ip=ip, username=username, password=password)

    for line in lines:
        exec(client, line)
    client_close(client)
    input("Press 'Enter' to continue...")

def client_close(client):
    client.close()
    del client
