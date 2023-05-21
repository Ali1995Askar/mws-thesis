from typing import Set, List
from app.src_2.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


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

            neighbors = self.bipartite_graph.graph.neighbors(node)
            free_neighbor = self.find_un_matched_neighbor(neighbors, matched_nodes)

            if free_neighbor:
                matched_nodes.add(node)
                matched_nodes.add(free_neighbor)
                matched_edges.add((node, free_neighbor))
                un_matched_edges.remove((node, free_neighbor))
                cm += 1
                continue

            mn = self.find_matched_nodes(neighbors, matched_edges)
            choice = self.find_other_choice(mn, matched_nodes, un_matched_edges)

            if not choice:
                continue

            matched_edges.add(choice)
            un_matched_edges.remove(choice)

            neighbor = next((tup[1] for tup in matched_edges if tup[0] == choice[0]), None)

            matched_edges.remove((choice[0], neighbor))

            matched_edges.add((node, neighbor))

            un_matched_edges.add((choice[0], neighbor))
            matched_nodes |= {node, neighbor, choice[1]}

            cm += 1
        return list(matched_edges)

    @staticmethod
    def find_other_choice(nodes, match_nodes, un_matched_edges):
        for un_matched_edge in un_matched_edges:
            if un_matched_edge[0] in nodes and un_matched_edge[1] not in match_nodes:
                return un_matched_edge

    def find_un_matched_neighbor(self, neighbors: List, matched_nodes: Set):
        for neighbor in neighbors:
            if neighbor not in matched_nodes and neighbor not in self.source_sink:
                return neighbor
        return None

    @staticmethod
    def find_matched_nodes(node_neighbors, matched_edges):
        res = []
        for node_neighbor in node_neighbors:
            result = next((tup[0] for tup in matched_edges if tup[1] == node_neighbor), None)
            if result:
                res.append(result)
        return res

    def get_best_case_matching_num(self):
        max_size_of_matching = min(len(self.bipartite_graph.red_nodes), len(self.bipartite_graph.blue_nodes))
        return max_size_of_matching
