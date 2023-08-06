from typing import List

import pytest
from management import models


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def heuristic_matching_1(pytech_user, task_fix_tests, worker_ali_askar) -> models.HeuristicMatching:
    heuristic_matching = models.HeuristicMatching.objects.create(
        user=pytech_user,
        execution_time=1.5,
        heuristic_matching=0,
        heuristic_algorithm=models.HeuristicMatching.HeuristicAlgorithm.STATIC_MIN_DEGREE.value
    )
    return heuristic_matching


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def heuristic_matching_2(pytech_user, task_fix_tests, worker_ali_askar) -> models.HeuristicMatching:
    heuristic_matching = models.HeuristicMatching.objects.create(
        user=pytech_user,
        execution_time=1.5,
        heuristic_matching=5,
        heuristic_algorithm=models.HeuristicMatching.HeuristicAlgorithm.DYNAMIC_MIN_DEGREE.value
    )
    return heuristic_matching


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def max_matching_1(pytech_user, task_fix_tests, worker_ali_askar) -> models.MaxMatching:
    max_matching = models.MaxMatching.objects.create(
        user=pytech_user,
        execution_time=1.5,
        max_matching=0,
    )
    return max_matching


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def max_matching_2(pytech_user, task_fix_tests, worker_ali_askar) -> models.MaxMatching:
    max_matching = models.MaxMatching.objects.create(
        user=pytech_user,
        execution_time=1.5,
        max_matching=6,
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


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def execution_history_2(pytech_user, max_matching_1, heuristic_matching_1) -> models.ExecutionHistory:
    execution_history = models.ExecutionHistory.objects.create(
        user=pytech_user,
        max_matching=max_matching_1,
        heuristic_matching=heuristic_matching_1,
        graph_density=0.3,
    )
    return execution_history


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def execution_history_3(pytech_user, max_matching_2, heuristic_matching_2) -> models.ExecutionHistory:
    execution_history = models.ExecutionHistory.objects.create(
        user=pytech_user,
        max_matching=max_matching_2,
        heuristic_matching=heuristic_matching_2,
        graph_density=0.1,
    )
    return execution_history


@pytest.fixture()
@pytest.mark.django_db(transaction=True)
def execution_history_4(pytech_user, max_matching_2, heuristic_matching_2) -> models.ExecutionHistory:
    execution_history = models.ExecutionHistory.objects.create(
        user=pytech_user,
        max_matching=max_matching_2,
        heuristic_matching=heuristic_matching_2,
        graph_density=0.8,
    )
    return execution_history
