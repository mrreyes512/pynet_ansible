#!/usr/bin/env python
"""
Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.
"""

from ciscoconfparse import CiscoConfParse as ccp


cisco_cfg = ccp("cisco.txt")

non_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map", childspec=r"AES")

print "search group: Non-AES match address\n"

for i in non_aes:
    print i.text


for i in non_aes[0].children:
    print i.text





