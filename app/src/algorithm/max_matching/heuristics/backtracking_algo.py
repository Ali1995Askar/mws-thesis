from typing import Set, List
from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class BackTrackingAlgo(AbstractHeuristic):

    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        matched_nodes = set()
        matched_edges = set()
        un_matched_edges = set(self.bipartite_graph.edges())

        bmm = self.get_best_case_matching_num()
        cm = 0

        node_degree = list(self.bipartite_graph.graph.out_degree)
        red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]

        sorted_red_nodes = sorted(red_nodes, key=self.sort_by_degree)

        for node, _ in sorted_red_nodes:
            if cm == bmm:
                break

            neighbors = list(self.bipartite_graph.graph.neighbors(node))
            free_neighbor = self.find_un_matched_neighbor(neighbors, matched_nodes)

            if free_neighbor:
                matched_nodes.add(node)
                matched_nodes.add(free_neighbor)
                assert self.bipartite_graph.has_edge_with_positive_capacity(node, free_neighbor)
                matched_edges.add((node, free_neighbor))
                un_matched_edges.remove((node, free_neighbor))
                cm += 1
                continue

            mn = self.find_matched_nodes(neighbors, matched_edges)
            if not mn:
                continue

            choice = self.find_other_choice(mn, matched_nodes, un_matched_edges)

            if not choice:
                continue

            edge_to_replace = self.get_old_edge(choice, matched_edges)

            matched_edges.remove(edge_to_replace)
            un_matched_edges.add(edge_to_replace)

            un_matched_edges.remove(choice)
            matched_edges.add(choice)
            matched_edges.add((node, edge_to_replace[1]))

            assert self.bipartite_graph.has_edge_with_positive_capacity(choice[0], choice[1])

            matched_nodes |= {node, edge_to_replace[1], choice[1]}

            cm += 1

        return list(matched_edges)

    # def find_other_choice(self, nodes, match_nodes, un_matched_edges):
    #     for u, v in un_matched_edges:
    #         if u in nodes and v not in match_nodes:
    #             if u in self.bipartite_graph.red_nodes and v in self.bipartite_graph.blue_nodes:
    #                 return u, v

    def find_other_choice(self, nodes, match_nodes, un_matched_edges):
        blue_nodes = self.bipartite_graph.blue_nodes
        for u, v in un_matched_edges:
            if u in nodes and v not in match_nodes and u in self.bipartite_graph.red_nodes and v in blue_nodes:
                return u, v
        return None

    # def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
    #     for neighbor in neighbors:
    #         if neighbor not in matched_nodes and neighbor not in self.source_sink:
    #             return neighbor
    #     return None

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        unmatched_set = set(self.source_sink)
        unmatched_set |= matched_nodes
        for neighbor in neighbors:
            if neighbor not in unmatched_set:
                return neighbor
        return None

    @staticmethod
    def find_matched_nodes(node_neighbors, matched_edges):

        res = []
        for node_neighbor in node_neighbors:
            for tup in matched_edges:
                if tup[1] == node_neighbor:
                    res.append(tup[0])

        return res

    def get_best_case_matching_num(self):
        max_size_of_matching = min(len(self.bipartite_graph.red_nodes), len(self.bipartite_graph.blue_nodes))
        return max_size_of_matching

    @staticmethod
    def get_old_edge(choice, matched_edges):
        for u, v in matched_edges:
            if u == choice[0]:
                return u, v
