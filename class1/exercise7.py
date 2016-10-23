#!/usr/bin/env python
"""
Write a Python program that reads both the YAML file and the JSON file created in exercise6 and pretty prints the data structure that is returned
"""

import yaml
import json
from pprint import pprint


print "YAML Output: \n"

with open("exercise6.yml") as file:
    yaml_output = yaml.load(file)
    pprint(yaml_output)

print "\n\n---------\n\n"

print "JSON Output:\n"

with open("exercise6.json") as file:
    json_output = json.load(file)
    pprint(json_output)
