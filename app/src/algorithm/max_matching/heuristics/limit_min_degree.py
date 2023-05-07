import random

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class LimitMinDegree(AbstractHeuristic):

    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        # Compute the limit value
        degrees = [deg[1] for deg in self.bipartite_graph.graph.degree()]
        limit_val = (max(degrees) + min(degrees)) // 2

        # Copy the graph and create sets for the source/sink nodes and the matching edges
        temp_graph = self.bipartite_graph.graph.copy()
        source_sink = {'source', 'sink'}
        matching_edges = set()

        # Create sets for the matched and unmatched red nodes
        red_nodes = {(node, degree) for node, degree in temp_graph.out_degree if
                     node in self.bipartite_graph.red_nodes and degree < limit_val}
        unmatched_red_nodes = {node for node, _ in red_nodes}
        matched_nodes = set()

        # Sort the red nodes by degree
        red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        # Find the matching edges
        while red_nodes:
            red_node, degree = red_nodes.pop(0)
            if red_node in matched_nodes or red_node in source_sink:
                continue
            blue_neighbors = temp_graph.neighbors(red_node)
            for blue_neighbor in blue_neighbors:
                if blue_neighbor in matching_edges:
                    continue
                edge = (red_node, blue_neighbor)
                temp_graph.remove_node(red_node)
                temp_graph.remove_node(blue_neighbor)
                matching_edges.add(edge)
                matched_nodes.add(red_node)
                matched_nodes.add(blue_neighbor)
                unmatched_red_nodes.remove(red_node)
                red_nodes = sorted([(node, degree) for node, degree in temp_graph.out_degree if
                                    node in unmatched_red_nodes and degree < limit_val], key=self.sort_by_degree)
                break

        # Find matching edges for the remaining unmatched red nodes with high degree
        for red_node in unmatched_red_nodes:
            neighbors = set(temp_graph.neighbors(red_node)) - source_sink
            if not neighbors:
                continue
            blue_node = random.choice(list(neighbors))
            matching_edges.add((red_node, blue_node))
            temp_graph.remove_node(red_node)
            temp_graph.remove_node(blue_node)

        return list(matching_edges)
