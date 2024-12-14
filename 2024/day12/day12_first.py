#!/usr/bin/env python3
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from utils import *

set_release()
A = "AAAA\nBBCD\nBBCC\nEEEC"
B = "OOOOO\nOXOXO\nOOOOO\nOXOXO\nOOOOO"
data = load_input_or_debug(B).split("\n")

def perimeter_for_point(map, coord: Coord):
    v = coord.value_from_map(map)
    destinations = [x+coord for x in SIMPLE_DIRECTIONS]
    return [x.is_in_map(map) and x.value_from_map(map) == v for x in destinations].count(False)

debug(perimeter_for_point(data, Coord(0,0)))
debug(perimeter_for_point(data, Coord(1,1)))

parsed_map = [[False for i in x] for x in data]

def parse_plant(map, parsed_map, plant, position):
    if position.value_from_map(parsed_map): return (0, 0)
    print("parsing plan {} at {}".format(plant, position))
    area = 1
    perimeter = perimeter_for_point(map, position)
    position.set_value_in_map(parsed_map, True)
    is_valid_destination = lambda x: x.is_in_map(map) and x.value_from_map(map) == plant and not x.value_from_map(parsed_map)
    for i in [x for x in simple_moves(position) if is_valid_destination(x)]:
        na, np = parse_plant(map, parsed_map, plant, i)
        area += na
        perimeter += np

    return (area, perimeter)

debug(parsed_map)

prize = 0
for c in coord_generator(len(data), len(data[0])):
    if c.value_from_map(parsed_map): continue

    plant = c.value_from_map(data)

    area, perimeter = parse_plant(data, parsed_map, plant, c)
    prize += area*perimeter
    debug("plant {} has area {} and perimeter {}; prize is {}".format(plant, area, perimeter, area*perimeter))

print("Total prize is", prize)