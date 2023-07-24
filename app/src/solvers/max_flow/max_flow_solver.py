from networkx import Graph
from typing import Tuple, Dict, Any
from src.solvers.max_flow.ford_fulkerson import ford_fulkerson


class MaxFLowSolver:
    graph: Graph
    source: Any
    sink: Any

    def __init__(self, graph: Graph, source: Any = 'source', sink: Any = 'sink'):
        self.graph = graph
        self.source = source
        self.sink = sink

    def find_max_flow(self, initial_flow=None) -> Tuple[int, Dict]:
        kwargs = {'G': self.graph, 's': self.source, 't': self.sink}
        if initial_flow:
            kwargs.update({'residual': initial_flow})

        res = ford_fulkerson(**kwargs)
        max_flow_value = res.graph["flow_value"]
        flow_network = res.succ
        return max_flow_value, flow_network
