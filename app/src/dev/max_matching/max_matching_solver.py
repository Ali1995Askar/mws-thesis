from networkx import DiGraph
from typing import Tuple, List, Union, Any
from src.dev.graph.bipartite_graph import BipartiteGraph
from src.algorithm.max_flow.ford_fulkerson_solver import FordFulkersonSolver
from src.dev.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class MaxMatchingSolver:

    def __init__(self):
        self.initial_flow_graph: Union[DiGraph, None] = None
        self.max_matching_value: Union[int, None] = None
        self.bipartite_graph: Union[BipartiteGraph, None] = None
        self.temp_graph: Union[BipartiteGraph, None] = None
        self.solver: Union[FordFulkersonSolver, None] = None
        self.heuristic_algorithm: Union[AbstractHeuristic, None] = None
        self.max_matching: Union[List[Tuple[Any, Any]], None] = None

    def set_bipartite_graph(self, bipartite_graph: BipartiteGraph):
        self.bipartite_graph = bipartite_graph
        self.temp_graph = self.bipartite_graph.get_graph_copy()

    def init_ford_fulkerson_solver(self):
        self.solver = FordFulkersonSolver(graph=self.temp_graph.graph)

    def set_initial_flow(self, heuristic_algorithm: Type[AbstractHeuristic]):
        self.heuristic_algorithm = heuristic_algorithm(bipartite_graph=self.bipartite_graph)
        self.initial_flow_graph = self.heuristic_algorithm.execute()

    def add_source(self):
        self.temp_graph.graph.add_node('source')

    def add_sink(self):
        self.temp_graph.graph.add_node('sink')

    def direct_bipartite_graph(self):
        edges = self.bipartite_graph.graph.edges(data=True)

        red_nodes = self.bipartite_graph.red_nodes
        blue_nodes = self.bipartite_graph.blue_nodes

        for u, v, d in edges:

            if v in red_nodes and u in blue_nodes:
                self.temp_graph.graph[u][v]['capacity'] = 0

            if u in red_nodes:
                self.temp_graph.add_edge('source', u)
                self.temp_graph.add_edge(u, 'source', capacity=0)

            if v in blue_nodes:
                self.temp_graph.add_edge(v, 'sink')
                self.temp_graph.add_edge('sink', v, capacity=0)

            if u in blue_nodes:
                self.temp_graph.add_edge(u, 'sink')
                self.temp_graph.add_edge('sink', u, capacity=0)

            if v in blue_nodes:
                self.temp_graph.add_edge(v, 'sink')
                self.temp_graph.add_edge('sink', v, capacity=0)

    def reduce_to_max_flow(self):
        if not self.bipartite_graph.is_bipartite():
            raise Exception('Graph is not Bipartite')

        self.bipartite_graph.split_nodes()

        self.temp_graph.red_nodes = self.bipartite_graph.red_nodes
        self.temp_graph.blue_nodes = self.bipartite_graph.blue_nodes

        self.add_source()
        self.add_sink()
        self.direct_bipartite_graph()

    def find_max_matching(self):
        kwargs = {}
        if self.initial_flow_graph:
            kwargs.update({'initial_solution': self.initial_flow_graph})

        _, flow_network = self.solver.find_max_flow(**kwargs)
        for k, v in flow_network.items():
            for kk, vv in v.items():
                if self.bipartite_graph.has_edge_with_positive_capacity(k, kk) and vv['flow'] == 1:
                    self.max_matching.append((k, kk))

    def print_matching_edges(self):
        print(f'Match edges:')
        for idx, edge in enumerate(self.max_matching):
            print(f'{idx + 1}: {edge[0]} --> {edge[1]}')

    def get_matching_value(self):
        return len(self.max_matching)

    def get_max_matching_edges(self):
        return self.max_matching
