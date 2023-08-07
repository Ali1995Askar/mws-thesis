import json
import pytest
from management.selectors import ManagementSelectors


class TestManagementSelectors:

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
