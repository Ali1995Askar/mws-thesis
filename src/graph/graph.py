import networkx as nx
from typing import List


class Graph:
    graph: nx.DiGraph

    def __init__(self):
        self.graph = nx.DiGraph()

    @property
    def density_rate(self):
        density_rate = nx.density(self.graph)
        return density_rate

    @property
    def sparse_rate(self) -> float:
        sparse_rate = 1 - nx.density(self.graph)
        return sparse_rate

    def remove_edge(self, src, dest):
        self.graph.remove_edge(src, dest)

    def add_edges(self, edges: List):
        self.graph.add_edges_from(edges)

    def add_nodes(self, nodes):
        self.graph.add_nodes_from(nodes)

    def get_neighbors(self, node):
        neighbors = list(self.graph.successors(node))
        return neighbors

    def build_manually(self, nodes: List, edges: List):
        self.add_nodes(nodes=nodes)
        self.add_edges(edges=edges)

    def read_graph_from_json(self):
        pass

    def print_pretty(self):
        pass
