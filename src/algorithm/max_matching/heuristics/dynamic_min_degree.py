import heapq
from src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class DynamicMinDegree(AbstractHeuristic):

    def find_matching_edges(self):
        temp_graph = self.bipartite_graph.graph.copy()
        source_sink = ['source', 'sink']
        matching_edges = set()
        matched_nodes = []
        red_nodes = sorted(self.bipartite_graph.red_nodes, key=temp_graph.degree)

        while red_nodes:
            # print(red_nodes)
            print(temp_graph.)
            red_node = red_nodes.pop(0)
            print(f'degree {red_node} for:', temp_graph.degree(red_node))
            # print('red_node', red_node)
            if red_node in red_nodes or red_node in source_sink:
                continue

            blue_neighbors = list(self.bipartite_graph.graph.neighbors(red_node))
            for blue_neighbor in blue_neighbors:
                if blue_neighbor not in matching_edges:
                    edge = (red_node, blue_neighbor)
                    # print('edge', edge)
                    # print('Has edge', temp_graph.has_edge(red_node, blue_neighbor))
                    temp_graph.remove_edge(red_node, blue_neighbor)
                    print(f'degree {red_node} for:', temp_graph.degree(red_node))
                    # print('Has edge', temp_graph.has_edge(red_node, blue_neighbor))
                    matching_edges.add(edge)
                    matched_nodes.extend([red_node, blue_neighbor])
                    red_nodes = sorted(set(red_nodes), key=temp_graph.degree)
                    break

        return list(matching_edges)
