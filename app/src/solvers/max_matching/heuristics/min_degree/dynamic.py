from typing import List, Tuple

from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class DynamicMinDegreeHeuristic(AbstractHeuristic):

    def get_matching_edges(self) -> List[Tuple]:
        temp = self.bipartite_graph.get_graph_copy()

        matching_edges = set()
        matched_nodes = set()

        red_with_degrees = list(item for item in temp.out_degree if
                                item[0] not in matched_nodes and item[0] in self.bipartite_graph.red_nodes)
        sorted_red_nodes = sorted(red_with_degrees, key=self.sort_by_degree)

        while len(sorted_red_nodes) > 0:
            red_node, degree = sorted_red_nodes.pop(0)

            blue_neighbors = self.get_node_neighbors(red_node)
            free_blue_neighbor = self.find_un_matched_neighbor(blue_neighbors, matched_nodes)

            if not free_blue_neighbor:
                continue

            matched_nodes.add(red_node)
            matched_nodes.add(free_blue_neighbor)
            matching_edges.add((red_node, free_blue_neighbor))

            temp.remove_node(red_node)
            temp.remove_node(free_blue_neighbor)

            red_with_degrees = list(item for item in temp.out_degree if
                                    item[0] not in matched_nodes and item[0] in self.bipartite_graph.red_nodes)
            sorted_red_nodes = sorted(red_with_degrees, key=self.sort_by_degree)

        return list(matching_edges)
