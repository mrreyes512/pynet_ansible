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

for device in (pynet1, pynet2, srx):
    ssh = ConnectHandler(**device)
    arp_table = ssh.send_command("show arp")
    print '-' * 80
    print device['ip'] + ' - ' + device['device_type'] +  ' - arp table output'
    print arp_table
