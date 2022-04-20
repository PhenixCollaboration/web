#!/usr/bin/python3

import yaml


authors_file = open('authsmod.csv', 'r')
primary_file = open('primary.csv',  'r')

authors = authors_file.readlines()
primary = primary_file.readlines()

people = []

primary_lookup = {}

for line in primary:
    elements = line.strip().split(',')
    primary_lookup[elements[0]+','+elements[1]] = elements[3]

for line in authors:
    person = {}
    name = elements[0]+','+elements[1]

    elements = line.strip().split(',')
    output_line = elements[:4]

    inst = elements[3]

    if len(elements)>4:
        try:
            inst = primary_lookup[elements[0]+','+elements[1]]
        except:
            print('Primary Institution lookup ERROR')

    person['name']      = name
    person['email']     = elements[2]
    person['inst']      = inst

    # output_line[3] = inst

    people.append(person)

    #print(','.join(output_line))

print(yaml.dump(people, sort_keys=False))
# print(people)