#!/usr/bin/env python3
import sys
import math

def solve(A: int, B: int):
    open = 1
    count = 0
    while(open<B):
        open -= 1
        open += A 
        count += 1
    print(count)
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()