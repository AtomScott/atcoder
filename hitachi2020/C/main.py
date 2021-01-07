#!/usr/bin/env python3
import sys

class Node():
    def __init__(self, data):
        self.neighbours = []
        self.data = data

    def add_neighbour(self, node):
        self.neighbours += [node]

    def get_neighbours(self, K):
        # base case 
        if K == 0:
            return [self.data]

        else:
            nodes = []
            for neighbour in self.neighbours:
                nodes += [n for n in neighbour.get_neighbours(K-1) if n != self.data]
                return nodes
        


def solve(N: int, A: "List[int]", B: "List[int]"):

    nodes = [Node(i) for i in range(N)]
    edges = [[a-1,b-1] for a,b in zip(A,B)]

    for a,b in edges:
        nodes[a].add_neighbour(nodes[b])
        nodes[b].add_neighbour(nodes[a])

    pairs = []
    for node in nodes:
        pairs += [(node.data+1, n+1) for n in node.get_neighbours(K=3)]
    return


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int()] * (N - 1)  # type: "List[int]"
    b = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, a, b)

if __name__ == '__main__':
    main()