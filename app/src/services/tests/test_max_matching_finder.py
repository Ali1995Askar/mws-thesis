import pytest
from src.services.max_matching_finder import MaxMatching
from tasks.models import Task
from tasks.selectors import TaskSelectors


class TestMaxMatchingFinder:
    @pytest.mark.django_db(transaction=True)
    def test_execute(self, pytech_user, task_fix_tests, task_send_emails, worker_omar, aws_category, worker_ahmad):
        task_fix_tests.categories.add(aws_category)
        print(worker_omar.status)
        print(worker_ahmad.status)
        print(task_fix_tests.status)
        print(task_send_emails.status)
        print(task_fix_tests.assigned_to)
        print(task_send_emails.assigned_to)
        print(worker_omar.task_set.all())
        print(worker_ahmad.task_set.all())
        solver = MaxMatching(user=pytech_user, heuristic_algorithm='limit_min_degree')
        solver.execute()
        print('==================================')
        worker_omar.refresh_from_db()
        worker_ahmad.refresh_from_db()
        task_fix_tests.refresh_from_db()
        task_send_emails.refresh_from_db()
        print(worker_omar.status)

        print(worker_ahmad.status)
        print(task_fix_tests.status)
        print(task_send_emails.status)
        print(task_fix_tests.assigned_to)
        print(task_send_emails.assigned_to)
        print(worker_omar.task_set.all())
        print(worker_ahmad.task_set.all())
        # res = TaskSelectors.get_connected_workers_for_all_tasks()
        # print(res)

    @pytest.mark.django_db(transaction=True)
    def test_execute_2(self, pytech_user, pytech_user_tasks, pytech_user_workers):
        print(Task.objects.all().values('status'))
        solver = MaxMatching(user=pytech_user, heuristic_algorithm='limit_min_degree')
        solver.execute()
        print(Task.objects.all().values('status'))
