import sys
import itertools

# Stealing from version 3.12, which I don't have installed
def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(itertools.islice(it, n)):
        yield batch

def resolve_map(map_data, source):
    for area in map_data:
        d_start, s_start, length = area
        if source in range(s_start, s_start + length + 1):
            return source - s_start + d_start
    return source

def resolve_source(maps, source):
    if len(maps) == 0:
        return source
    dest = resolve_map(maps[0], source)
    return resolve_source(maps[1:], dest)

if __name__ == "__main__":
    f = sys.argv[1]
    with open(sys.argv[1]) as f:
        raw = f.read()
    lines = raw.splitlines()

    raw_seeds = [int(x) for x in lines[0].split(':')[1].split()]
    init_seeds = raw_seeds[::2]
    length_seeds = raw_seeds[1::2]

    maps = []
    for line in lines[2:]:
        if ':' in line:
            map_data = []
        elif line:
            map_data.append([int(x) for x in line.split()])
        else:
            maps.append(map_data)
    maps.append(map_data)

    seeds = []
    for init, length in batched(raw_seeds, 2):
        for seed in range(init, init + length + 1):
            seeds.append(seed)

    locations = []
    for i, seed in enumerate(seeds):
        print(f"{i} out of {len(seeds)}")
        locations.append(resolve_source(maps, seed))

    ans = min(locations)
    sys.stdout.write(str(ans) + '\n')
