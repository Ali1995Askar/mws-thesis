from typing import Tuple, Dict
from app.src_2.algorithm.max_flow.core.ford_fulkerson import ford_fulkerson
from app.src_2.algorithm.max_flow.abstract_max_flow_solver import AbstractMaxFlowSolver


class FordFulkersonSolver(AbstractMaxFlowSolver):

    def find_max_flow(self, initial_solution=None) -> Tuple[float, Dict]:
        kwargs = {'G': self.graph, 's': self.source, 't': self.sink}
        if initial_solution:
            kwargs.update({'residual': initial_solution})

        res = ford_fulkerson(**kwargs)
        max_flow_value = res.graph["flow_value"]
        flow_network = res.succ
        return max_flow_value, flow_network
