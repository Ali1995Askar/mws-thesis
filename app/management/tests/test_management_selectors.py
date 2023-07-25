import pytest
from management.selectors import ExecutionHistorySelectors


class TestExecutionHistorySelectors:
    @pytest.mark.django_db(transaction=True)
    def test_get_latest_execution_history(self, pytech_user, execution_history_1):
        data = ExecutionHistorySelectors.get_latest_execution_history(user=pytech_user)
        assert data == {
            'execution_time': 3.0,
            'graph_density': 0.6,
            'matching': 0,
            'used_heuristic_algorithm': 'STATIC MIN DEGREE'
        }
        execution_history_1.delete()
        data = ExecutionHistorySelectors.get_latest_execution_history(user=pytech_user)
        assert data == {
            'execution_time': None,
            'graph_density': None,
            'matching': None,
            'used_heuristic_algorithm': None
        }
