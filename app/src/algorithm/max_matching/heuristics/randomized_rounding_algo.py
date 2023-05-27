import random
from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class RandomizedRoundingAlgo(AbstractHeuristic):
    def find_matching_edges(self):
        matched_nodes = []
        matching = set()

        red_nodes = self.bipartite_graph.red_nodes
        blue_nodes = self.bipartite_graph.blue_nodes

        for u, v in self.bipartite_graph.graph.edges():
            
            if u in self.source_sink or v in self.source_sink or random.random() < 0.5:
                continue

            if self.check_if_node_matched(u, matched_nodes) or self.check_if_node_matched(v, matched_nodes):
                continue

            if u not in red_nodes or v not in blue_nodes:
                continue

            matching.add((u, v))
            matched_nodes.append(u)
            matched_nodes.append(v)

        matching_edges = list(matching)
        return matching_edges
