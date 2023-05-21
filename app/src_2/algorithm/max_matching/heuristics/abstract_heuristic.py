from typing import Tuple, List
from abc import abstractmethod

from app.src_2.graph.bipartite_graph import BipartiteGraph


class AbstractHeuristic:
    bipartite_graph: BipartiteGraph
    matching_edges: List

    def __init__(self, bipartite_graph: BipartiteGraph):
        self.bipartite_graph = bipartite_graph
        self.matching_edges = []

    def execute(self):
        self.matching_edges = self.find_matching_edges()
        # initial_flow_network = self.build_initial_flow()
        # return initial_flow_network

    @abstractmethod
    def find_matching_edges(self) -> List[Tuple]:
        pass

    def get_node_neighbors(self, node):
        blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
        return blue_neighbors

    @staticmethod
    def check_if_node_matched(node, matched_nodes):
        return node in matched_nodes
