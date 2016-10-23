#!/usr/bin/env python
"""
Find all of the crypto map entries that are using PFS group2
"""

from ciscoconfparse import CiscoConfParse as ccp


cisco_cfg = ccp("cisco.txt")

group2 = cisco_cfg.find_objects_w_child(parentspec=r"^crypto map", childspec=r"set pfs group2")

print "search group: set pfs group2\n"

for i in group2:
    print i.text






