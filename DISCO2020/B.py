import sys

lines = sys.stdin.readlines()
N = int(lines[0])

stdin = list(map(int,lines[1].split(' ')))

lst = []
S1, S2 = 0, sum(stdin)
for i, a in enumerate(stdin):
    S1 += a
    S2 -= a
    lst.append(abs(S1-S2))

print(lst)
print(min(lst))