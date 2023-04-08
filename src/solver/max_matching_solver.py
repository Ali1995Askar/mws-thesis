from typing import Dict
from networkx import Graph

from src.algorithm.max_flow.max_flow_algorithm import MaxFlowAlgorithm


class MaxMatchingSolver:
    def __init__(self, strategy: MaxFlowAlgorithm, ):
        self.strategy = strategy

    def find_max_matching(self, graph: Graph, init_solution: Dict):
        self.strategy.set_graph(graph=graph)
        self.strategy.set_init_solution(init_solution=init_solution)
        self.strategy.find_max_flow(source=1, sink=3)
