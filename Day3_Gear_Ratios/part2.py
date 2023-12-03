import sys
import string
import re
import math

number = re.compile('[0-9]+')

gears = {}

def check(match, lines, line, column):
    minCol = max(column - 1, 0)
    maxCol = min(column + 2, len(lines[0]))
    minLine = max(line - 1, 0)
    maxLine = min(line + 2, len(lines))
    for l, line in enumerate(lines[minLine:maxLine]):
        for c, col in enumerate(line[minCol:maxCol]):
            if col == '*':
                key = f'({l + minLine}, {c + minCol})'
                if key in gears:
                    gears[key] = set([match]) | gears[key]
                else:
                    gears[key] = set([match])

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        raw = f.read()
        lines = raw.splitlines()
        for i, line in enumerate(lines):
            for n in number.finditer(line):
                span = n.span()
                if any([check(int(n.group()), lines, i, j) for j in range(*span)]):
                    acc += int(n.group())
        print(gears)
        acc = 0
        for k, v in gears.items():
            if len(v) == 2:
                acc += math.prod(v)
        sys.stdout.write(str(acc) + '\n')
