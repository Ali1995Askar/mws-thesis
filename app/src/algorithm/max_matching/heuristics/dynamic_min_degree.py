from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class DynamicMinDegree(AbstractHeuristic):
    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        temp_graph = self.bipartite_graph.graph.copy()
        source_sink = ['source', 'sink']
        matching_edges = set()
        matched_nodes = []
        node_degree = list(temp_graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        while red_nodes:
            red_node = red_nodes.pop(0)[0]
            if red_node in matched_nodes or red_node in source_sink:
                continue

            blue_neighbors = list(temp_graph.neighbors(red_node))

            for blue_neighbor in blue_neighbors:
                if blue_neighbor in matching_edges:
                    continue

                edge = (red_node, blue_neighbor)
                temp_graph.remove_node(red_node)
                temp_graph.remove_node(blue_neighbor)
                matching_edges.add(edge)
                matched_nodes.extend([red_node, blue_neighbor])
                node_degree = list(temp_graph.out_degree)
                red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
                red_nodes = sorted(red_nodes, key=self.sort_by_degree)

                break

        return list(matching_edges)
