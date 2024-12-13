#!/usr/bin/env python3
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from utils import *

set_release()

data = load_input_or_debug("89010123\n"
"78121874\n"
"87430965\n"
"96549874\n"
"45678903\n"
"32019012\n"
"01329801\n"
"10456732").split("\n")

def get_start_points(map):
    start_points = []
    # Find the start points
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '0':
                start_points.append(Coord(i, j))
    return start_points

def paths(map, start_point):
    if start_point.value_from_map(map) == '9':
        return [start_point]

    destinations = []
    for d in SIMPLE_DIRECTIONS:
        position_to_check = start_point + d
        if position_to_check.is_in_map(map) and int(start_point.value_from_map(map)) + 1 == int(position_to_check.value_from_map(map)):
            destinations += paths(map, position_to_check)
    return list(set(destinations))

debug(data)

start_points = get_start_points(data)
debug(start_points)

total = 0
for start_point in start_points:
    p = paths(data, start_point)
    debug(p)
    total += len(p)
print(total)