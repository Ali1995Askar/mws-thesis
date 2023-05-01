from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class SimpleGreedy(AbstractHeuristic):
    def find_matching_edges(self):
        matching_edges = set()
        matched_nodes = []
        source_sink = ['source', 'sink']
        counter = 0
        edges = self.bipartite_graph.graph.edges()
        matched_nodes_number = len(self.bipartite_graph.red_nodes)

        for u, v in edges:
            if counter == matched_nodes_number:
                break
            if u not in matched_nodes and v not in matched_nodes and u not in source_sink and v not in source_sink:
                matching_edges.add((u, v))
                matched_nodes.extend([u, v])
                counter += 1
        return list(matching_edges)
