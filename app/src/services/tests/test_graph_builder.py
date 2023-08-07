import pytest
from src.services.graph_builder import GraphBuilder
from src.graph.bipartite_graph import BipartiteGraph


class TestGraphBuilder:
    @pytest.fixture()
    @pytest.mark.django_db(transaction=True)
    def graph_builder(self, pytech_user):
        inst = GraphBuilder(user=pytech_user)
        return inst

    @pytest.mark.django_db(transaction=True)
    def test_build_and_get_bipartite_graph(self, graph_builder, mocker):
        def fill_edges_and_nodes():
            graph_builder.nodes = [1, 2, 3, 4, 5, 6, 6]
            graph_builder.edges = [(1, 4), (2, 5), (3, 6)]

        mocker.patch('src.services.graph_builder.GraphBuilder.set_nodes_and_edges', side_effect=fill_edges_and_nodes)

        graph = graph_builder.get_bipartite_graph()
        assert isinstance(graph, BipartiteGraph)
        assert all(edge in [(1, 4), (2, 5), (3, 6), (4, 1), (5, 2), (6, 3)] for edge in graph.edges())
        assert all(node in [1, 2, 3, 4, 5, 6] for node in graph.nodes())

    @pytest.mark.django_db(transaction=True)
    def test_set_nodes_and_edges(self,
                                 graph_builder,
                                 task_fix_tests,
                                 task_pay_salaries,
                                 task_send_emails,
                                 worker_omar,
                                 worker_ahmad,
                                 worker_ali_askar,
                                 mocker):
        mocker.patch(
            'tasks.selectors.TaskSelectors.get_tasks_with_connected_workers',
            return_value={
                task_fix_tests: [worker_ali_askar.id],
                task_pay_salaries: [worker_omar.id],
                task_send_emails: [worker_ahmad.id],
            })
        graph_builder.set_nodes_and_edges()

        assert set(graph_builder.nodes) == {f'task-{task_fix_tests.id}',
                                            f'worker-{worker_ali_askar.id}',
                                            f'task-{task_pay_salaries.id}',
                                            f'worker-{worker_omar.id}',
                                            f'task-{task_send_emails.id}',
                                            f'worker-{worker_ahmad.id}'}
        assert all(
            edge in [
                (f'worker-{worker_ali_askar.id}', f'task-{task_fix_tests.id}'),
                (f'worker-{worker_omar.id}', f'task-{task_pay_salaries.id}'),
                (f'worker-{worker_ahmad.id}', f'task-{task_send_emails.id}')
            ]
            for edge in graph_builder.edges
        )
        assert len(graph_builder.edges) == len(
            [
                (f'worker-{worker_ali_askar.id}', f'task-{task_fix_tests.id}'),
                (f'worker-{worker_omar.id}', f'task-{task_pay_salaries.id}'),
                (f'worker-{worker_ahmad.id}', f'task-{task_send_emails.id}')
            ]
        )
