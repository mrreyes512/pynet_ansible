#!/usr/bin/env python
"""
Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2.
"""
import paramiko
from getpass import getpass

ip_addr = '184.105.247.71'
port = 22
username = 'pyclass'
#password = getpass()
password = '88newclass'

remote_conn_pre=paramiko.SSHClient()
#remote_conn_pre.load_system_host_keys()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

stdin, stdout, stderr = remote_conn_pre.exec_command('show version\n')
#print stdout.readlines()
for line in stdout.readlines():
    print line.strip()

#remote_conn = remote_conn_pre.invoke_shell()
#remote_conn.send("show ip int brief\n")
#outp = remote_conn.recv(5000)
#print outp


