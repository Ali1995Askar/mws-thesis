from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class DynamicMinDegreeAlgo(AbstractHeuristic):

    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        temp_graph = self.bipartite_graph.graph.copy()
        matching_edges = set()
        matched_nodes = []
        node_degree = list(temp_graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        while red_nodes:
            red_node = red_nodes.pop(0)[0]

            if self.check_if_node_matched(red_node, matched_nodes):
                continue

            blue_neighbors = self.get_node_neighbors(red_node)

            for blue_neighbor in blue_neighbors:
                if self.check_if_node_matched(blue_neighbor, matched_nodes):
                    continue

                if blue_neighbor in self.source_sink or red_node in self.source_sink:
                    continue

                edge = (red_node, blue_neighbor)

                temp_graph.remove_node(red_node)
                temp_graph.remove_node(blue_neighbor)

                matching_edges.add(edge)

                matched_nodes.append(red_node)
                matched_nodes.append(blue_neighbor)

                node_degree = list(temp_graph.out_degree)
                red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
                red_nodes = sorted(red_nodes, key=self.sort_by_degree)
                break

        return list(matching_edges)
