from collections import deque

from src.algorithm.graph_traversal.graph_search import GraphSearch


class BFS(GraphSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.queue = []

    def add_to_list(self, node):
        self.queue.append(node)

    def pop_from_list(self):
        return self.queue.pop(0)
