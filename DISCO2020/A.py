import sys

line = sys.stdin.readlines()[0]
X, Y = map(int,line.split(' '))

ret = 0

if X == Y == 1:
    ret += 400000

for p in [X,Y]:
    if p == 1:
        ret += 300000
    if p == 2:
        ret += 200000
    if p == 3:
        ret += 100000

print(ret)