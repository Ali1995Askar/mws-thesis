from typing import Tuple, Dict

from src.algorithm.max_flow.core.edmonds_karp import edmonds_karp
# from networkx.algorithms.flow import edmonds_karp
from src.algorithm.max_flow.max_flow_algorithm import MaxFlowAlgorithm
import networkx as nx


#


class EdmondsKarpAlgorithm(MaxFlowAlgorithm):
    def find_max_flow(self, initial_solution=None) -> Tuple[float, Dict]:
        kwargs = {'G': self.graph, 's': self.source, 't': self.sink}
        if initial_solution:
            kwargs.update({'residual': initial_solution})

        res = edmonds_karp(**kwargs)
        max_flow_value = res.graph["flow_value"]
        flow_network = res.succ
        return max_flow_value, flow_network
