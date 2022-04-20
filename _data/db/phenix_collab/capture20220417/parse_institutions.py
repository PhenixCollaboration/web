#!/usr/bin/python3

import yaml

insts_file      = open('instpipenow',  'r')
insts           = insts_file.readlines()
institutions    = []


for line in insts:
    institution = {}
    content = line.strip().split(' | ')
    institution[content[0]] = content[1]
    institutions.append(institution)

print(yaml.dump(institutions, sort_keys=False))
