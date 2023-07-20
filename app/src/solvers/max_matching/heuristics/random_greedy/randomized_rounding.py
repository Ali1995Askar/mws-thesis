import random
from typing import List, Tuple

from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class RandomizedRoundingHeuristic(AbstractHeuristic):
    def get_matching_edges(self) -> List[Tuple]:
        matching_edges = set()
        matched_nodes = set()
        red_nodes = self.bipartite_graph.red_nodes

        for red_node in red_nodes:

            if random.random() < 0.5:
                continue

            neighbors = self.get_node_neighbors(red_node)
            free_blue_neighbor = self.find_un_matched_neighbor(neighbors, matched_nodes)

            if not free_blue_neighbor:
                continue

            matching_edges.add((red_node, free_blue_neighbor))
            matched_nodes.add(red_node)
            matched_nodes.add(free_blue_neighbor)

        return list(matching_edges)
