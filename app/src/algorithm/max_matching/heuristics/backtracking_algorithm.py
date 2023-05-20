from typing import Any, Set
from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class BacktrackingAlgorithm(AbstractHeuristic):
    def find_matching_edges(self):
        matched_nodes = set()
        matched_edges = set()
        un_matched_edges = set(self.bipartite_graph.edges())

        bmm = self.get_best_case_matching_num()
        cm = 0

        for node in self.bipartite_graph.red_nodes:
            if cm == bmm:
                break

            neighbor = self.find_un_matched_neighbor(node, matched_nodes)

            if neighbor:
                matched_nodes.add(node)
                matched_nodes.add(neighbor)
                matched_edges.add((node, neighbor))
                un_matched_edges.remove((node, neighbor))
                cm += 1
                continue

            nn = list(self.bipartite_graph.graph.neighbors(node))
            mn = self.find_matched_nodes(nn, matched_edges)
            choice = self.find_best_choice(mn, matched_nodes, un_matched_edges)

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
    def find_best_choice(nodes, match_nodes, un_matched_edges):
        for un_matched_edge in un_matched_edges:
            if un_matched_edge[0] in nodes and un_matched_edge[1] not in match_nodes:
                return un_matched_edge

    def find_un_matched_neighbor(self, node: Any, matched_nodes: Set):
        for neighbor in self.bipartite_graph.graph.neighbors(node):
            if neighbor not in matched_nodes:
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
