import json

import pytest

from categories.models import Category
from educations.models import Education
from management.selectors import ManagementSelectors
from tasks.models import Task
from workers.models import Worker


class TestManagementSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_get_latest_execution_history(self, pytech_user, execution_history_2, execution_history_1):
        data = ManagementSelectors.get_latest_execution_history(user=pytech_user)
        assert data == {
            'execution_time': 3.0,
            'graph_density': execution_history_1.graph_density,
            'matching': 0,
            'used_heuristic_algorithm': 'STATIC MIN DEGREE'
        }
        execution_history_1.delete()
        data = ManagementSelectors.get_latest_execution_history(user=pytech_user)
        assert data == {
            'execution_time': 3.0,
            'graph_density': execution_history_2.graph_density,
            'matching': 0,
            'used_heuristic_algorithm': 'STATIC MIN DEGREE'
        }
        execution_history_2.delete()

        data = ManagementSelectors.get_latest_execution_history(user=pytech_user)
        assert data == {
            'execution_time': None,
            'graph_density': None,
            'matching': None,
            'used_heuristic_algorithm': None
        }

    @pytest.mark.django_db(transaction=True)
    def test_get_last_10_execution_history_statistics(self,
                                                      pytech_user,
                                                      execution_history_1,
                                                      execution_history_2,
                                                      execution_history_3,
                                                      execution_history_4):
        data = ManagementSelectors.get_last_10_execution_history_statistics(user=pytech_user)
        rows = data['rows']

        accuracy_dict = json.loads(data['accuracy_dict'])
        time_dict = json.loads(data['time_dict'])
        assert len(rows) == 4
        assert len(accuracy_dict) == 4
        assert len(time_dict) == 4
       