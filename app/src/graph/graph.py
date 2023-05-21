import networkx as nx
from typing import List


class Graph:
    graph: nx.DiGraph

    def __init__(self):
        self.graph = nx.DiGraph()

    def edges(self, data=False):
        return list(self.graph.edges(data=data))

    def nodes(self):
        return list(self.graph.nodes())

    def remove_edge(self, src, dest):
        self.graph.remove_edge(src, dest)

    def add_edge(self, src, dest, capacity=1):
        self.graph.add_edge(src, dest, capacity=capacity)

    def add_edges(self, edges: List):
        self.graph.add_edges_from(edges)

    def add_nodes(self, nodes):
        self.graph.add_nodes_from(nodes)

    def build_manually(self, nodes: List, edges: List):
        self.add_nodes(nodes=nodes)
        self.add_edges(edges=edges)

    def build_un_directed_edges(self, edges):
        self.graph.clear()
        temp = []
        for edge in edges:
            temp.append((edge[0], edge[1], {'capacity': 1}))
            temp.append((edge[1], edge[0], {'capacity': 1}))

        return temp

    def print_graph(self):
        # Draw the graph using ASCII art
        for node in self.graph.nodes():
            neighbors = list(self.graph.neighbors(node))
            print(f"Node {node}: ==> {neighbors}")
