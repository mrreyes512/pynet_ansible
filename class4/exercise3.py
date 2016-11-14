#!/usr/bin/env python
"""
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2.
"""
import pexpect
import sys
from getpass import getpass

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = '22'
    password = '88newclass'
    # password = getpass()
    cisco_prompt = '#'

    ssh = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    # ssh.logfile = sys.stdout
    ssh.timeout = 7

    ssh.expect('ssword:')
    ssh.sendline(password)

    ssh.expect(cisco_prompt)
    ssh.sendline('show ip int brief')

    ssh.expect(cisco_prompt)
    print ssh.before
    # print ssh.after

if __name__ == "__main__":
    main()
