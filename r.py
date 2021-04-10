#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import paramiko

host = "192.168.210.8"
port = 22
transport = paramiko.Transport((host, port))
transport.connect(username='user', password='user2020')
sftp = paramiko.SFTPClient.from_transport(transport)

remotepath = '/home/user/Рабочий стол/khar/2.c'
localpath = '/home/user/Рабочий стол/Students/2.c'

sftp.get(remotepath, localpath)
sftp.put(localpath, remotepath)

sftp.close()
transport.close()
