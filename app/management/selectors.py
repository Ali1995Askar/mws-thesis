import json

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
                'graph_density': None
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
    def get_last_15_execution_history_statistics(user):
        execution_histories = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime')[:15]
        if not execution_histories:
            return {}

        data = []
        accuracy_data = []
        execution_time_data = []
        for obj in execution_histories:
            used_heuristic_algorithm = obj.heuristic_matching.heuristic_algorithm.split("_")
            used_heuristic_algorithm = " ".join(used_heuristic_algorithm)
            heuristic_execution_time = round(obj.heuristic_matching.execution_time, 4)
            max_matching_execution_time = round(obj.heuristic_matching.execution_time, 4) + heuristic_execution_time

            heuristic_matching = obj.heuristic_matching.heuristic_matching
            max_matching = obj.max_matching.max_matching

            graph_density = obj.graph_density
            row = {
                'graph_density': graph_density,
                'used_heuristic_algorithm': used_heuristic_algorithm,
                'heuristic_matching': heuristic_matching,
                'heuristic_execution_time': heuristic_execution_time,
                'max_matching': max_matching,
                'max_matching_execution_time': max_matching_execution_time,
            }
            data.append(row)

            accuracy_dict = {
                'heuristic_matching': heuristic_matching,
                'max_matching': max_matching,
                'graph_density': graph_density
            }
            time_dict = {
                'heuristic_matching': heuristic_execution_time,
                'max_matching': max_matching_execution_time,
                'graph_density': graph_density
            }

            accuracy_data.append(accuracy_dict)
            execution_time_data.append(time_dict)
        context = {
            'rows': data,
            'accuracy_dict': json.dumps(accuracy_data),
            'time_dict': json.dumps(execution_time_data),

        }
        return context

    @staticmethod
    def build_random_graph_by_density(density: float, username: str = 'admin'):
        pass
