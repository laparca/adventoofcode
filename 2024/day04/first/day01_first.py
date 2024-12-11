#!/usr/bin/env python3
import re
input_file = open("input.txt", "r")
data = input_file.readlines()

#data = [
#"MMMSXXMASM",
#"MSAMXMSMSA", 
#"AMXSXMAAMM", 
#"MSAMASMSMX", 
#"XMASAMXAMM", 
#"XXAMMXXAMA", 
#"SMSMSASXSS", 
#"SAXAMASAAA", 
#"MAMMMXMMMM", 
#"MXMXAXMASX"]
def check_value_from(list, position, desired):
    return list[position[0]][position[1]] == desired

def check_str_direction(str, list, position, direction):
    for c in str:
        if position[0] < 0 or position[1] < 0 or position[0] >= len(list) or position[1] >= len(list[0]):
            #print(position, direction)
            return False
        if not check_value_from(list, position, c):
            return False
        position = (position[0] + direction[0], position[1] + direction[1])
    return True

def count_xmas(list):
    directions = [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]
    counter = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if list[i][j] == 'X':
                for dir in directions:
                    if check_str_direction("XMAS", list, (i, j),  dir):
                        print("XMAS found in " + str(i) + ", " + str(j) + " with direction " + str(dir))
                        counter += 1
    return counter

#print(data)

print(count_xmas(data))

