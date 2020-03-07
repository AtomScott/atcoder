#!/usr/bin/env python3
import sys
import math

def check1(k):
    return math.floor(k*0.08) == math.floor(k*0.1)

def check2(k, A , B):
    return math.floor(k*0.08) == A and math.floor(k*0.1) == B

def solve(A: int, B: int):
    k1 = A / .08
    k2 = B / .1

    min_k = math.floor(min(k1 - k1*0.08, k2 - k2 * 0.1))
    max_k = math.floor(max(k1 + k1*0.08, k2 + k2 * 0.1))

    # min_k = math.floor(min(k1 - k1*0.08, k2 - k2 * 0.1))
    # max_k = math.floor(max(k1 + k1*0.08, k2 + k2 * 0.1))

    ans = -1
    for k in range(min_k, max_k+1):
        c1 = check1(k)
        c2 = check2(k, A, B)
        if c2:
            ans = k
            break

    print(ans)
    
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
