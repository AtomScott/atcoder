#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(A: int, B: int, C: int, D: int):
    f = lambda x, y, a: x <= a <= y
    if f(A,B,C) or f(A,B,D):
        print('Yes')
    else:
        if f(C,D,A) or f(C,D,B):
            print('Yes')
            return 
        print('No')
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
