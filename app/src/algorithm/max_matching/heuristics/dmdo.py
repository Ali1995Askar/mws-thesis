from typing import List, Set, Dict
from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class DMDO(AbstractHeuristic):
    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        temp_graph = self.bipartite_graph.graph.copy()
        matching_edges = set()
        matched_nodes = set()
        node_degree = list(temp_graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        while red_nodes:
            red_node = red_nodes.pop(0)[0]

            if self.check_if_node_matched(red_node, matched_nodes):
                continue

            blue_neighbors = list(self.bipartite_graph.graph.neighbors(red_node))
            free_blue_neighbor = self.find_un_matched_neighbor(blue_neighbors, matched_nodes)

            if not free_blue_neighbor:
                continue

            edge = (red_node, free_blue_neighbor)

            temp_graph.remove_node(red_node)
            temp_graph.remove_node(free_blue_neighbor)

            matching_edges.add(edge)
            matched_nodes.add(red_node)
            matched_nodes.add(free_blue_neighbor)

            node_degree = list(temp_graph.out_degree)
            red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
            red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        return list(matching_edges)

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        for neighbor in neighbors:
            if not self.check_if_node_matched(neighbor, matched_nodes):
                return neighbor
        return None
