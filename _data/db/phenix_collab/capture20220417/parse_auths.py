#!/usr/bin/python3

import sys

lines = sys.stdin.readlines()

for line in lines:
    content = line.strip()
    elements = content.split(',')
    print((',').join(elements[3:]))
