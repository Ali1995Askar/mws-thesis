import time
from copy import deepcopy, copy
from abc import abstractmethod
from typing import Tuple, List, Set
from src.graph.bipartite_graph import BipartiteGraph


class AbstractHeuristic:
    source_sink = ['source', 'sink']

    def __init__(self, bipartite_graph: BipartiteGraph):
        # self.bipartite_graph: BipartiteGraph = deepcopy(bipartite_graph)
        self.bipartite_graph: BipartiteGraph = bipartite_graph.get_instance_copy()
        self.matching_edges: List = []

    def execute(self):
        self.matching_edges = self.get_matching_edges()
        return self.matching_edges

    @abstractmethod
    def get_matching_edges(self) -> List[Tuple]:
        pass

    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        for neighbor in neighbors:
            if not self.check_if_node_matched(neighbor, matched_nodes):
                return neighbor
        return None

    def get_node_neighbors(self, node):
        blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
        return blue_neighbors

    @staticmethod
    def check_if_node_matched(node, matched_nodes):
        return node in matched_nodes
