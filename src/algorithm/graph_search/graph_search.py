from typing import Dict, List
from networkx import Graph
from abc import ABC, abstractmethod


class GraphSearch(ABC):
    graph: Graph
    data_structure: List

    def __init__(self):
        self.visited: set = set()
        self.parent: Dict = {}
        self.data_structure: List = []

    def set_graph(self, graph: Graph):
        self.graph = graph

    def get_graph(self) -> Graph:
        return self.graph

    @abstractmethod
    def add_to_list(self, node):
        pass

    @abstractmethod
    def pop_from_list(self):
        pass

    def visit(self, node):
        self.visited.add(node)

    def get_neighbors(self, node):
        return self.graph[node]

    def find_path(self, source, target):
        pass

