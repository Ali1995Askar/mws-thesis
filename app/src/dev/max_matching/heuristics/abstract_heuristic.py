from copy import deepcopy
from abc import abstractmethod
from typing import Tuple, List, Set

from graph.bipartite_graph import BipartiteGraph


class AbstractHeuristic:
    bipartite_graph: BipartiteGraph
    matching_edges: List
    source_sink = ['source', 'sink']

    def __init__(self, bipartite_graph: BipartiteGraph):
        self.bipartite_graph = deepcopy(bipartite_graph)
        self.matching_edges = []

    def execute(self):
        self.matching_edges = self.get_matching_edges()
        initial_flow_network = self.build_initial_flow()
        return initial_flow_network

    @abstractmethod
    def get_matching_edges(self) -> List[Tuple]:
        pass

    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        unmatched_set = set(self.source_sink)
        unmatched_set |= matched_nodes
        for neighbor in neighbors:
            if neighbor not in unmatched_set:
                return neighbor
        return None

    def get_node_neighbors(self, node):
        blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
        return blue_neighbors

    @staticmethod
    def check_if_node_matched(node, matched_nodes):
        return node in matched_nodes

    def build_initial_flow(self):
        residual_network = deepcopy(self.bipartite_graph.graph)
        residual_network.graph["inf"] = float("inf")

        for u, v, d in residual_network.edges(data=True):
            d["flow"] = 0

        for u, v in self.matching_edges:
            residual_network[u][v]['flow'] += 1
            residual_network['source'][u]['flow'] += 1
            residual_network[v]['sink']['flow'] += 1

            residual_network[v][u]['flow'] -= 1
            residual_network[u]['source']['flow'] -= 1
            residual_network['sink'][v]['flow'] -= 1

        return residual_network
