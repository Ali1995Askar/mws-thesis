import pytest

from workers.selectors import WorkerSelectors


class TestWorkerSelectors:
    @pytest.mark.django_db(transaction=True)
    def test_delete_related_worker_edges(self, worker_omar):
        WorkerSelectors.delete_related_worker_edges(worker=worker_omar)

    @pytest.mark.django_db(transaction=True)
    def test_get_connected_tasks(self,
                                 task_fix_tests,
                                 task_pay_salaries,
                                 task_send_emails,
                                 asp_category,
                                 aws_category,
                                 java_category,
                                 it_education,
                                 software_education,
                                 worker_omar,
                                 worker_ahmad):
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_omar)
        assert connected_tasks.count() == 3

        worker_omar.education = it_education
        worker_omar.save()

        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_omar)
        assert connected_tasks.count() == 3

        task_send_emails.educations.add(software_education)

        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_omar)
        assert connected_tasks.count() == 2

        worker_omar.education = software_education
        worker_omar.save()
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_omar)
        assert connected_tasks.count() == 3

        task_pay_salaries.educations.add(it_education)
        task_fix_tests.educations.add(it_education)
        assert connected_tasks.first() == task_send_emails

        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_ahmad)
        assert connected_tasks.count() == 0

        worker_ahmad.education = it_education
        worker_ahmad.save()

        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_ahmad)
        assert connected_tasks.count() == 2

        worker_ahmad.categories.add(asp_category, aws_category)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_ahmad)
        assert connected_tasks.count() == 2

        task_pay_salaries.categories.add(java_category)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_ahmad)
        assert connected_tasks.count() == 1

        task_fix_tests.categories.add(java_category)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_ahmad)
        assert connected_tasks.count() == 0

        worker_ahmad.categories.add(java_category)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_ahmad)
        assert connected_tasks.count() == 2

        task_send_emails.educations.add(it_education)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_ahmad)
        assert connected_tasks.count() == 3

        task_send_emails.categories.add(java_category)
        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_omar)
        assert connected_tasks.count() == 0

        worker_omar.categories.add(java_category)

        connected_tasks = WorkerSelectors.get_connected_tasks(worker=worker_omar)
        assert connected_tasks.count() == 1

    @pytest.mark.django_db(transaction=True)
    def test_get_workers_count_by_status(self):
        pass
