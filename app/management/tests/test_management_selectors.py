import pytest
from management.models import Edge
from management.selectors import BipartiteGraphSelectors, EdgeSelectors, ExecutionHistorySelectors
from tasks.models import Task
from workers.models import Worker


class TestBipartiteGraphSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_bulk_add_edges(self, pytech_user, svu_user, edges_objects):
        assert Edge.objects.all().count() == 0
        assert pytech_user.bipartitegraph.edges.all().count() == 0

        BipartiteGraphSelectors.bulk_edges_create(user=pytech_user, edges=edges_objects)

        assert Edge.objects.all().count() == len(edges_objects)
        assert pytech_user.bipartitegraph.edges.all().count() == len(edges_objects)

    @pytest.mark.django_db(transaction=True)
    def test_get_latest_graph_data(self, pytech_user, edges_objects):
        data = BipartiteGraphSelectors.get_latest_graph_data(user=pytech_user)
        assert data == {'graph_density': 0.0, 'max_degree': 0, 'min_degree': 0}
        BipartiteGraphSelectors.bulk_edges_create(user=pytech_user, edges=edges_objects)
        data = BipartiteGraphSelectors.get_latest_graph_data(user=pytech_user)
        assert data == {'graph_density': 0.1, 'max_degree': 1, 'min_degree': 1}

        edges = pytech_user.bipartitegraph.edges.all()
        Edge.objects.create(user=pytech_user, task=edges.first().task, worker=edges.last().worker)

        BipartiteGraphSelectors.bulk_edges_create(user=pytech_user, edges=edges_objects)
        data = BipartiteGraphSelectors.get_latest_graph_data(user=pytech_user)
        assert data == {'graph_density': 0.11, 'max_degree': 2, 'min_degree': 1}

        Edge.objects.create(user=pytech_user, task=edges[1].task, worker=edges.last().worker)
        BipartiteGraphSelectors.bulk_edges_create(user=pytech_user, edges=edges_objects)
        data = BipartiteGraphSelectors.get_latest_graph_data(user=pytech_user)
        assert data == {'graph_density': 0.12, 'max_degree': 3, 'min_degree': 1}


class TestEdgeSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_build_edges_for_task(self, pytech_user, task_fix_tests, worker_ali_askar, worker_omar):
        connected_workers = Worker.objects.all()
        edges = EdgeSelectors.build_edges_for_task(task=task_fix_tests, connected_workers=connected_workers)
        assert len(edges) == len(connected_workers)
        assert all(isinstance(edge, Edge) for edge in edges)
        assert all(edge.user == pytech_user for edge in edges)
        assert Edge.objects.all().count() == 0

    @pytest.mark.django_db(transaction=True)
    def test_build_edges_for_worker(self, pytech_user, worker_ali_askar, task_fix_tests, task_pay_salaries):
        connected_tasks = Task.objects.all()
        edges = EdgeSelectors.build_edges_for_worker(worker=worker_ali_askar, connected_tasks=connected_tasks)
        assert len(edges) == len(connected_tasks)
        assert all(isinstance(edge, Edge) for edge in edges)
        assert all(edge.user == pytech_user for edge in edges)


class TestExecutionHistorySelectors:
    @pytest.mark.django_db(transaction=True)
    def test_get_latest_execution_history(self, pytech_user, execution_history_1):
        data = ExecutionHistorySelectors.get_latest_execution_history(user=pytech_user)
        assert data == {'execution_time': 3.0, 'matching': 0, 'used_heuristic_algorithm': 'STATIC_MIN_DEGREE'}
        execution_history_1.delete()
        data = ExecutionHistorySelectors.get_latest_execution_history(user=pytech_user)
        assert data == {'execution_time': None, 'matching': None, 'used_heuristic_algorithm': None}
