from networkx import Graph
from collections import deque
from abc import ABC, abstractmethod
from typing import List, Union, Dict


class GraphSearch(ABC):

    def __init__(self, graph):
        self.graph = graph
        self.visited = set()
        self.parent = {}

    @abstractmethod
    def add_to_list(self, node):
        pass

    @abstractmethod
    def pop_from_list(self):
        pass

    def traverse(self, source, target=None):
        self.add_to_list(source)
        while self:
            current_node = self.pop_from_list()
            if current_node == target:
                return self.find_path(source, target)
            self.visit(current_node)
            for neighbor in self.get_neighbors(current_node):
                if neighbor not in self.visited:
                    self.add_to_list(neighbor)
                    self.parent[neighbor] = current_node
        return None

    def visit(self, node):
        self.visited.add(node)

    def get_neighbors(self, node):
        return self.graph[node]

    def find_path(self, source, target):
        path = [target]
        while path[-1] != source:
            path.append(self.parent[path[-1]])
        return list(reversed(path))
