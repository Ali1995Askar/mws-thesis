from tasks.selectors import TaskSelectors
from src.services.graph_builder import GraphBuilder
from src.services.max_matching_finder import MaxMatching


class Services:

    @staticmethod
    def execute_algorithm(request):
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
