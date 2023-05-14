import random
from typing import Any, Set

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class ModifiedAlgorithm(AbstractHeuristic):

    def find_matching_edges(self):
        matched_nodes = set()
        matched_edges = set()
        un_matched_edges = set()

        bmm = self.get_best_case_matching_num()
        cm = 0

        for node in self.bipartite_graph.red_nodes:
            neighbor = self.find_un_matched_neighbor(node, matched_nodes)

            if neighbor:
                matched_nodes.add(node)
                matched_nodes.add(neighbor)
                matched_edges.add((node, neighbor))
                cm += 1
                continue

            if cm == bmm:
                break

        return list(matched_edges)

    def swap(self):
        pass

    def find_un_matched_neighbor(self, node: Any, matched_nodes: Set):
        for neighbor in self.bipartite_graph.graph.neighbors(node):
            if neighbor not in matched_nodes:
                return neighbor
        return None

    def find_best_choice(self):
        pass

    def get_best_case_matching_num(self):
        max_size_of_matching = min(len(self.bipartite_graph.red_nodes), len(self.bipartite_graph.blue_nodes))
        return max_size_of_matching
