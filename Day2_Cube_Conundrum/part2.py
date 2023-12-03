import sys
import re

redEx = re.compile('[0-9]+(?= red)')
greenEx = re.compile('[0-9]+(?= green)')
blueEx = re.compile('[0-9]+(?= blue)')

def get_power(line):
    red = max([int(x) for x in redEx.findall(line)])
    green = max([int(x) for x in greenEx.findall(line)])
    blue = max([int(x) for x in blueEx.findall(line)])
    return str(red * green * blue)

if __name__ == "__main__":
    for line in sys.stdin:
        power = get_power(line) + '\n'
        sys.stdout.write(power)
