#!/usr/bin/python3

authors_file = open('authsmod.csv', 'r')
primary_file = open('primary.csv',  'r')

authors = authors_file.readlines()
primary = primary_file.readlines()

primary_lookup = {}
for line in primary:
    content = line.strip()
    elements = content.split(',')
    primary_lookup[elements[0]+','+elements[1]] = elements[3]

for line in authors:
    content = line.strip()
    elements = content.split(',')
    output_line = elements[:4]

    if len(elements)>4:
        try:
            output_line[3] = primary_lookup[elements[0]+','+elements[1]]
        except:
            print('Primary Institution lookup ERROR')

    print(','.join(output_line))