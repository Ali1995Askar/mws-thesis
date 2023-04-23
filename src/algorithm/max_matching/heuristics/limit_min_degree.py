import random

from src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class LimitMinDegree(AbstractHeuristic):

    @staticmethod
    def sort_by_degree(node_degree):
        return node_degree[1]

    def find_matching_edges(self):
        limit = 3
        temp_graph = self.bipartite_graph.graph.copy()
        source_sink = ['source', 'sink']
        matching_edges = set()
        matched_nodes = []
        node_degree = list(temp_graph.out_degree)

        red_nodes = [node for node in node_degree if node[0] in
                     self.bipartite_graph.red_nodes and node[1] < limit]

        ss = sorted(red_nodes, key=self.sort_by_degree)
        print('bye', red_nodes)
        red_nodes_big_degree = [node for node in self.bipartite_graph.red_nodes if
                                not any(n[0] == node for n in red_nodes)]

        print('hello', red_nodes_big_degree)

        while ss:
            red_node = ss.pop(0)[0]
            print('red_node', red_node)
            if red_node in matched_nodes or red_node in source_sink:
                continue

            blue_neighbors = list(temp_graph.neighbors(red_node))
            for blue_neighbor in blue_neighbors:
                if blue_neighbor in matching_edges:
                    continue
                edge = (red_node, blue_neighbor)
                print('delete node', red_node, blue_neighbor)
                temp_graph.remove_node(red_node)
                temp_graph.remove_node(blue_neighbor)
                matching_edges.add(edge)
                matched_nodes.extend([red_node, blue_neighbor])
                node_degree = list(temp_graph.out_degree)
                red_nodes = [node for node in node_degree if node[0] in self.bipartite_graph.red_nodes]
                red_nodes = sorted(red_nodes, key=self.sort_by_degree)

                break
        if red_nodes_big_degree:
            for red_node in red_nodes_big_degree:
                neighbors = [
                    node for node in list(temp_graph.neighbors(red_node)) if node not in source_sink
                ]
                if not neighbors:
                    continue
                blue_node = random.choice(neighbors)
                matching_edges.add((red_node, blue_node))
                temp_graph.remove_node(red_node)
                temp_graph.remove_node(blue_node)

        return list(matching_edges)
