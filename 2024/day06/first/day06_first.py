#!/usr/bin/env python3

f = open("input.txt")
data = f.read().split("\n")
#data = [
#"....#.....",
#".........#",
#"..........",
#"..#.......",
#".......#..",
#"..........",
#".#..^.....",
#"........#.",
#"#.........",
#"......#..."
#]
guard_position = (0, 0)
guard_direction = (-1, 0)

def rotate90(direction):
    x, y = direction

    return (y, -x)

def get_guard_info(map):
    for line_num in range(len(map)):
        for column_num in range(len(map[line_num])):
            if map[line_num][column_num] == '^':
                return (line_num, column_num)


def move_guard(map, position, direction):
    new_position = (position[0] + direction[0], position[1] + direction[1])
    if is_in_map(map, new_position):
        if map[new_position[0]][new_position[1]] == '#':
            return move_guard(map, position, rotate90(direction))
    return (new_position, direction)

def is_in_map(map, position):
    return position[0] >= 0 and position[0] < len(map) and position[1] >= 0 and position[0] < len(map[0])
        
map = [[y for y in x] for x in data]
guard_position = get_guard_info(map)

while is_in_map(map, guard_position):
    (new_position, guard_direction) = move_guard(map, guard_position, guard_direction)
    map[guard_position[0]][guard_position[1]] = 'X'
    guard_position = new_position


print(sum([x.count('X') for x in map]))
