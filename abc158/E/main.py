#!/usr/bin/env python3
import sys

def countSubStr(str, n, k): 
    numMultiples = 0
    seenRemainders = [set() for i in range(n)]# array of n sets, all initially empty
    for i in range(0, n+1):
        remainder = 0
        prefixesFound = 0
        for j in range(i, n):
            remainder = (10 * remainder + int(str[j])) % k
            if remainder in seenRemainders[j]:
                break

            seenRemainders[j].add(remainder)

            if remainder == 0:
                prefixesFound += 1
        numMultiples += prefixesFound * (prefixesFound + 1) / 2
    return int(numMultiples)


def solve(N: int, P: int, S: int):
    S = [c for c in str(S)]
    ans = countSubStr(S, len(S), P)
    print(ans)


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(N, P, S)

if __name__ == '__main__':
    main()
