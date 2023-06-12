from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class SimpleGreedyAlgo(AbstractHeuristic):

    def find_matching_edges(self):
        matching_edges = set()
        matched_nodes = []
        edges = self.bipartite_graph.graph.edges()

        for u, v in edges:

            if u in self.source_sink or u in matched_nodes:
                continue

            if v in self.source_sink or v in matched_nodes:
                continue

            matching_edges.add((u, v))
            matched_nodes.append(u)
            matched_nodes.append(v)

        return list(matching_edges)
