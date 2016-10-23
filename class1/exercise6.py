#!/usr/bin/env python
"""
Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.
"""

import yaml
import json

candidates = [ 'cruz', 'sanders' ]
candidates.append({})
candidates[-1]['hilary_issue'] = 'emails'
candidates.append({})
candidates[-1]['trump_issue'] = 'tax_form'

with open ("exercise6.yml", "w") as file:
    file.write(yaml.dump(candidates, default_flow_style=False))

#yaml.load to read yaml files

with open ("exercise6.json", "w") as file:
    json.dump(candidates, file)
