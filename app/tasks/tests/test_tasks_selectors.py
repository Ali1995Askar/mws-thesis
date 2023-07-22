import pytest

from tasks.selectors import TaskSelectors


class TestTaskSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_delete_related_task_edges(self, task_fix_tests):
        TaskSelectors.delete_related_task_edges(task=task_fix_tests)

    @pytest.mark.django_db(transaction=True)
    def test_get_connected_workers(self):
        pass

    @pytest.mark.django_db(transaction=True)
    def test_get_tasks_count_by_status(self):
        pass
