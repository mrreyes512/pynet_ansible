#!/usr/bin/env python
"""
Use PExpect to change the logging buffer size (logging buffered <size>) on
pynet-rtr2. Verify this change by examining the output of 'show run'.
"""
import pexpect
import sys
import re
from getpass import getpass

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    port = '22'
    password = '88newclass'
    # password = getpass()
    cisco_prompt = '#'
    buffersize = '20480'

    ssh = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    # ssh.logfile = sys.stdout
    ssh.timeout = 7

    ssh.expect('ssword:')
    ssh.sendline(password)

    ssh.expect(cisco_prompt)
    ssh.sendline('terminal length 0')

    ssh.expect(cisco_prompt)
    ssh.sendline('configure terminal')

    ssh.expect(cisco_prompt)
    ssh.sendline('logging buffered ' + str(buffersize))

    ssh.expect(cisco_prompt)
    ssh.sendline('do show run')

    try:
	pattern = re.compile(r'^log.*buffered.*$', re.MULTILINE)
	ssh.expect(pattern)
	# print ssh.before
	print ssh.after
    except pexpect.TIMEOUT:
	print "...took too long"

if __name__ == "__main__":
    main()

