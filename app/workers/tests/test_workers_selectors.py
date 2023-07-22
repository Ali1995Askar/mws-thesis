import pytest


class TestWorkerSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_delete_related_worker_edges(self):
        pass

    @pytest.mark.django_db(transaction=True)
    def test_get_connected_tasks(self):
        pass

    @pytest.mark.django_db(transaction=True)
    def test_get_workers_count_by_status(self):
        pass
