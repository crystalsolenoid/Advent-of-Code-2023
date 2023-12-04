import sys

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        raw = f.read()
    lines = raw.splitlines()
    ans = 0
    for line in lines:
        win, have = [set(x.split()) for x in line.split(':')[1].split('|')]
        hits = len(win & have)
        ans += 2 ** (hits - 1) if hits > 0 else 0
    sys.stdout.write(str(ans) + '\n')
