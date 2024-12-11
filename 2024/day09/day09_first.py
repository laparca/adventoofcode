#!/usr/bin/env python3
TEST=False

def read_file(f : str) -> str:
    with open(f) as file:
        return file.read()

data = read_file("input.txt") if not TEST else "2333133121414131402"

def swap_in_list(l, p0, p1):
    a = l[p0]
    l[p0] = l[p1]
    l[p1] = a

def checksum(l):
    sum = 0
    for i in range(len(l)):
        if l[i] != '.':
            sum += i * l[i]
    return sum

disk_map = []
file_id = 0
for i in range(len(data)):
    if i % 2 == 0:
        for j in range(int(data[i])):
            disk_map.append(file_id)
        file_id += 1
    else:
        for j in range(int(data[i])):
            disk_map.append('.')

if TEST:
    print(disk_map)

left = disk_map.index('.')
right = len(disk_map) - 1
while left < right:
    if disk_map[right] != '.':
        swap_in_list(disk_map, left, right)
        left = disk_map.index('.', left)
    else:
        right -= 1

if TEST:
    print(disk_map)
print(checksum(disk_map))