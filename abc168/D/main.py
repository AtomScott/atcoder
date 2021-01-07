#!/usr/bin/env python3
import sys
from collections import deque

YES = "Yes"  # type: str


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    dq = deque([])
    traversed = [False for _ in range(N+1)]
    ans = [None for _ in range(N+1)]

    G = {n : set([]) for n in range(1, N+1)}
    for a, b in zip(A,B):
        G[a].add(b)
        G[b].add(a)

    dq.append(1)
    traversed[1] = True

    while dq:
        s = dq.popleft()

        for node in G[s]:
            if not traversed[node]:
                dq.append(node)
                traversed[node] = True
                ans[node] = s

    print(YES)
    for s in ans:
        if s != None:
            print(s)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
