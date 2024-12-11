#!/usr/bin/env python3
TEST=False

def read_file(f : str) -> list[str]:
    with open(f) as file:
        return file.read().split("\n")

data = read_file("input.txt") if not TEST else [
    "............", #  0
    "........0...", #  1
    ".....0......", #  2
    ".......0....", #  3
    "....0.......", #  4
    "......A.....", #  5
    "............", #  6
    "............", #  7
    "........A...", #  8
    ".........A..", #  9
    "............", # 10
    "............"  # 11
]

class Coord:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def __add__(self, c):
        return Coord(self.x + c.x, self.y + c.y)
    
    def __sub__(self, c):
        return Coord(self.x - c.x, self.y - c.y)
    
    def __lt__(self, c):
        return self.x < c.x or (self.x == c.x and self.y < c.y)
    
    def __eq__(self, c):
        return self.x == c.x and self.y == c.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'Coord({self.x}, {self.y})'

    def value_from_map(self, map):
        return map[self.x][self.y]
    
    def is_in_map(self, map):
        return self.x >= 0 and self.y >= 0 and self.x < len(map) and self.y < len(map[0])
    
    def put_in_map(self, map):
        if self.value_from_map(map) == '.':
            map[self.x][self.y] = '#'
 
def calculate_antinodes(a : Coord, b : Coord) -> list[Coord]:
    d = b - a
    return [a - d, b + d]

def prepare_information(data):
    anthenas_by_frequency = {}
    for row_num in range(len(data)):
        for column_num in range(len(data[row_num])):
            v = data[row_num][column_num]
            if v == '.': continue
            if not v in anthenas_by_frequency:
                anthenas_by_frequency[v] = []
            anthenas_by_frequency[v].append(Coord(row_num, column_num))
    return anthenas_by_frequency

anthenas_by_frequency = prepare_information(data)

antinodes = []
for freq in anthenas_by_frequency:
    anthenas = anthenas_by_frequency[freq]
    for i in range(len(anthenas)-1):
        for j in range(i+1, len(anthenas)):
            antinodes += calculate_antinodes(anthenas[i], anthenas[j])


# Remove duplicated values
antinodes = list(set(antinodes))

# Take only the ones inside the map
antinodes = [x for x in antinodes if x.is_in_map(data)]

# Remove the ones that overlaps an anthena
#antinodes = [x for x in antinodes if x.value_from_map(data) == '.']

print([str(x) for x in sorted(antinodes)])
print(len([str(x) for x in antinodes]))

# Draw map
new_map = []
for i in range(len(data)):
    row = []
    for j in range(len(data[i])):
        row.append(data[i][j])
    new_map.append(row)

for antinode in antinodes:
    antinode.put_in_map(new_map)

for line in new_map:
    r = ""
    for c in line:
        r += c
    print(r)