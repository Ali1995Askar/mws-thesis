import random

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic

NUM_OF_ITERATION = 5


class MonteCarlo(AbstractHeuristic):
    def find_matching_edges(self):
        max_matching_size = 0
        max_matching_edges = set()

        for _ in range(NUM_OF_ITERATION):
            matching = set()
            matched_nodes = []
            red_nodes = self.bipartite_graph.red_nodes
            random.shuffle(red_nodes)
            for red_node in red_nodes:
                blue_neighbors = self.bipartite_graph.blue_nodes
                free_blue_neighbors = [n for n in blue_neighbors if
                                       n not in matched_nodes and self.bipartite_graph.graph.has_edge(red_node, n)]

                if free_blue_neighbors:
                    blue_neighbor = random.choice(free_blue_neighbors)
                    matched_nodes.extend([red_node, blue_neighbor])
                    matching.add((red_node, blue_neighbor))

            matching_size = len(matching)
            if matching_size > max_matching_size:
                max_matching_size = matching_size
                max_matching_edges = matching
        return list(max_matching_edges)
