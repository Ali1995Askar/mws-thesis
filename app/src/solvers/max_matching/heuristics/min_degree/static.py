from typing import List, Tuple
from app.src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class StaticMinDegreeHeuristic(AbstractHeuristic):
    def get_matching_edges(self) -> List[Tuple]:
        matching_edges = set()
        matched_nodes = set()

        node_degree = list(self.bipartite_graph.graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        sorted_red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        for red_node, _ in sorted_red_nodes:
            neighbors = self.get_node_neighbors(red_node)
            free_blue_neighbor = self.find_un_matched_neighbor(neighbors, matched_nodes)

            if not free_blue_neighbor:
                continue

            matched_nodes.add(red_node)
            matched_nodes.add(free_blue_neighbor)
            matching_edges.add((red_node, free_blue_neighbor))

        return list(matching_edges)
