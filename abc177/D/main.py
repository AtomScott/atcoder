#!/usr/bin/env python3
import sys
import networkx as nx

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    G=nx.Graph()

    if M == 0 :
        print(1)
        return

    for a, b in zip(A,B):
        G.add_edge(a, b)

    Gc = max(nx.connected_components(G), key=len)
    print(len(Gc))
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
