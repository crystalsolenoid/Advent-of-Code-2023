import sys

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        raw = f.read()
    lines = raw.splitlines()
    ans = 0
    for line in lines:
        sWin, sHave = [x.split() for x in line.split(':')[1].split('|')]
        win = set([int(x) for x in sWin])
        have = set([int(x) for x in sHave])
        hits = len(win & have)
        ans += 2 ** (hits - 1) if hits > 0 else 0
    sys.stdout.write(str(ans) + '\n')
