#!/usr/bin/env python3
import sys
import numpy as np

YES = "Yes"  # type: str
NO = "No"  # type: str

def is_bingo(row, B):
    count = 0 
    for b in B:
        if b in row:
            count += 1
    if count >= 3:
        return True
    else:
        False

def solve(A: "List[List[int]]", N: int, b: "List[int]"):
    A = np.asarray(A)
    isbingo = False

    for row in A:
        if is_bingo(row, b):
            isbingo = True

    for col in A.T:
        if is_bingo(col, b):
            isbingo = True

    for diag in [np.diag(A), np.diag(np.fliplr(A))]:
        if is_bingo(diag, b):
            isbingo = True

    if isbingo:
        print(YES)
    else:
        print(NO)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]  # type: "List[List[int]]"
    N = int(next(tokens))  # type: int
    b = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(A, N, b)

if __name__ == '__main__':
    main()
