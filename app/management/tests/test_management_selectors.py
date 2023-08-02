import pytest

from categories.models import Category
from educations.models import Education
from management.selectors import ExecutionHistorySelectors
from tasks.models import Task
from workers.models import Worker


class TestExecutionHistorySelectors:
    @pytest.mark.django_db(transaction=True)
    def test_get_latest_execution_history(self, pytech_user, execution_history_1):
        data = ExecutionHistorySelectors.get_latest_execution_history(user=pytech_user)
        assert data == {
            'execution_time': 3.0,
            'graph_density': 0.6,
            'matching': 0,
            'used_heuristic_algorithm': 'STATIC MIN DEGREE'
        }
        execution_history_1.delete()
        data = ExecutionHistorySelectors.get_latest_execution_history(user=pytech_user)
        assert data == {
            'execution_time': None,
            'graph_density': None,
            'matching': None,
            'used_heuristic_algorithm': None
        }

    @pytest.mark.django_db(transaction=True)
    def test_get_last_10_execution_history_statistics(self):
        pass

    @pytest.mark.django_db(transaction=True)
    def test_build_graph(self, pytech_user):
        tasks = Task.objects.filter(user=pytech_user)
        workers = Worker.objects.filter(user=pytech_user)
        categories = Category.objects.filter(user=pytech_user)
        educations = Education.objects.filter(user=pytech_user)

        assert tasks.count() == 0
        assert workers.count() == 0
        assert categories.count() == 0
        assert educations.count() == 0

        ExecutionHistorySelectors.build_graph(nodes=10, density=0.1, username=pytech_user.username)

        assert tasks.count() == 5
        assert workers.count() == 5
        assert categories.count() == 2
        assert educations.count() == 2
      
        for task in tasks:
            print(task.categories.all())
            print(task.educations.all())
            print('===========================================')
        print('***********************************************************************************************')

        for worker in workers:
            print(worker.categories.all())
            print(worker.education)
            print('===========================================')

        print(workers.count() * tasks.count())
