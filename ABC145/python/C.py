import sys
import itertools
import numpy as np

lines = sys.stdin.readlines()

N = int(lines[0].rstrip())
perms = list(itertools.permutations(range(N)))
combs = list(itertools.combinations(range(N), 2))

arr_2d = np.zeros((N,2))
if N <= 2:
	arr_dist_memo = np.zeros((len(combs)+1,len(combs)+1))
else:
	arr_dist_memo = np.zeros((len(combs),len(combs)))

arr_dist_ave = np.zeros(len(perms))

for i, line in enumerate(lines[1:]):
    x, y = map(int,line.split(' '))
    arr_2d[i, 0] = x
    arr_2d[i, 1] = y

for i,j in combs:
    arr_dist_memo[i, j] = np.linalg.norm(arr_2d[i] - arr_2d[j])

for index, l in enumerate(perms):
    for i, j  in zip(range(N-1), range(1, N)):
        arr_dist_ave[index] += arr_dist_memo[l[i],l[j]]

print(np.mean(arr_dist_ave)*2)