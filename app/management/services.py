import time
from typing import List

from core.factories import HeuristicFactory
from src.graph.bipartite_graph import BipartiteGraph
from src.services.graph_builder import GraphBuilder
from src.services.max_matching_finder import MaxMatching
from tasks.selectors import TaskSelectors


class Services:

    @staticmethod
    def execute_algorithm(request):
        # heuristic_algorithm = request.POST['heuristic_algorithm']
        graph_builder = GraphBuilder(user=request.user)
        bipartite_graph = graph_builder.get_bipartite_graph()
        solver = MaxMatching(user=request.user, graph=bipartite_graph, heuristic_algorithm="MODIFIED_GREEDY")
        solver.execute()

    @staticmethod
    def clear_assigned_tasks(request):
        TaskSelectors.update_progress_tasks_to_open(user=request.user)

    @staticmethod
    def mark_tasks_done(request):
        TaskSelectors.update_progress_tasks_to_done(user=request.user)

    @staticmethod
    def get_task_assigner_action_func(action: str):
        actions = {
            'execute_algorithm': Services.execute_algorithm,
            'clear_assigned_tasks': Services.clear_assigned_tasks,
            'mark_tasks_done': Services.mark_tasks_done,
        }

        return actions[action]

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

        return matching_results, time_results
