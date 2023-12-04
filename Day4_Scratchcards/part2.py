import sys

ans = 0

def play(lines, i):
    global ans
    ans += 1
    card = lines[i]
    sWin, sHave = [x.split() for x in card.split(':')[1].split('|')]
    win = set([int(x) for x in sWin])
    have = set([int(x) for x in sHave])
    matches = len(win & have)
    end = min(i + matches + 1, len(lines))
    for j in range(i + 1, end):
        play(lines, j)

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        raw = f.read()
    lines = raw.splitlines()
    for i, _ in enumerate(lines):
        play(lines, i)
    sys.stdout.write(str(ans) + '\n')
