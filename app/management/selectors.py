from management.models import ExecutionHistory


class ExecutionHistorySelectors:
    @staticmethod
    def get_latest_execution_history(user):
        execution_history = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime').first()
        if not execution_history:
            return {
                'execution_time': None,
                'matching': None,
                'used_heuristic_algorithm': None
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
            'graph_density': 2,
        }
