import networkx as nx
from typing import Union
from networkx import Graph
from networkx.algorithms import bipartite


class BipartiteGraph:
    def __init__(self):
        self.graph: Union[Graph, None] = None

    def build_manual_graph(self, red_nodes, blue_nodes, edges):
        graph = Graph()
        graph.add_nodes_from(red_nodes, bipartite=0)
        graph.add_nodes_from(blue_nodes, bipartite=1)
        graph.add_edges_from(edges)
        self.graph: Graph = graph

    def build_random_graph(self, num_of_red_nodes, num_of_blue_nodes, edge_prob):
        self.graph = bipartite.random_graph(num_of_red_nodes, num_of_blue_nodes, edge_prob)

    def to_dict_of_lists(self):
        graph = nx.to_dict_of_lists(self.graph)
        return graph

    def to_edge_list(self):
        graph = nx.to_edgelist(self.graph)
        return graph

    def hopcroft_karp_matching(self):
        matching = nx.bipartite.maximum_matching(self.graph)
        return matching
