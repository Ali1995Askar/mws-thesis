from management.factories import Factory


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
        print(request.POST)
        print('clear_assigned_tasks')

    @staticmethod
    def mark_tasks_done(request):
        print(request.POST)
        print('mark_tasks_done')

    @staticmethod
    def get_task_assigner_action_func(action: str):
        actions = {
            'build_graph': Services.build_graph,
            'execute_algorithm': Services.execute_algorithm,
            'clear_assigned_tasks': Services.clear_assigned_tasks,
            'mark_tasks_done': Services.mark_tasks_done,
        }

        return actions[action]
