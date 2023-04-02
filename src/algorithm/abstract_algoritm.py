from abc import abstractmethod


class AbstractAlgorithm:
    def __int__(self, graph):
        self.graph = graph

    @abstractmethod
    def execute(self):
        pass
