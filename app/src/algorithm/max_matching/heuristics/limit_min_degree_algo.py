import random
from operator import itemgetter
from app.src.graph.bipartite_graph import BipartiteGraph

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class LimitMinDegreeAlgo(AbstractHeuristic):

    def __init__(self, bipartite_graph: BipartiteGraph):
        super().__init__(bipartite_graph)
        self.limit_val = None
        self.temp_graph = None

    def find_matching_edges(self):
        matching_edges = set()
        matched_nodes = set()
        self.limit_val = self.get_limit_value()
        self.temp_graph = self.bipartite_graph.graph.copy()

        # Create sets for the matched and unmatched red nodes
        red_nodes_low_degree = self.get_nodes_with_degree_less_than_limit()
        unmatched_red_nodes = list(map(itemgetter(0), red_nodes_low_degree))

        # Sort the red nodes by degree
        red_nodes = sorted(red_nodes_low_degree, key=self.sort_by_degree)

        # Find the matching edges
        while red_nodes:
            red_node, degree = red_nodes.pop(0)

            if red_node in self.source_sink or self.check_if_node_matched(red_node, matched_nodes):
                continue

            blue_neighbors = self.temp_graph.neighbors(red_node)

            for blue_neighbor in blue_neighbors:
                if self.check_if_node_matched(blue_neighbor, matched_nodes):
                    continue

                if blue_neighbor in self.source_sink:
                    continue
                    
                edge = (red_node, blue_neighbor)

                self.temp_graph.remove_node(red_node)
                self.temp_graph.remove_node(blue_neighbor)

                matching_edges.add(edge)
                matched_nodes.add(red_node)
                matched_nodes.add(blue_neighbor)

                unmatched_red_nodes.remove(red_node)
                self.re_sort_nodes(unmatched_red_nodes)

                break

        # Find matching edges for the remaining unmatched red nodes with high degree
        matching_edges = self.process_big_degrees_nodes(unmatched_red_nodes, matching_edges)
        return list(matching_edges)

    def get_limit_value(self):
        degrees = [deg[1] for deg in self.bipartite_graph.graph.degree()]
        limit_val = (max(degrees) + min(degrees)) // 2
        return limit_val

    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def re_sort_nodes(self, unmatched_red_nodes):
        nodes_with_degree = []
        for node, degree in self.temp_graph.out_degree:
            if node not in unmatched_red_nodes:
                continue

            if degree > self.limit_val:
                continue

            nodes_with_degree.append((node, degree))

        return sorted(nodes_with_degree)

    def get_nodes_with_degree_less_than_limit(self):
        nodes_with_degree = []
        for node, degree in self.temp_graph.out_degree:
            if node not in self.bipartite_graph.red_nodes:
                continue

            if degree > self.limit_val:
                continue

            nodes_with_degree.append((node, degree))

        return nodes_with_degree

    def process_big_degrees_nodes(self, unmatched_red_nodes, matching_edges):
        for red_node in unmatched_red_nodes:

            neighbors = set(self.temp_graph.neighbors(red_node))
            if not neighbors:
                continue

            blue_node = random.choice(list(neighbors))
            matching_edges.add((red_node, blue_node))
            self.temp_graph.remove_node(red_node)
            self.temp_graph.remove_node(blue_node)

        return matching_edges
