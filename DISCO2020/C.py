import sys

# input to int
def f(s):
    if s == '.':
        return 0
    if s =='#':
        return 1
H, W, K = map(int, sys.stdin.readline())

lst = []
row_berries = []
for _ in range(H):
    row = list(map(f, sys.stdin.readline()))
    row_berries.append(sum(row))
    lst.append(row)

col_berries = []
for col in list(map(list, zip(*lst))):
    col_berries.append(sum(col))

mat = [[1] * H] * W
c = 1
for row in row_berries:
    mat.append([c] * W)
    if row > 0:
        c += 1