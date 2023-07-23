import pytest
from tasks.models import Task
from tasks.selectors import TaskSelectors


class TestTaskSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_delete_related_task_edges(self, task_fix_tests):
        TaskSelectors.delete_related_task_edges(task=task_fix_tests)

    @pytest.mark.django_db(transaction=True)
    def test_get_connected_workers(self,
                                   task_fix_tests,
                                   asp_category,
                                   aws_category,
                                   it_education,
                                   worker_omar,
                                   worker_ahmad):
        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.count() == 2
        worker_omar.education = it_education
        worker_omar.save()
        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.count() == 2

        worker_omar.categories.add(asp_category)
        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.count() == 2

        task_fix_tests.categories.add(asp_category)
        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.first() == worker_omar

        task_fix_tests.educations.add(it_education)
        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.first() == worker_omar

        task_fix_tests.categories.add(aws_category)
        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.count() == 0

        worker_ahmad.categories.add(asp_category, aws_category)
        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.count() == 0

        worker_ahmad.education = it_education
        worker_ahmad.save()

        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        assert connected_workers.first() == worker_ahmad

        worker_omar.categories.add(aws_category)
        assert connected_workers.count() == 2

    @pytest.mark.django_db(transaction=True)
    def test_get_tasks_count_by_status(self,
                                       pytech_user,
                                       svu_user,
                                       task_fix_tests,
                                       task_pay_salaries,
                                       task_send_emails):
        data = TaskSelectors.get_tasks_count_by_status(user=pytech_user)
        assert data == {'OPEN': 3, 'DONE': 0, 'PROGRESS': 0}
        task_fix_tests.status = Task.Status.DONE.value
        task_fix_tests.save()
        data = TaskSelectors.get_tasks_count_by_status(user=pytech_user)
        assert data == {'DONE': 1, 'OPEN': 2, 'PROGRESS': 0}
        task_pay_salaries.status = Task.Status.PROGRESS.value
        task_pay_salaries.save()
        data = TaskSelectors.get_tasks_count_by_status(user=pytech_user)
        assert data == {'DONE': 1, 'OPEN': 1, 'PROGRESS': 1}
        task_send_emails.status = Task.Status.PROGRESS.value
        task_send_emails.save()
        data = TaskSelectors.get_tasks_count_by_status(user=pytech_user)
        assert data == {'DONE': 1, 'PROGRESS': 2, 'OPEN': 0}
        task_fix_tests.user = svu_user
        task_fix_tests.save()
        data = TaskSelectors.get_tasks_count_by_status(user=pytech_user)
        assert data == {'PROGRESS': 2, 'OPEN': 0, 'DONE': 0}
        data = TaskSelectors.get_tasks_count_by_status(user=svu_user)
        assert data == {'DONE': 1, 'OPEN': 0, 'PROGRESS': 0}
