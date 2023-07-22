import pytest


class TestWorkerServices:
    @pytest.mark.django_db(transaction=True)
    def test_add_new_worker_to_bipartite_graph(self):
        pass
