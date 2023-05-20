import copy
from abc import abstractmethod
from typing import Tuple, List
from app.utils.decorators import time_it
from app.src.graph.bipartite_graph import BipartiteGraph


class AbstractHeuristic:
    bipartite_graph: BipartiteGraph
    matching_edges: List
    source_sink = ['source', 'sink']

    def __init__(self, bipartite_graph: BipartiteGraph):
        self.bipartite_graph = bipartite_graph
        self.matching_edges = []

    def get_node_neighbors(self, node):
        blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
        return blue_neighbors

    @staticmethod
    def check_if_node_matched(node, matched_nodes):
        if node in AbstractHeuristic.source_sink or node in matched_nodes:
            return True
        return False

    @abstractmethod
    def find_matching_edges(self) -> List[Tuple]:
        pass

    @time_it
    def execute(self):
        self.matching_edges = self.find_matching_edges()
        initial_flow_network = self.build_initial_flow()
        return initial_flow_network

    def build_initial_flow(self):
        residual_network = copy.deepcopy(self.bipartite_graph.graph)
        residual_network.graph["inf"] = float("inf")

        for u, v, d in residual_network.edges(data=True):
            d["flow"] = 0

        for u, v in self.matching_edges:
            residual_network[u][v]['flow'] = 1
            residual_network['source'][u]['flow'] = 1
            residual_network[v]['sink']['flow'] = 1

            residual_network[v][u]['flow'] = -1
            residual_network[u]['source']['flow'] = -1
            residual_network['sink'][v]['flow'] = -1

        return residual_network
