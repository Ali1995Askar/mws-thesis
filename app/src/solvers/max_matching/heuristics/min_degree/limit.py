from typing import List, Tuple
from src.graph.bipartite_graph import BipartiteGraph
from src.solvers.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class LimitMinDegreeHeuristic(AbstractHeuristic):

    def __init__(self, bipartite_graph: BipartiteGraph):
        super().__init__(bipartite_graph)
        self.limit_val = None

    def get_limit_value(self) -> int:
        degrees = list(self.bipartite_graph.graph.out_degree)
        max_tuple = max(degrees, key=lambda x: x[1])
        min_tuple = min(degrees, key=lambda x: x[1])
        limit_val = (max_tuple[1] - min_tuple[1]) // 2

        if min_tuple[1] > max_tuple[1]:
            print(degrees)
            print(max_tuple)
            print(min_tuple)
            raise Exception

        return limit_val

    def get_matching_edges(self) -> List[Tuple]:
        temp = self.bipartite_graph.get_graph_copy()
        self.limit_val = self.get_limit_value()

        big_degree_nodes = set()
        matching_edges = set()
        matched_nodes = set()

        red_with_degrees = list(item for item in temp.out_degree if
                                item[0] not in matched_nodes and item[0] in self.bipartite_graph.red_nodes)
        sorted_red_nodes = sorted(red_with_degrees, key=self.sort_by_degree)

        while len(sorted_red_nodes) > 0:
            red_node, degree = sorted_red_nodes.pop(0)
            if degree > self.limit_val:
                big_degree_nodes.add(red_node)
            else:
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

        matching = self.process_big_degrees(temp, big_degree_nodes, matched_nodes)
        matching_edges |= matching
        return list(matching_edges)

    def process_big_degrees(self, temp, big_degree_nodes, matched_nodes):
        matching = set()
        for red_node in big_degree_nodes:
            neighbors = list(temp.neighbors(red_node))
            free_blue_neighbor = self.find_un_matched_neighbor(neighbors, matched_nodes)
            if not free_blue_neighbor:
                continue
            matching.add((red_node, free_blue_neighbor))
            temp.remove_node(red_node)
            temp.remove_node(free_blue_neighbor)

        return matching
