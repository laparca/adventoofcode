#!/usr/bin/env python3
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from utils import *

set_release()

def index_or_default(l, value, default=None, start=0, end=9223372036854775807):
    try:
        return l.index(value, start, end)
    except ValueError:
        return default

def treat_stone(stone):
    if int(stone) == 0:
        return ['1']
    
    if len(stone) % 2 == 0:
        half_left  = stone[:len(stone)//2]
        half_right = stone[len(stone)//2:]
        return [str(int(half_left)), str(int(half_right))]
    
    return [str(int(stone) * 2024)]

def treat_stones(stones):
    new_stones = []
    for stone in stones:
        new_stones += treat_stone(stone)
    return new_stones

data = load_input_or_debug("125 17").split(" ")

debug(treat_stone("125"))
debug(treat_stones(data))

debug("starting...")
stones = data
for i in range(25):
    stones = treat_stones(stones)
    debug("{}. {}".format(i, stones))
print(len(stones))
