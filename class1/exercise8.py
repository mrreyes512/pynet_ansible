#!/usr/bin/env python
"""
Write a Python program using ciscoconfparse that parses this config file. Note, this config file is not fully valid (i.e. parts of the configuration are missing). The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.
"""

from ciscoconfparse import CiscoConfParse as ccp


cisco_cfg = ccp("cisco.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map")

print "cisco.txt: crypto map\n"

for i in crypto_map:
    print i.text






