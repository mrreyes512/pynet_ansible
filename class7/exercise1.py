#!/usr/bin/env python
"""
Use Arista's eAPI to obtain 'show interfaces' from the switch. Parse the 'show
interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of
the interfaces on the switch.  Accomplish this using Arista's pyeapi.
"""

import pyeapi


def main():

    connect = pyeapi.connect_to("pynet-sw4")

    raw_output = connect.enable("show interfaces")
    interfaces = raw_output[0]['result']['interfaces']

    for interface in interfaces:
        if 'interfaceCounters' in interfaces[interface]:
            print "  Interface: " + str(interfaces[interface]['name'])
            print "  In Octets: " + str(interfaces[interface]['interfaceCounters']['inOctets'])
            print " Out Octets: " + str(interfaces[interface]['interfaceCounters']['outOctets'])
            print ""

if __name__ == '__main__':
    main()
