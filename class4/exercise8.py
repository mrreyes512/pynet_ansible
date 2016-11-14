#!/usr/bin/env python
"""
8. Use Netmiko to change the logging buffer size (logging buffered <size>) and to disable
console logging (no logging console) from a file on both pynet-rtr1 and pynet-rtr2
(see 'Errata and Other Info, item #4).
"""
from netmiko import ConnectHandler
from devices import pynet1, pynet2

def main():

    for device in (pynet1, pynet2):
	ssh = ConnectHandler(**device)
	arp_table = ssh.send_config_from_file(config_file='config.txt')
	running = ssh.send_command("show running | inc logging")

	print '-' * 80
	print device['ip'] + ' - ' + device['device_type'] +  ' - set logging'
	print running

if __name__ == "__main__":
    main()
