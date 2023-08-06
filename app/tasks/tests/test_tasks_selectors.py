import time

import pytest
from tasks.models import Task
from tasks.selectors import TaskSelectors
from workers.models import Worker


class TestTaskSelectors:

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

    @pytest.mark.django_db(transaction=True)
    def test_update_progress_tasks_to_open(self,
                                           pytech_user,
                                           svu_user,
                                           task_fix_tests,
                                           task_pay_salaries,
                                           task_send_emails,
                                           worker_omar,
                                           worker_ahmad,
                                           ):
        task_send_emails.user = svu_user
        task_send_emails.save()

        assert Task.objects.filter(user=pytech_user, status=Task.Status.OPEN).count() == 2
        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.FREE).count() == 2

        task_fix_tests.status = Task.Status.PROGRESS
        task_fix_tests.assigned_to = worker_ahmad

        task_pay_salaries.status = Task.Status.PROGRESS
        task_pay_salaries.assigned_to = worker_omar

        worker_omar.status = Worker.Status.OCCUPIED
        worker_ahmad.status = Worker.Status.OCCUPIED

        worker_omar.save()
        worker_ahmad.save()

        task_fix_tests.save()
        task_pay_salaries.save()

        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.OCCUPIED).count() == 2
        assert Task.objects.filter(user=pytech_user, status=Task.Status.PROGRESS).count() == 2

        TaskSelectors.update_progress_tasks_to_open(user=svu_user)
        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.OCCUPIED).count() == 2
        assert Task.objects.filter(user=pytech_user, status=Task.Status.PROGRESS).count() == 2

        assert Worker.objects.filter(user=svu_user, status=Worker.Status.OCCUPIED).count() == 0
        assert Task.objects.filter(user=svu_user, status=Task.Status.PROGRESS).count() == 0

        TaskSelectors.update_progress_tasks_to_open(user=pytech_user)
        assert Task.objects.filter(user=pytech_user, status=Task.Status.OPEN).count() == 2
        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.FREE).count() == 2

    @pytest.mark.django_db(transaction=True)
    def test_update_progress_tasks_to_done(self,
                                           pytech_user,
                                           svu_user,
                                           task_fix_tests,
                                           task_pay_salaries,
                                           task_send_emails,
                                           worker_omar,
                                           worker_ahmad,
                                           ):
        task_send_emails.user = svu_user
        task_send_emails.save()

        assert Task.objects.filter(user=pytech_user, status=Task.Status.OPEN).count() == 2
        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.FREE).count() == 2

        task_fix_tests.status = Task.Status.PROGRESS
        task_fix_tests.assigned_to = worker_ahmad

        task_pay_salaries.status = Task.Status.PROGRESS
        task_pay_salaries.assigned_to = worker_omar

        worker_omar.status = Worker.Status.OCCUPIED
        worker_ahmad.status = Worker.Status.OCCUPIED

        worker_omar.save()
        worker_ahmad.save()

        task_fix_tests.save()
        task_pay_salaries.save()

        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.OCCUPIED).count() == 2
        assert Task.objects.filter(user=pytech_user, status=Task.Status.PROGRESS).count() == 2

        TaskSelectors.update_progress_tasks_to_done(user=svu_user)
        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.OCCUPIED).count() == 2
        assert Task.objects.filter(user=pytech_user, status=Task.Status.PROGRESS).count() == 2

        assert Worker.objects.filter(user=svu_user, status=Worker.Status.OCCUPIED).count() == 0
        assert Task.objects.filter(user=svu_user, status=Task.Status.PROGRESS).count() == 0

        TaskSelectors.update_progress_tasks_to_done(user=pytech_user)
        assert Task.objects.filter(user=pytech_user, status=Task.Status.DONE).count() == 2
        assert Worker.objects.filter(user=pytech_user, status=Worker.Status.FREE).count() == 2

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

        connected_workers = TaskSelectors.get_connected_workers(task=task_fix_tests)
        worker_omar.categories.add(aws_category)
        assert connected_workers.count() == 2

    @pytest.mark.skip
    @pytest.mark.django_db(transaction=True)
    def test_get_tasks_with_connected_workers(self,
                                              pytech_user,
                                              task_fix_tests,
                                              task_pay_salaries,
                                              asp_category,
                                              aws_category,
                                              it_education,
                                              worker_omar,
                                              worker_ahmad):
        data = TaskSelectors.get_tasks_with_connected_workers(user=pytech_user)
        for k, v in data.items():
            assert k in [task_fix_tests, task_pay_salaries]
            assert v.count() == 2

        worker_omar.education = it_education
        worker_omar.save()
        data = TaskSelectors.get_tasks_with_connected_workers(user=pytech_user)
        for k, v in data.items():
            assert k in [task_fix_tests, task_pay_salaries]
            assert v.count() == 2

        task_fix_tests.categories.add(asp_category)
        data = TaskSelectors.get_tasks_with_connected_workers(user=pytech_user)

        workers = data[task_fix_tests]
        assert workers.count() == 0

        workers = data[task_pay_salaries]
        assert workers.count() == 2

        worker_omar.categories.add(asp_category)
        data = TaskSelectors.get_tasks_with_connected_workers(user=pytech_user)
        workers = data[task_fix_tests]
        assert workers.count() == 1

        workers = data[task_pay_salaries]
        assert workers.count() == 2

        worker_ahmad.categories.add(asp_category)
        data = TaskSelectors.get_tasks_with_connected_workers(user=pytech_user)
        workers = data[task_fix_tests]
        assert workers.count() == 2

        workers = data[task_pay_salaries]
        assert workers.count() == 2

        worker_omar.status = Worker.Status.OCCUPIED
        worker_omar.save()
        data = TaskSelectors.get_tasks_with_connected_workers(user=pytech_user)
        workers = data[task_fix_tests]
        assert workers.count() == 1

        workers = data[task_pay_salaries]
        assert workers.count() == 1

    @pytest.mark.django_db(transaction=True)
    def test_load(self, pytech_user, pytech_user_tasks, pytech_user_workers):
        s = time.time()
        data = TaskSelectors.get_tasks_with_connected_workers(user=pytech_user)
        e = time.time()
        print(e - s)
        assert data
