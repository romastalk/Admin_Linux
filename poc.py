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
