from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class StaticMinDegreeAlgo(AbstractHeuristic):
    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        matching_edges = set()
        matched_nodes = []

        node_degree = list(self.bipartite_graph.graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        sorted_red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        for red_node, _ in sorted_red_nodes:
            if self.check_if_node_matched(red_node, matched_nodes):
                continue

            blue_neighbors = self.get_node_neighbors(red_node)
            if red_node in self.source_sink:
                continue

            for blue_node in blue_neighbors:

                if blue_node in self.source_sink:
                    continue

                if self.check_if_node_matched(blue_node, matched_nodes):
                    continue

                matching_edges.add((red_node, blue_node))
                matched_nodes.append(red_node)
                matched_nodes.append(blue_node)

                break

        return list(matching_edges)
