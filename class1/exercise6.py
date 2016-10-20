#!/usr/bin/env python

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
