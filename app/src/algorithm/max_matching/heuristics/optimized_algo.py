from typing import List, Set, Dict

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class OptimizedAlgo(AbstractHeuristic):
    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        matching_blue_red = {}
        matched_nodes = set()
        matched_edges = set()

        node_degree = list(self.bipartite_graph.graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
        sorted_red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        for node, _ in sorted_red_nodes:
            blue_neighbors = list(self.bipartite_graph.graph.neighbors(node))
            free_blue_neighbor = self.find_un_matched_neighbor(blue_neighbors, matched_nodes)

            if free_blue_neighbor:
                matched_nodes.add(node)
                matched_nodes.add(free_blue_neighbor)
                matched_edges.add((node, free_blue_neighbor))
                matching_blue_red[free_blue_neighbor] = node
                continue

            else:
                print('Print Cant find')
                replace_data = self.get_replace_data(matched_nodes, blue_neighbors, matching_blue_red)
                print(replace_data)
                if not replace_data:
                    continue

                old_blue = replace_data[0]
                old_red = replace_data[1]
                new_blue = replace_data[2]

                matched_nodes.add(node)
                matched_nodes.add(new_blue)

                matched_edges.remove((old_red, old_blue))
                matched_edges.add((old_red, new_blue))
                matched_edges.add((node, old_blue))

                matching_blue_red[new_blue] = old_red
                matching_blue_red[old_blue] = node

        return list(matched_edges)

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        for neighbor in neighbors:
            if not self.check_if_node_matched(neighbor, matched_nodes):
                return neighbor
        return None

    def get_replace_data(self, matched_nodes, neighbors, matching_dict):

        for neighbor in neighbors:
            matched_red_node = matching_dict[neighbor]
            blue_neighbors = self.bipartite_graph.graph.neighbors(matched_red_node)

            for blue_node in blue_neighbors:
                if not self.check_if_node_matched(blue_node, matched_nodes):
                    return neighbor, matched_red_node, blue_node

        return None
