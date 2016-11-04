#!/usr/bin/env python
"""
Using SNMPv3 create a script that detects router configuration changes.

If the running configuration has changed, then send an email notification to
yourself identifying the router that changed and the time that it changed.

Note, the running configuration of pynet-rtr2 is changing every 15 minutes
(roughly at 0, 15, 30, and 45 minutes after the hour).  This will allow you
to test your script in the lab environment.
"""

import pysnmp
import snmp_helper
import email_helper
import datetime

