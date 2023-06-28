from typing import List, Tuple, Set

from max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class SimpleGreedyHeuristic(AbstractHeuristic):
    def get_matching_edges(self) -> List[Tuple]:
        matching_blue_red = {}
        matched_nodes = set()
        matched_edges = set()
        red_nodes = self.bipartite_graph.red_nodes

        for node in red_nodes:

            blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
            free_blue_neighbor = self.find_un_matched_neighbor(blue_neighbors, matched_nodes)

            if free_blue_neighbor:
                matched_nodes.add(node)
                matched_nodes.add(free_blue_neighbor)
                matched_edges.add((node, free_blue_neighbor))
                matching_blue_red[free_blue_neighbor] = node

        return list(matched_edges)
