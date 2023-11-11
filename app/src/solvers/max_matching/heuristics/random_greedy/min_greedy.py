from typing import List, Tuple

from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class MinGreedy(AbstractHeuristic):
    def find_un_matched_low_degree_neighbor(self, blue_neighbors, matched_nodes):
        return min((node for node in blue_neighbors if not self.check_if_node_matched(node, matched_nodes)),
                   key=lambda neighbor: len(list(self.bipartite_graph.graph.neighbors(neighbor))),
                   default=None)

    def get_matching_edges(self) -> List[Tuple]:
        graph = self.bipartite_graph.graph
        matched_nodes = set()
        matching_edges = set()
        red_nodes = self.bipartite_graph.red_nodes

        while len(red_nodes) > 0:
            node = red_nodes.pop()
            blue_neighbors = self.get_node_neighbors(node)

            if not blue_neighbors:
                graph.remove_node(node)
                continue

            free_blue_neighbor = self.find_un_matched_low_degree_neighbor(blue_neighbors, matched_nodes)

            if not free_blue_neighbor:
                red_nodes.remove(node)
                graph.remove_node(node)
                continue

            matching_edges.add((node, free_blue_neighbor))
            matched_nodes.add(node)
            matched_nodes.add(free_blue_neighbor)

            graph.remove_node(free_blue_neighbor)
            graph.remove_node(node)

        return list(matching_edges)
