from typing import Dict
from networkx import Graph
from abc import ABC, abstractmethod
from src.algorithm.graph_traversal.graph_search import AbstractGraphTraversal


class MaxFlowAlgorithm(ABC):
    graph: Graph
    init_solution: Dict = None
    path_finder: AbstractGraphTraversal

    def get_graph(self):
        return self.graph

    def set_graph(self, graph: Graph):
        self.graph = graph

    def get_path_finder(self):
        return self.path_finder

    def set_path_finder(self, path_finder: AbstractGraphTraversal):
        self.path_finder = path_finder

    def set_init_solution(self, init_solution: Dict):
        self.init_solution = init_solution

    def get_init_solution(self):
        return self.init_solution

    @abstractmethod
    def find_max_flow(self, source: int, sink: int) -> tuple[int, Dict]:
        pass
