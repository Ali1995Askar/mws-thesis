from typing import List, Set, Dict

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class SMDO(AbstractHeuristic):
    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        matching_blue_red = {}
        matched_nodes = set()
        matched_edges = set()

        node_degree = list(self.bipartite_graph.graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        sorted_red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        for node, _ in sorted_red_nodes:
            if self.check_if_node_matched(node, matched_nodes):
                continue

            blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
            free_blue_neighbor = self.find_un_matched_neighbor(blue_neighbors, matched_nodes)

            if free_blue_neighbor:
                matched_nodes.add(node)
                matched_nodes.add(free_blue_neighbor)
                matched_edges.add((node, free_blue_neighbor))
                matching_blue_red[free_blue_neighbor] = node
                continue

        return list(matched_edges)

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        for neighbor in neighbors:
            if not self.check_if_node_matched(neighbor, matched_nodes):
                return neighbor
        return None
  