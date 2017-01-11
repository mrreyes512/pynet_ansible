#!/usr/bin/env python
"""
Using Arista's pyeapi, create a script that allows you to add a VLAN (both the
VLAN ID and the VLAN name).  Your script should first check that the VLAN ID is
available and only add the VLAN if it doesn't already exist.  Use VLAN IDs
between 100 and 999.  You should be able to call the script from the command
line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100

Once again only remove the VLAN if it exists on the switch.  You will probably
want to use Python's argparse to accomplish the argument processing.
"""

import pyeapi
import argparse
from pprint import pprint

def vlan_CHECK(vlan_id, connect):
    print "check for VLAN : " + str(vlan_id)

    try:
        # raw_output = connect.enable("show vlans")
        cmd = 'show vlan ' + str(vlan_id)
        raw_output = connect.enable(cmd)
        response = raw_output[0]['result']['vlans']

        pprint(response)
        return response[vlan_id]['name']

    except (pyeapi.eapilib.CommandError, KeyError):
        return False

    return True


def vlan_REMOVE(vlan_id, connect):
    cmd = ['no vlan ' + str(vlan_id)]
    if connect.config(cmd):
        print "Removing VLAN : " + str(vlan_id)

def vlan_ADD(vlan_id, vlan_name, connect):
    cmd = ['vlan ' + str(vlan_id), 'name ' + vlan_name]
    if connect.config(cmd):
        print "Adding VLAN : " + str(vlan_id)

def main():

    # connect back to my switch
    connect = pyeapi.connect_to("pynet-sw4")

    # argparse stuff
    parser = argparse.ArgumentParser("Adding and Removing of a VLAN to Arista swiches uing pyeapi")
    parser.add_argument("vlan_id", help="VLAN number to create or remove", action="store", type=int)
    parser.add_argument("--name", help="Specify VLAN name", action="store", dest="vlan_name", type=str)
    parser.add_argument("--remove", help="Remove the given VLAN ID", action="store_true", dest="remove_vlan")

    args = parser.parse_args()

    # pprint(vlan_CHECK(args.vlan_id))
    # vlan_CHECK(connect, args.vlan_id)

    if args.remove_vlan:
        vlan_REMOVE(args.vlan_id, connect)
    else:
        if vlan_CHECK(args.vlan_id, connect):
            vlan_ADD(args.vlan_id, args.vlan_name, connect)
        else:
            print "VLAN Already Present, no action"

    # if vlan_CHECK(args.vlan_id, connect):
	# print "VLAN exists, removing it"
	# command_str = 'no vlan {}'.format(vlan_id)
	# eapi_conn.config([command_str])
    # else:
	# print "VLAN does not exist, no action required"


if __name__ == '__main__':
    main()
