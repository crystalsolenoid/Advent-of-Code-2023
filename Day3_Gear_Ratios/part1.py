import sys
import string
import re

number = re.compile('[0-9]+')

def check(symbols, lines, line, column):
    minCol = max(column - 1, 0)
    maxCol = min(column + 2, len(lines[0]))
    minLine = max(line - 1, 0)
    maxLine = min(line + 2, len(lines))
    surround = ''.join([l[minCol:maxCol] for l in lines[minLine:maxLine]])
    return any(symbol in surround for symbol in symbols)

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        raw = f.read()
        symbols = set(raw) - set(string.digits + '.\n')
        lines = raw.splitlines()
        acc = 0
        for i, line in enumerate(lines):
            for n in number.finditer(line):
                span = n.span()
                if any([check(symbols, lines, i, j) for j in range(*span)]):
                    acc += int(n.group())
        sys.stdout.write(str(acc) + '\n')
