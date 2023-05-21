from networkx import Graph
from typing import Tuple, Dict, Any
from abc import ABC, abstractmethod


class AbstractMaxFlowSolver(ABC):
    graph: Graph
    source: Any
    sink: Any

    def __init__(self, graph: Graph, source: Any = 'source', sink: Any = 'sink'):
        self.graph = graph
        self.source = source
        self.sink = sink

    @abstractmethod
    def find_max_flow(self, initial_solution=None) -> Tuple[int, Dict]:
        pass
