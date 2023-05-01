import random

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class RandomizedRounding(AbstractHeuristic):
    def find_matching_edges(self):
        source_sink = ['source', 'sink']
        red_nodes = self.bipartite_graph.red_nodes
        blue_nodes = self.bipartite_graph.blue_nodes
        matched_nodes = []
        matching = set()
        for u, v in self.bipartite_graph.graph.edges():
            if u not in source_sink and v not in source_sink and random.random() < 0.5:
                if u in red_nodes and v in blue_nodes and u not in matched_nodes and v not in matched_nodes:
                    matching.add((u, v))
                    matched_nodes.extend([u, v])
        matching_edges = list(matching)
        return matching_edges
