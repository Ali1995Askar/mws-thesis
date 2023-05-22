from copy import deepcopy

from networkx import DiGraph
from typing import List, Tuple, Any, Union, Type
from app.utils.utils import camel_case_to_readable
from app.src_2.graph.bipartite_graph import BipartiteGraph
from app.src_2.algorithm.max_flow.abstract_max_flow_solver import AbstractMaxFlowSolver
from app.src_2.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic


class MaxMatchingSolver:
    initial_flow: Union[DiGraph, None]
    max_matching_value: Union[int, None]
    bipartite_graph: Union[BipartiteGraph, None]
    temp_graph: Union[BipartiteGraph, None]
    solver: Union[AbstractMaxFlowSolver, None]
    heuristic_algorithm: Union[AbstractHeuristic, None]
    max_matching_edges: Union[List[Tuple[Any, Any]], None]

    def __init__(self):
        self.initial_flow = None
        self.max_matching_value = None
        self.bipartite_graph = None
        self.temp_graph = None
        self.solver = None
        self.heuristic_algorithm = None
        self.max_matching_edges = None

    def set_bipartite_graph(self, bipartite_graph: BipartiteGraph):
        self.bipartite_graph = bipartite_graph
        self.temp_graph = deepcopy(self.bipartite_graph)

    def set_solver(self, solver: Type[AbstractMaxFlowSolver]):
        self.max_matching_value = 0
        self.max_matching_edges = []
        self.solver = solver(graph=self.temp_graph.graph)

    def set_initial_flow(self, heuristic_algorithm: Type[AbstractHeuristic]):
        self.heuristic_algorithm = heuristic_algorithm(bipartite_graph=self.temp_graph)
        initial_flow = self.heuristic_algorithm.execute()
        self.initial_flow = initial_flow

    def add_source(self):
        self.temp_graph.graph.add_node('source')
        # for red_node in self.temp_graph.red_nodes:
        #     self.temp_graph.add_edge('source', red_node)
        #     self.temp_graph.add_edge(red_node, 'source')

    def add_sink(self):
        self.temp_graph.graph.add_node('sink')
        # for blue_node in self.temp_graph.blue_nodes:
        #     self.temp_graph.add_edge(blue_node, 'sink')
        #     self.temp_graph.add_edge('sink', blue_node)

    def direct_bipartite_graph(self):
        edges = self.temp_graph.graph.edges(data=True)

        red_nodes = self.temp_graph.red_nodes
        blue_nodes = self.temp_graph.blue_nodes

        for u, v, d in edges:

            if v in red_nodes and u in blue_nodes:
                d['capacity'] = 0

            if u in red_nodes:
                self.temp_graph.add_edge('source', u)

            if v in blue_nodes:
                self.temp_graph.add_edge('source', v)

            if u in blue_nodes:
                self.temp_graph.add_edge(u, 'sink')

            if v in blue_nodes:
                self.temp_graph.add_edge(v, 'sink')

    def reduce_to_max_flow(self):
        if not self.bipartite_graph.is_bipartite():
            raise Exception('Graph is not Bipartite')

        self.temp_graph.split_nodes()
        self.add_source()
        self.add_sink()
        self.direct_bipartite_graph()

    def find_max_matching(self):
        kwargs = {}
        if self.initial_flow:
            kwargs.update({'initial_solution': self.initial_flow})

        _, flow_network = self.algorithm.find_max_flow(**kwargs)
        for k, v in flow_network.items():
            for kk, vv in v.items():
                if self.bipartite_graph.has_edge_with_positive_capacity(k, kk) and vv['flow'] == 1:
                    self.max_matching_edges.append((k, kk))
        self.max_matching_value = len(self.max_matching_edges)

    def print_result(self):
        algo_name = camel_case_to_readable(camel_case_string=type(self.algorithm).__name__)
        msg = f"Max Matching using '{algo_name}' is: {self.max_matching_value}"
        if self.heuristic_algorithm:
            init_match = len(self.heuristic_algorithm.matching_edges)
            msg = f"{msg} (using {type(self.heuristic_algorithm).__name__} as a heuristic with result: {init_match})"
        print(msg)

    def print_matching_edges(self):
        print(f'Match edges:')
        for idx, edge in enumerate(self.max_matching_edges):
            print(f'{idx + 1}: {edge[0]} --> {edge[1]}')
