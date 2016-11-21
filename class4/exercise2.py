#!/usr/bin/env python
"""
Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2.
This will require that you enter into configuration mode.
"""
import paramiko
import time
from getpass import getpass

ip_addr = '184.105.247.71'
port = 22
username = 'pyclass'
#password = getpass()
password = '88newclass'
buffersize = '20480'

def main():
    remote_conn_pre=paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip_addr, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
    remote_conn = remote_conn_pre.invoke_shell()

    remote_conn.send("terminal length 0\n")
    remote_conn.send("configure terminal\n")
    remote_conn.send("logging buffered " + str(buffersize) + "\n")
    remote_conn.send("end\n")
    remote_conn.send("copy run start\n\n")

    time.sleep(1)
    outp = remote_conn.recv(5000)
    print outp

if __name__ == "__main__":
    main()
