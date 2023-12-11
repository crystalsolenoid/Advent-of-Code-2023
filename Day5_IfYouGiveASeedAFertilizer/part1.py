import sys

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

    seeds = [int(x) for x in lines[0].split(':')[1].split()]

    maps = []
    for line in lines[2:]:
        if ':' in line:
            map_data = []
        elif line:
            map_data.append([int(x) for x in line.split()])
        else:
            maps.append(map_data)
    maps.append(map_data)

    locations = []
    for seed in seeds:
        locations.append(resolve_source(maps, seed))

    ans = min(locations)
    sys.stdout.write(str(ans) + '\n')
