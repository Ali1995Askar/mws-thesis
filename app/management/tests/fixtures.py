from typing import List

import pytest
from management import models


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def edge_pytech_fix_tests(pytech_user, task_fix_tests, worker_ali_askar) -> models.Edge:
    edge = models.Edge.objects.create(user=pytech_user, task=task_fix_tests, worker=worker_ali_askar)
    return edge


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def edges_objects(pytech_user, pytech_user_tasks, pytech_user_workers) -> List[models.Edge]:
    edges = []
    for i in range(10):
        edge = models.Edge(
            user=pytech_user,
            task=pytech_user_tasks[i],
            worker=pytech_user_workers[i])
        edges.append(edge)

    return edges


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def heuristic_matching_1(pytech_user, task_fix_tests, worker_ali_askar) -> models.HeuristicMatching:
    heuristic_matching = models.HeuristicMatching.objects.create(
        execution_time=1.5,
        heuristic_matching=0,
        heuristic_algorithm=models.HeuristicMatching.HeuristicAlgorithm.STATIC_MIN_DEGREE.value
    )
    return heuristic_matching


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def max_matching_1(pytech_user, task_fix_tests, worker_ali_askar) -> models.MaxMatching:
    max_matching = models.MaxMatching.objects.create(
        execution_time=1.5,
        max_matching=0,
    )
    return max_matching


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def execution_history_1(pytech_user, max_matching_1, heuristic_matching_1) -> models.ExecutionHistory:
    execution_history = models.ExecutionHistory.objects.create(
        user=pytech_user,
        max_matching=max_matching_1,
        heuristic_matching=heuristic_matching_1,
        graph_density=0.6,
    )
    return execution_history
