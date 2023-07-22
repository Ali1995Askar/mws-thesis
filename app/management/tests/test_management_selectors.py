import pytest
from management.models import Edge
from management.selectors import BipartiteGraphSelectors


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
        assert data == {'graph_density': 0.11, 'max_degree': 3, 'min_degree': 1}


class TestEdgeSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_build_edges_for_task(self):
        pass

    @pytest.mark.django_db(transaction=True)
    def test_build_edges_for_worker(self):
        pass


class TestExecutionHistorySelectors:
    @pytest.mark.django_db(transaction=True)
    def test_get_latest_execution_history(self):
        pass
