from src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class StaticMinDegree(AbstractHeuristic):
    def find_matching_edges(self):
        source_sink = ['source', 'sink']
        matching_edges = set()
        matched_nodes = []
        red_nodes = sorted(self.bipartite_graph.red_nodes, key=self.bipartite_graph.graph.degree)

        for red_node in red_nodes:
            if red_node in source_sink or red_node in matched_nodes:
                continue
            blue_neighbors = list(self.bipartite_graph.graph.neighbors(red_node))

            for blue_node in blue_neighbors:
                if blue_node not in matched_nodes and blue_node not in source_sink:
                    edge = (red_node, blue_node)

                    matching_edges.add(edge)
                    matched_nodes.extend([red_node, blue_node])
                    break
        return list(matching_edges)
