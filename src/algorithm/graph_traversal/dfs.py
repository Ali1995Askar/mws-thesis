from typing import List

from src.algorithm.graph_traversal.graph_search import GraphSearch


class DFS(GraphSearch):

    def __init__(self, graph):
        super().__init__(graph)
        self.stack = []

    def add_to_list(self, node):
        self.stack.append(node)

    def pop_from_list(self):
        return self.stack.pop()
