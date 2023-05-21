import copy
from typing import Tuple, List
from abc import abstractmethod

from app.src_2.graph.bipartite_graph import BipartiteGraph


class AbstractHeuristic:
    bipartite_graph: BipartiteGraph
    matching_edges: List
    source_sink = ['source', 'sink']

    def __init__(self, bipartite_graph: BipartiteGraph):
        self.bipartite_graph = bipartite_graph
        self.matching_edges = []

    def execute(self):
        self.matching_edges = self.find_matching_edges()
        initial_flow_network = self.build_initial_flow()
        return initial_flow_network

    @abstractmethod
    def find_matching_edges(self) -> List[Tuple]:
        pass

    def get_node_neighbors(self, node):
        blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
        return blue_neighbors

    @staticmethod
    def check_if_node_matched(node, matched_nodes):
        return node in matched_nodes

    def build_initial_flow(self):
        residual_network = copy.deepcopy(self.bipartite_graph.graph)
        residual_network.graph["inf"] = float("inf")

        for u, v, d in residual_network.edges(data=True):
            d["flow"] = 0

        for u, v in self.matching_edges:
            residual_network[u][v]['flow'] = 1
            residual_network['source'][u]['flow'] = 1
            residual_network[v]['sink']['flow'] = 1

            residual_network[v][u]['flow'] = 0
            residual_network[u]['source']['flow'] = 0
            residual_network['sink'][v]['flow'] = 0
        print('3333333333333333333333333333333333333333333333333333333333333333333333333333333333')
        print(self.matching_edges)
        print('3333333333333333333333333333333333333333333333333333333333333333333333333333333333')
        print(len(self.matching_edges))
        print('------------------------------------------------')
        for u, v in residual_network.edges:
            print(u, '-->', v, 'flow:', residual_network[u][v]['flow'], 'capacity', residual_network[u][v]['capacity'])
        print('------------------------------------------------')

        return residual_network
