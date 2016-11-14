#!/usr/bin/env python
"""
7. Use Netmiko to change the logging buffer size
(logging buffered <size>) on pynet-rtr2.
"""
from netmiko import ConnectHandler
from devices import pynet2

def main():
    ssh = ConnectHandler(**pynet2)
    running = ssh.send_command("show running | inc logging")
    config_cmd = ['logging buffered 21999']

    print '-' * 80
    print pynet2['ip'] + ' - ' + pynet2['device_type'] +  ' - set logging'
    print running

    output = ssh.send_config_set(config_cmd)

    running = ssh.send_command("show running | inc logging")
    print running

if __name__ == "__main__":
    main()
