#!/usr/bin/env python
"""
5. Use Netmiko to enter into configuration mode on pynet-rtr2. Also use Netmiko to
verify your state (i.e. that you are currently in configuration mode).
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

print 'Connect to pynet1'
pynet_rtr1 = ConnectHandler(**pynet1)

print 'enter config mode'
pynet_rtr1.config_mode()

print 'am i in config mode?'
print pynet_rtr1.check_config_mode()
