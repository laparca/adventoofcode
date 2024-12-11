#!/usr/bin/python3
import re

def mul(list):
    m = 1
    for i in list:
        m *= i
    return m

with open('input.txt') as input:
    matcher = re.compile(r'mul\([0-9]{1,3},[0-9]{1,3}\)')
    only_numbers = re.compile(r'[0-9]+')
    values = matcher.findall(input.read())

    values = sum([mul([int(y) for y in only_numbers.findall(x)]) for x in values])
    print(values)