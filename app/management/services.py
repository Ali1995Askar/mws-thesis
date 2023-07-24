from management.factories import Factory
from tasks.selectors import TaskSelectors


class Services:

    @staticmethod
    def build_graph(request):
        print(request.POST)
        print('build_graph')

    @staticmethod
    def execute_algorithm(request):
        heuristic_algorithm = request.POST['heuristic_algorithm']
        heuristic_inst = Factory.get_algorithms(heuristic_algorithm)
        print(heuristic_inst)
        print(heuristic_algorithm)

    @staticmethod
    def clear_assigned_tasks(request):
        TaskSelectors.update_progress_tasks_to_open(user=request.user)

    @staticmethod
    def mark_tasks_done(request):
        TaskSelectors.update_progress_tasks_to_done(user=request.user)

    @staticmethod
    def get_task_assigner_action_func(action: str):
        actions = {
            'build_graph': Services.build_graph,
            'execute_algorithm': Services.execute_algorithm,
            'clear_assigned_tasks': Services.clear_assigned_tasks,
            'mark_tasks_done': Services.mark_tasks_done,
        }

        return actions[action]
