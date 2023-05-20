from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class StaticMinDegree(AbstractHeuristic):
    def find_matching_edges(self):
        matching_edges = set()
        matched_nodes = []
        red_nodes = sorted(self.bipartite_graph.red_nodes, key=self.bipartite_graph.graph.degree)

        for red_node in red_nodes:
            if self.check_if_node_matched(red_node, matched_nodes):
                continue

            blue_neighbors = self.get_node_neighbors(red_node)

            for blue_node in blue_neighbors:

                if self.check_if_node_matched(blue_node, matched_nodes):
                    continue

                edge = (red_node, blue_node)
                matching_edges.add(edge)
                matched_nodes.extend([red_node, blue_node])
                break

        return list(matching_edges)
