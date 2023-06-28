from typing import List, Set

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class StaticMinDegreeAlgo(AbstractHeuristic):
    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        for neighbor in neighbors:
            if not self.check_if_node_matched(neighbor, matched_nodes) and neighbor not in self.source_sink:
                return neighbor
        return None

    def find_matching_edges(self):
        matching_edges = set()
        matched_nodes = set()

        node_degree = list(self.bipartite_graph.graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        sorted_red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        for red_node, _ in sorted_red_nodes:
            if self.check_if_node_matched(red_node, matched_nodes):
                continue

            blue_neighbors = self.get_node_neighbors(red_node)

            if red_node in self.source_sink:
                continue

            blue_node = self.find_un_matched_neighbor(blue_neighbors, matched_nodes)

            if not blue_node:
                continue

            matching_edges.add((red_node, blue_node))
            matched_nodes.add(red_node)
            matched_nodes.add(blue_node)

        return list(matching_edges)
