from copy import deepcopy
from typing import Type, List, Tuple, Any, Union

from networkx import DiGraph

from app.src.algorithm.max_matching.heuristics.abstract_heuristic import AbstractHeuristic
from app.utils.utils import camel_case_to_readable
from app.src.graph.bipartite_graph import BipartiteGraph
from app.src.algorithm.max_flow.max_flow_algorithm import MaxFlowAlgorithm


class MaxMatching:
    max_matching_value: Union[int, None]
    algorithm: Union[MaxFlowAlgorithm, None]
    bipartite_graph: Union[BipartiteGraph, None]
    temp_bipartite_graph: Union[BipartiteGraph, None]
    max_matching_edges: Union[List[Tuple[Any, Any]], None]
    initial_flow: Union[DiGraph, None]
    heuristic_algorithm: Union[AbstractHeuristic, None]

    def __init__(self):
        self.initial_flow = None
        self.heuristic_algorithm = None

    def reset(self):
        self.initial_flow = None
        self.heuristic_algorithm = None
        self.max_matching_value = None
        self.algorithm = None
        self.temp_bipartite_graph = deepcopy(self.bipartite_graph)
        self.max_matching_edges = None
        self.max_matching_edges = None

    def get_temp_graph(self):
        return self.temp_bipartite_graph.graph

    def reduce_to_max_flow(self):
        if not self.bipartite_graph.is_bipartite():
            raise Exception('Graph is not Bipartite')
        self.temp_bipartite_graph.split_nodes()
        self.add_source()
        self.add_sink()
        self.direct_graph()

    def set_bipartite_graph(self, bipartite_graph: BipartiteGraph):
        self.bipartite_graph = bipartite_graph
        self.temp_bipartite_graph = deepcopy(self.bipartite_graph)

    def set_initial_flow(self, heuristic_algorithm: Type[AbstractHeuristic]):
        self.heuristic_algorithm = heuristic_algorithm(bipartite_graph=self.temp_bipartite_graph)
        initial_flow = self.heuristic_algorithm.execute()
        self.initial_flow = initial_flow

    def set_algorithm(self, algorithm: Type[MaxFlowAlgorithm]):
        self.max_matching_value = 0
        self.max_matching_edges = []
        self.temp_bipartite_graph = deepcopy(self.bipartite_graph)
        self.algorithm = algorithm(graph=self.temp_bipartite_graph.graph)

    def add_source(self):
        self.temp_bipartite_graph.graph.add_node('source')
        for node in self.temp_bipartite_graph.red_nodes:
            self.temp_bipartite_graph.add_edge('source', node)
            self.temp_bipartite_graph.add_edge(node, 'source')

    def add_sink(self):
        self.temp_bipartite_graph.graph.add_node('sink')
        for node in self.temp_bipartite_graph.blue_nodes:
            self.temp_bipartite_graph.add_edge(node, 'sink')
            self.temp_bipartite_graph.add_edge('sink', node)

    def direct_graph(self):
        edges = self.temp_bipartite_graph.graph.edges(data=True)
        for u, v, d in edges:

            if v in self.temp_bipartite_graph.red_nodes and u in self.temp_bipartite_graph.blue_nodes:
                d['capacity'] = 0

            if u == 'sink':
                d['capacity'] = 0

            if v == 'source':
                d['capacity'] = 0

    def find_max_matching(self):
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
