#!/usr/bin/env python
"""
Write a script that connects using telnet to the pynet-rtr1 router. Execute the 'show ip int brief' command on the router and return the output.

Try to do this on your own (i.e. do not copy what I did previously). You should be able to do this by using the following items:

telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
remote_conn.read_until(<string_pattern>, TELNET_TIMEOUT)
remote_conn.read_very_eager()
remote_conn.write(<command> + '\n')
remote_conn.close()
"""

import telnetlib
import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_command(remote_conn, cmd):
    cmd = cmd.rstrip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()

def login(remote_conn, username, password):
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("assword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    return output

def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
	sys.exit("Connection timed-out")

def main():
    ip_addr = '184.105.247.70'
    #ip_addr = '8.8.8.8'
    username = 'pyclass'
    password = '88newclass'


    remote_conn = telnet_connect(ip_addr)
    output = login(remote_conn, username, password)
    #print output

    time.sleep(1)
    output = remote_conn.read_very_eager()
    #print output

    output = send_command(remote_conn, 'terminal length 0')
    output = send_command(remote_conn, 'show ip interface brief')
    print output

    remote_conn.close()

if __name__ == "__main__":
    main()

