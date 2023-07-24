from management.models import ExecutionHistory


class ExecutionHistorySelectors:
    @staticmethod
    def get_latest_execution_history(user):
        execution_history = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime').first()
        if not execution_history:
            return {
                'execution_time': None,
                'matching': None,
                'used_heuristic_algorithm': None,
                'graph_density': 0
            }
        max_matching = execution_history.max_matching
        heuristic_matching = execution_history.heuristic_matching
        execution_time = max_matching.execution_time + heuristic_matching.execution_time
        used_heuristic_algorithm = heuristic_matching.heuristic_algorithm.split("_")
        used_heuristic_algorithm = " ".join(used_heuristic_algorithm)
        return {
            'execution_time': execution_time,
            'matching': max_matching.max_matching,
            'used_heuristic_algorithm': used_heuristic_algorithm,
            'graph_density': execution_history.graph_density,
        }

    @staticmethod
    def get_last_15_execution_history(user):
        execution_histories = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime')[:15]
        if not execution_histories:
            return {}

        data = []

        for obj in execution_histories:
            used_heuristic_algorithm = obj.heuristic_matching.heuristic_algorithm.split("_")
            used_heuristic_algorithm = " ".join(used_heuristic_algorithm)
            heuristic_execution_time = round(obj.heuristic_matching.execution_time, 4)
            max_matching_execution_time = round(obj.heuristic_matching.execution_time, 4) + heuristic_execution_time
            row = {
                'graph_density': obj.graph_density,
                'used_heuristic_algorithm': used_heuristic_algorithm,
                'heuristic_matching': obj.heuristic_matching.heuristic_matching,
                'heuristic_execution_time': heuristic_execution_time,
                'max_matching': obj.max_matching.max_matching,
                'max_matching_execution_time': max_matching_execution_time,
            }
            data.append(row)
        context = {'rows': data}
        return context
