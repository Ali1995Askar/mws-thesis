import time
import pytest
from src.services.graph_builder import GraphBuilder
from src.services.max_matching_finder import MaxMatching


class TestMaxMatchingFinder:
    @pytest.mark.django_db(transaction=True)
    def test_execute(self, pytech_user, task_fix_tests, task_send_emails, worker_omar, aws_category, worker_ahmad):
        graph_builder = GraphBuilder(user=pytech_user)
        graph = graph_builder.get_bipartite_graph()
        solver = MaxMatching(user=pytech_user, heuristic_algorithm='limit', graph=graph)
        solver.execute()

    def test_solve(self):
        pass

    def test_get_heuristic_solver(self):
        pass

    def test_update_nodes_status(self):
        pass

    def test_save_max_matching_model(self):
        pass

    def test_save_heuristic_matching_model(self):
        pass

    def test_save_execution_history(self):
        pass
