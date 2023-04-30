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
            # print(f'edge number {edges_count} added successfully')
        self.build_manually(nodes=nodes, edges=edges)

    def fast_way(self, num_of_nodes, density):
        self.graph.clear()
        red_nodes = set(range(0, math.ceil(num_of_nodes / 2)))
        blue_nodes = set(range(len(red_nodes), num_of_nodes))

        nodes = red_nodes | blue_nodes

        num_of_edges = math.ceil((len(red_nodes) * len(blue_nodes)) * density)
        # Create a list of all possible edges between red and blue nodes

        possible_edges = []
        for red_node in red_nodes:
            for blue_node in blue_nodes:
                possible_edges.append((red_node, blue_node))

        # Shuffle the list of edges and select the desired number
        random.shuffle(possible_edges)
        selected_edges = possible_edges[:num_of_edges]

        edges = []
        # Create the edges with capacity 1
        for i, j in selected_edges:
            edges.append((i, j, {'capacity': 1}))
            edges.append((j, i, {'capacity': 1}))

        self.build_manually(nodes=list(nodes), edges=edges)
        # Create the graph and add the nodes and edges
        import networkx
        if networkx.is_bipartite(self.graph):
            print(f'build random bipartite graph with {num_of_nodes} nodes and {len(selected_edges)} edges')
        else:
            print(num_of_nodes, num_of_edges)
            print("Error: graph is not bipartite")
