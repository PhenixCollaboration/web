#!/usr/bin/python3

import yaml


authors_file = open('authsmod.csv', 'r')
primary_file = open('primary.csv',  'r')
insts_file   = open('instpipenow',  'r')

# Create the institutions lookup table
institution = {}
insts = insts_file.readlines()

for line in insts:
    content = line.strip().split(' | ')
    institution[content[0]] = content[1]

# print(institution)

authors = authors_file.readlines()
primary = primary_file.readlines()

people = []

# For primary institution lookup, the key is LASTNAME,FIRSTNAME
primary_lookup = {}
for line in primary:
    elements = line.strip().split(',')
    primary_lookup[elements[0]+','+elements[1]] = elements[3]

for line in authors:
    person = {}
    elements = line.strip().split(',')
    name = elements[0]+','+elements[1]

    # Default is just the last element (works for single institution)
    inst = elements[3]

    # Now detect multiple institions and select only one
    # pased on the "primary" info
    if len(elements)>4:
        try:
            inst = primary_lookup[elements[0]+','+elements[1]]
        except:
            print('Primary Institution lookup ERROR')
            exit(-1)

    full_institution = ''
    try:
        full_institution = institution[inst]
    except:
        print('Full Institution Name lookup ERROR')
        exit(-2)

    person['name']      = name
    person['email']     = elements[2]
    person['inst']      = full_institution

    people.append(person)

print(yaml.dump(people, sort_keys=False))
