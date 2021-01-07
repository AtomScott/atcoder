#!/usr/bin/env python3
import sys
import numpy as np

YES = "Yes"  # type: str
NO = "No"  # type: str

from itertools import combinations

def solve(A: int, B: int, C: int, D: int):
    l = [list(combinations(list(range(4)), i)) for i in range(1,5)]
    l = [a for b in l for a in b]

    arr = np.array([A,B,C,D])

    for comb in l:
        idxs_eat = list(comb)
        idxs_abs = [i for i in range(4) if i not in comb]

        if arr[idxs_eat].sum() == arr[idxs_abs].sum():
            print(YES)
            return

    print(NO)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(A, B, C, D)

if __name__ == '__main__':
    main()
