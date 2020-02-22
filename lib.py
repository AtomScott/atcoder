def factors(n):
    gaps = [1,2,2,4,2,4,2,4,6,2,6]
    length, cycle = 11, 3
    f, fs, nxt = 2, [], 0
    while f * f <= n:
        while n % f == 0:
            fs.append(f)
            n /= f
        f += gaps[nxt]
        nxt += 1
        if nxt == length:
            nxt = cycle
    if n > 1: fs.append(n)
    return fs

import itertools

def powerset(L):
  pset = set()
  for n in range(len(L) + 1):
    for sset in itertools.combinations(L, n):
      pset.add(sset)
  return pset

def list_diff(first, second):
        second = set(second)
        return [item for item in first if item not in second]