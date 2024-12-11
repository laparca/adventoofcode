#!/usr/bin/python3
import re

def mul(list):
    m = 1
    for i in list:
        m *= i
    return m

with open('input.txt') as input:
    matcher = re.compile(r'(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(don\'t\(\))')
    only_numbers = re.compile(r'[0-9]+')
    values = matcher.findall(input.read())
    enabled = True
    filtered_values = []
    for v in values:
        if len(v[1]) > 0:
            print("enabled")
            enabled = True
        elif len(v[2]) > 0:
            print("disabled")
            enabled = False
        elif enabled:
            print(v[0])
            filtered_values.append(v[0])
    print(filtered_values)
    values = sum([mul([int(y) for y in only_numbers.findall(x)]) for x in filtered_values])
    print(values)