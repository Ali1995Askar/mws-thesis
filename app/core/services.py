import time
from typing import List

from core.factories import HeuristicFactory
from src.graph.bipartite_graph import BipartiteGraph


class Services:
    @staticmethod
    def heuristics_executor(nodes_count: int, graph_density: float, algorithms: List[str]):
        bipartite_graph = BipartiteGraph()
        bipartite_graph.random_build(num_of_nodes=nodes_count, density=graph_density)
        matching_results = []
        time_results = []
        for algorithm in algorithms:
            AlgoCls = HeuristicFactory.get_algo_inst_by_name(algorithm)
            algo = AlgoCls(bipartite_graph)
            start_time = time.time()
            res = algo.execute()
            end_time = time.time()
            exec_time = round(end_time - start_time, 6)
            matching_results.append({"algoName": algorithm, "algoMatchingValue": len(res)})
            time_results.append({"algoName": algorithm, "algoRunTime": exec_time})
            print(f'{algorithm} executed successfully ...')
            
        return matching_results, time_results
