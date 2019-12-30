import sys

for line in sys.stdin:
    r = int(line.rstrip())
    print(r*r)