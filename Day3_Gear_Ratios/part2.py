import sys
import string
import re
import math
import itertools

number = re.compile('[0-9]+')

gears = {}

def get_neighbors(raw, idx):
    r, c = coord_from_pos(raw, idx)
    r_range = range(r-1, r+2)
    c_range = range(c-1, c+2)
    neighbors = []
    for r, c in itertools.product(r_range, c_range):
        pos = pos_from_coord(raw, r, c)
        if pos in range(0, len(raw)):
            neighbors.append(pos)
    return [(i, raw[i]) for i in neighbors]

def coord_from_pos(raw, idx):
    rows = len(raw) // raw.count('\n')
    return (idx // rows, idx % rows)

def pos_from_coord(raw, r, c):
    rows = len(raw) // raw.count('\n')
    return r * rows + c

def find_gears(raw):
    for n in number.finditer(raw):
        find_neighbor_gears(raw, n)

def find_neighbor_gears(raw, n):
    for digit in range(*n.span()):
        for g in filter(lambda x: x[1] == '*', get_neighbors(raw, digit)):
            if g[0] in gears:
                gears[g[0]] = set([int(n.group())]) | gears[g[0]]
            else:
                gears[g[0]] = set([int(n.group())])

def count_gears():
    acc = 0
    for k, v in gears.items():
        if len(v) == 2:
            acc += math.prod(v)
    return acc

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        raw = f.read()
        find_gears(raw)
        ans = str(count_gears())
        sys.stdout.write(ans + '\n')
