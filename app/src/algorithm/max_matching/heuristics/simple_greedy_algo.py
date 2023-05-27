from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class SimpleGreedyAlgo(AbstractHeuristic):

    def find_matching_edges(self):
        matching_edges = set()
        matched_nodes = []
        counter = 0
        edges = self.bipartite_graph.graph.edges()
        matched_nodes_number = len(self.bipartite_graph.red_nodes)

        for u, v in edges:

            if counter == matched_nodes_number:
                break

            if u in self.source_sink or v in self.source_sink:
                continue

            if u in matched_nodes or v in matched_nodes:
                continue

            matching_edges.add((u, v))
            matched_nodes.extend([u, v])
            counter += 1

        return list(matching_edges)
