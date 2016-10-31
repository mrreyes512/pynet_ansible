import telnetlib
import time
import socket
import sys
import getpass

TELNET_PORT = 23
TELNET_TIMEOUT = 6

class TelnetCisco(object):
    """
    Establish and maintain telnet connection to devices
    """

    def send_command(remote_conn, cmd):
	'''
	Send a command down the telnet channel; Return the response
	'''
	cmd = cmd.rstrip()
	remote_conn.write(cmd + '\n')
	time.sleep(1)
	return remote_conn.read_very_eager()

    def login(remote_conn, username, password):
	'''
	Login to network device
	'''
	output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
	remote_conn.write(username + '\n')
	output += remote_conn.read_until("ssword:", TELNET_TIMEOUT)
	remote_conn.write(password + '\n')
	return output

    def disable_paging(remote_conn, paging_cmd='terminal length 0'):
	'''
	Disable the paging of output (i.e. --More--)
	'''
	return send_command(remote_conn, paging_cmd)

    def telnet_connect(ip_addr):
	'''
	Establish telnet connection
	'''
	try:
	    return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
	except socket.timeout:
	    sys.exit("Connection timed-out")

