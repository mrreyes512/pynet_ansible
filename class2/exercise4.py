#!/usr/bin/env python
"""
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and prints out both the MIB2 sysName and sysDescr.
"""
from snmp_helper import snmp_extract
from snmp_helper import snmp_get_oid

DEVICES = ['184.105.247.70','184.105.247.71']

OIDS = ['.1.3.6.1.2.1.1.1.0','.1.3.6.1.2.1.1.5.0']

COMMUNITY = 'galileo'

# Read loop for all devices
for DEVICE in DEVICES:
    print "Host: ", DEVICE
    print "---"

    # Read loop for all OIDS
    for OID in OIDS:
        print "SNMP OID: ", OID
        print snmp_extract(snmp_get_oid((DEVICE, COMMUNITY, 161), OID))
        print
    print "========================="

