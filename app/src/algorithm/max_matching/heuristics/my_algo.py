import random

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic

NUM_OF_ITERATION = 5


class MyAlgo(AbstractHeuristic):
    def find_matching_edges(self):
        max_size_of_matching = min(len(self.bipartite_graph.red_nodes), len(self.bipartite_graph.blue_nodes))
        matched_nodes = set()
        max_matching_edges = set()
        matching = 0

        temp_matched_edges = set()
        temp_un_matched_edges = set()

        while matching < max_size_of_matching:
            for node in self.bipartite_graph.red_nodes:
                if node not in matched_nodes:
                    neighbors = self.bipartite_graph.graph.neighbors(node)
                    for neighbor in neighbors:
                        if neighbor not in matched_nodes:
                            matched_nodes.add(node)
                            matched_nodes.add(neighbor)
                            temp_matched_edges.add((node, neighbor))
                        else:
                            temp_un_matched_edges.add((node, neighbor))
                    matching += 1

        print(temp_matched_edges)
        print(temp_un_matched_edges)
        return list(max_matching_edges)

    @staticmethod
    def find_matched_edge(matched_edges, node):
        pass
