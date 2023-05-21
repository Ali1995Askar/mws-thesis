import math
import random
from typing import List, Tuple
from app.src.graph.graph import Graph
from networkx.algorithms import bipartite


class BipartiteGraph(Graph):
    red_nodes: List
    blue_nodes: List

    def is_bipartite(self) -> bool:
        res = bipartite.is_bipartite(self.graph)
        return res

    @property
    def density_rate(self):
        density_rate = self.graph.number_of_edges() / (len(self.red_nodes) * len(self.blue_nodes))
        return density_rate

    def split_nodes(self) -> Tuple[List, List]:
        color_map = bipartite.color(self.graph)
        self.red_nodes = [k for k, v in color_map.items() if v == 1]
        self.blue_nodes = [k for k, v in color_map.items() if v == 0]
        return self.red_nodes, self.blue_nodes

    def random_build(self, num_of_nodes, density):

        self.graph.clear()
        red_nodes = set(range(0, math.ceil(num_of_nodes / 2)))
        blue_nodes = set(range(len(red_nodes), num_of_nodes))

        self.red_nodes = list(red_nodes)
        self.blue_nodes = list(blue_nodes)

        nodes = red_nodes | blue_nodes

        num_of_edges = math.ceil((len(red_nodes) * len(blue_nodes)) * density)
        print(num_of_edges)
        possible_edges = []
        for red_node in red_nodes:
            for blue_node in blue_nodes:
                possible_edges.append((red_node, blue_node))

        random.shuffle(possible_edges)
        selected_edges = possible_edges[:num_of_edges]

        edges = []
        # Create the edges with capacity 1
        for i, j in selected_edges:
            edges.append((i, j, {'capacity': 1}))
            edges.append((j, i, {'capacity': 1}))

        self.build_manually(nodes=list(nodes), edges=edges)
