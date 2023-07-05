import random
from typing import List, Tuple

from app.src.problems.max_matching.heuristics.abstract_heuristic import AbstractHeuristic

NUM_OF_ITERATION = 3


class MonteCarloHeuristic(AbstractHeuristic):
    def get_matching_edges(self) -> List[Tuple]:
        max_matching_size = 0
        max_matching_edges = set()

        for _ in range(NUM_OF_ITERATION):
            matching = set()
            matched_nodes = set()
            red_nodes = self.bipartite_graph.red_nodes
            random.shuffle(list(red_nodes))
            for red_node in red_nodes:
                neighbors = self.get_node_neighbors(red_node)
                free_blue_neighbor = self.find_un_matched_neighbor(neighbors, matched_nodes)

                if not free_blue_neighbor:
                    continue

                matched_nodes.add(red_node)
                matched_nodes.add(free_blue_neighbor)
                matching.add((red_node, free_blue_neighbor))

            matching_size = len(matching)

            if matching_size > max_matching_size:
                max_matching_size = matching_size
                max_matching_edges = matching

        return list(max_matching_edges)
