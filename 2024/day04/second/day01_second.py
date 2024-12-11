#!/usr/bin/env python3
#import re
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
# M M   M S   S S   S M
#  A     A     A     A
# S S   M S   M M   S M
def count_xmas(list):
    counter = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[i])-1):
            if list[i][j] == 'A':
                if (list[i-1][j-1] == 'M' and list[i-1][j+1] == 'M' and list[i+1][j+1] == 'S' and list[i+1][j-1] == 'S') or \
                   (list[i-1][j-1] == 'M' and list[i-1][j+1] == 'S' and list[i+1][j+1] == 'S' and list[i+1][j-1] == 'M') or \
                   (list[i-1][j-1] == 'S' and list[i-1][j+1] == 'S' and list[i+1][j+1] == 'M' and list[i+1][j-1] == 'M') or \
                   (list[i-1][j-1] == 'S' and list[i-1][j+1] == 'M' and list[i+1][j+1] == 'M' and list[i+1][j-1] == 'S'):
                   print((i, j))
                   counter += 1
    return counter

#print(data)

print(count_xmas(data))

