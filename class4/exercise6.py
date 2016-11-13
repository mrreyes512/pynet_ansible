#!/usr/bin/env python
"""
6. Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2,
and juniper-srx.
"""
from netmiko import ConnectHandler
from getpass import getpass

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
    }

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'port': 22,
    }

srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
    'secret': '',
    'port': 22,
    }

dev_list = [ 'pynet1', 'srx' ]

for device in (pynet1, pynet2):
    print device
    ssh = ConnectHandler('**device')
    # output = ssh.find_prompt()
    # print output
