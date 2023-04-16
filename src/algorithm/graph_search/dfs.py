from src.algorithm.graph_search.graph_search import GraphSearch


class DFS(GraphSearch):

    def __init__(self):
        super().__init__()

    def add_to_list(self, node):
        self.data_structure.append(node)

    def pop_from_list(self):
        return self.data_structure.pop()
