#!/usr/bin/env python3
import sys
from collections import Counter


def solve(N: int, S: "List[str]"):
    cnt = Counter()
    for s in S:
        cnt[s] += 1
    
    lst = []
    mx = max(cnt.values())
    for key, val in cnt.items():
        if val == mx:
            lst += [key]

    for word in sorted(lst):
        print(word)
    
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
