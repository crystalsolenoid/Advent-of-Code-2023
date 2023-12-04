import sys
import string
import re
import math
import itertools

number = re.compile('[0-9]+')

class Grid():
    def __init__(self, raw):
        self.raw = raw
        self.rows = len(raw) // raw.count('\n')

        self.gears = {}

    def coord_from_pos(self, idx):
        return (idx // self.rows, idx % self.rows)

    def pos_from_coord(self, r, c):
        return r * self.rows + c

    def in_bounds(self, idx):
        return idx in range(0, len(self.raw))

    def get_neighbors(self, idx):
        r, c = self.coord_from_pos(idx)
        r_range = range(r-1, r+2)
        c_range = range(c-1, c+2)
        neighbors = []
        for r, c in itertools.product(r_range, c_range):
            pos = self.pos_from_coord(r, c)
            if self.in_bounds(pos):
                neighbors.append(pos)
        return [(i, self.raw[i]) for i in neighbors]

    def find_gears(self):
        for n in number.finditer(self.raw):
            self.find_neighbor_gears(n)

    def add_gear(self, n, g):
        key = g[0]
        value = int(n.group())
        if key in self.gears:
            self.gears[key] = set([value]) | self.gears[key]
        else:
            self.gears[key] = set([value])

    def find_neighbor_gears(self, n):
        for digit in range(*n.span()):
            for g in filter(lambda x: x[1] == '*', self.get_neighbors(digit)):
                self.add_gear(n, g)

    def count_gears(self):
        acc = 0
        for k, v in self.gears.items():
            if len(v) == 2:
                acc += math.prod(v)
        return acc

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        grid = Grid(f.read())
    grid.find_gears()
    ans = str(grid.count_gears())
    sys.stdout.write(ans + '\n')
