#!/usr/bin/env python3
import numpy as np
from collections import deque, namedtuple
from itertools import product

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

def make_edge(start, end, cost=1):
    return Edge(start, end, cost)

class Graph:
    def __init__(self, edges):

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(sum(
            ([edge.start, edge.end] for edge in self.edges), []
        ))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}

        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))
            neighbours[edge.end].add((edge.start, edge.cost))
        return neighbours

            
    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs =[[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.starts, edge,end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'

        # 1. Mark all nodes unvisited and store them.
        # 2. Set the distance to zero for our initial node 
        # and to infinity for other nodes.
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            # 3. Select the unvisited node with the smallest distance, 
            # it's current node now.
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])

            # 6. Stop, if the smallest distance 
            # among the unvisited nodes is infinity.
            if distances[current_vertex] == inf:
                break

            # 4. Find unvisited neighbors for the current node 
            # and calculate their distances through the current node.
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost

                # Compare the newly calculated distance to the assigned 
                # and save the smaller one.
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

            # 5. Mark the current node as visited 
            # and remove it from the unvisited set.
            vertices.remove(current_vertex)


        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path

def solve(N, M, C):
    graph = Graph([])

    C = np.asarray(C)
    start_x, start_y = np.where(C=='s')
    goal_x, goal_y = np.where(C=='g')

    np.indices(C.shape)
    row_idxs, col_idxs = np.indices(C.shape)
    for i, j in zip(row_idxs.flatten(), col_idxs.flatten()):
        for inc_i, inc_j in product([-1, 1], [-1, 1]):
            if 0 <= i - inc_i < C.shape[0] and  0 <= j - inc_j < C.shape[1]:
                graph.add_edge((i, j), (i - inc_i, j - inc_j))

    dist = graph.dijkstra((int(start_x), int(start_y)), (int(goal_x), int(goal_y)))
    print(dist)


# Generated by 1.1.6 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, M = list(map(int, input().split()))
    C = []
    for i in range(N):
        row = input()
        C.append([r for r in row])
    
    solve(N, M, C)
    pass

if __name__ == '__main__':
    main()