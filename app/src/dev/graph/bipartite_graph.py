import math
import random
from typing import List, Tuple, Set

from networkx import DiGraph
from graph.graph import Graph
from networkx.algorithms import bipartite


class BipartiteGraph(Graph):
    red_nodes: Set
    blue_nodes: Set

    def __init__(self):
        super().__init__()
        self.red_nodes = set()
        self.blue_nodes = set()

    def is_bipartite(self) -> bool:
        res = bipartite.is_bipartite(self.graph)
        return res

    def split_nodes(self) -> None:
        color_map = bipartite.color(self.graph)

        for k, v in color_map.items():
            if v == 1:
                self.red_nodes.add(k)
            if v == 0:
                self.blue_nodes.add(k)

    def random_build(self, num_of_nodes, density):
        self.graph = DiGraph()
        red_nodes = set(range(0, math.ceil(num_of_nodes / 2)))
        blue_nodes = set(range(len(red_nodes), num_of_nodes))

        self.red_nodes = red_nodes
        self.blue_nodes = blue_nodes

        nodes = red_nodes | blue_nodes

        num_of_edges = math.ceil((len(red_nodes) * len(blue_nodes)) * density)

        possible_edges = []
        for red_node in red_nodes:
            for blue_node in blue_nodes:
                possible_edges.append((red_node, blue_node))

        random.shuffle(possible_edges)
        selected_edges = possible_edges[:num_of_edges]

        edges = []

        for i, j in selected_edges:
            edges.append((i, j, {'capacity': 1}))
            edges.append((j, i, {'capacity': 1}))

        self.build_manually(nodes=list(nodes), edges=edges)


