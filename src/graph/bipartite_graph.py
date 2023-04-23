import copy
import math
import random
from typing import List, Tuple

from src.graph.graph import Graph
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
        self.red_nodes = [node for node in range(0, math.ceil(num_of_nodes / 2))]
        self.blue_nodes = [node for node in range(len(self.red_nodes), num_of_nodes)]

        nodes = []
        nodes.extend(self.red_nodes)
        nodes.extend(self.blue_nodes)

        num_of_edges = math.ceil((len(self.red_nodes) * len(self.blue_nodes)) * density)
        edges = []
        edges_count = len(edges)
        print(f'build random graph with {num_of_nodes} nodes and {num_of_edges} edges')
        while edges_count < num_of_edges:
            source = random.choice(self.red_nodes)
            target = random.choice(self.blue_nodes)
            if any(edge[0] == source and edge[1] == target for edge in edges):
                continue

            edges.append((source, target, {'capacity': 1}))
            edges.append((target, source, {'capacity': 1}))
            edges_count += 1
            print(f'edge number {edges_count} added successfully')
        self.build_manually(nodes=nodes, edges=edges)
