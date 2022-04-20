#!/usr/bin/python3

authors = open('authsmod.csv','r')

lines = authors.readlines()

for line in lines:
    content = line.strip()
    elements = content.split(',')
    print((',').join(elements[3:]))
