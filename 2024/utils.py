DEBUG=True

def load_input_or_debug(debug_value):
    if DEBUG:
        return debug_value
    with open("input.txt") as f:
        return f.read()

def set_release():
    global DEBUG
    DEBUG=False

def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


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
    
    def __repr__(self):
        return f'Coord({self.x}, {self.y})'

    def value_from_map(self, map):
        return map[self.x][self.y]
    
    def is_in_map(self, map):
        return self.x >= 0 and self.y >= 0 and self.x < len(map) and self.y < len(map[0])
    
    def put_in_map(self, map):
        if self.value_from_map(map) == '.':
            map[self.x][self.y] = '#'

D_UP    = Coord(-1,  0)
D_RIGHT = Coord( 0,  1)
D_DOWN  = Coord( 1,  0)
D_LEFT  = Coord( 0, -1)

D_UP_RIGHT   = Coord(-1,  1)
D_UP_LEFT    = Coord(-1, -1)
D_DOWN_RIGHT = Coord( 1,  1)
D_DOWN_LEFT  = Coord( 1, -1)

SIMPLE_DIRECTIONS = [ D_UP, D_RIGHT, D_DOWN, D_LEFT]
ALL_DIRECTIONS = [ D_UP, D_UP_RIGHT, D_RIGHT, D_DOWN_RIGHT, D_DOWN, D_DOWN_LEFT, D_LEFT, D_UP_LEFT]