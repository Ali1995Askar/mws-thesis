from networkx import DiGraph
from typing import List, Tuple, Any, Union

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic
from app.src_2.algorithm.max_flow.abstract_max_flow_solver import AbstractMaxFlowSolver
from app.src_2.graph.bipartite_graph import BipartiteGraph
from app.utils.utils import camel_case_to_readable


class MaxMatchingSolver:
    max_matching_value: Union[int, None]
    algorithm: Union[AbstractMaxFlowSolver, None]
    bipartite_graph: Union[BipartiteGraph, None]
    max_matching_edges: Union[List[Tuple[Any, Any]], None]
    initial_flow: Union[DiGraph, None]
    heuristic_algorithm: Union[AbstractHeuristic, None]

    def __init__(self):
        self.initial_flow = None
        self.heuristic_algorithm = None

    def add_source(self):
        self.bipartite_graph.graph.add_node('source')
        for red_node in self.bipartite_graph.red_nodes:
            self.bipartite_graph.add_edge('source', red_node)

    def add_sink(self):
        self.bipartite_graph.graph.add_node('sink')
        for blue_node in self.bipartite_graph.blue_nodes:
            self.bipartite_graph.add_edge(blue_node, 'sink')

    def direct_bipartite_graph(self):
        for u, v, d in self.bipartite_graph.edges():
            self.bipartite_graph.has_edge_with_positive_capacity(v, u)
            self.bipartite_graph.graph.remove_edge(v, u)

    def reduce_to_max_flow(self):
        if not self.bipartite_graph.is_bipartite():
            raise Exception('Graph is not Bipartite')
        self.bipartite_graph.split_nodes()
        self.direct_bipartite_graph()
        self.add_source()
        self.add_sink()

    def solve(self):
        kwargs = {}
        if self.initial_flow:
            kwargs.update({'initial_solution': self.initial_flow})

        _, flow_network = self.algorithm.find_max_flow(**kwargs)

        for k, v in flow_network.items():
            for kk, vv in v.items():
                if self.bipartite_graph.graph.has_edge(k, kk) and vv['flow'] == 1:
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
