import time
import pytest
from src.services.graph_builder import GraphBuilder
from src.services.max_matching_finder import MaxMatching


class TestMaxMatchingFinder:
    @pytest.mark.django_db(transaction=True)
    def test_execute(self, pytech_user, task_fix_tests, task_send_emails, worker_omar, aws_category, worker_ahmad):
        graph_builder = GraphBuilder(user=pytech_user)
        graph = graph_builder.get_bipartite_graph()
        solver = MaxMatching(user=pytech_user, heuristic_algorithm='limit_min_degree', graph=graph)
        solver.execute()
        print(solver.max_matching_solver.get_max_matching_edges())

    @pytest.mark.django_db(transaction=True)
    def test_execute_2(self, pytech_user, aws_category, pytech_user_workers, pytech_user_tasks):
        start = time.time()
        graph_builder = GraphBuilder(user=pytech_user)
        graph = graph_builder.get_bipartite_graph()
        end = time.time()
        print(end - start)
        start = time.time()
        solver = MaxMatching(user=pytech_user, heuristic_algorithm='static_min_degree', graph=graph)
        solver.execute()
        end = time.time()
        print(solver.max_matching_solver.get_matching_value())
