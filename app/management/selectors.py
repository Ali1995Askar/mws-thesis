import json
import math
import random

from tasks.models import Task
from workers.models import Worker
from categories.models import Category
from educations.models import Education
from django.db.models.functions import Concat
from management.models import ExecutionHistory
from django.contrib.auth.models import User
from django.db.models import Count, F, Value


class ManagementSelectors:

    @staticmethod
    def get_latest_execution_history(user):
        execution_history = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime').first()
        if not execution_history:
            return {
                'execution_time': None,
                'matching': None,
                'used_heuristic_algorithm': None,
                'graph_density': None
            }
        max_matching = execution_history.max_matching
        execution_time = max_matching.execution_time
        heuristic_matching = execution_history.heuristic_matching

        return {
            'execution_time': execution_time,
            'matching': max_matching.max_matching,
            'graph_density': execution_history.graph_density,
        }

    @staticmethod
    def get_last_10_execution_history_statistics(user):
        execution_histories = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime')[:10]
        if not execution_histories:
            return {}

        data = []
        accuracy_data = []
        execution_time_data = []
        for obj in execution_histories:
            heuristic_execution_time = obj.heuristic_matching.execution_time
            max_matching_execution_time = obj.max_matching.execution_time

            heuristic_matching = obj.heuristic_matching.heuristic_matching
            max_matching = obj.max_matching.max_matching

            graph_density = obj.graph_density
            row = {
                'graph_density': graph_density,
                'heuristic_matching': heuristic_matching,
                'heuristic_execution_time': heuristic_execution_time,
                'max_matching': max_matching,
                'max_matching_execution_time': max_matching_execution_time,
            }
            data.append(row)

            accuracy_dict = {
                'heuristic_matching': heuristic_matching,
                'max_matching': max_matching,
                'graph_density': graph_density
            }
            time_dict = {
                'heuristic_matching': heuristic_execution_time,
                'max_matching': max_matching_execution_time,
                'graph_density': graph_density
            }

            accuracy_data.append(accuracy_dict)
            execution_time_data.append(time_dict)
        context = {
            'rows': data,
            'accuracy_dict': json.dumps(accuracy_data),
            'time_dict': json.dumps(execution_time_data),

        }
        return context

    @staticmethod
    def build_graph(nodes: int, density: float, username: str = 'admin'):
        user: User = User.objects.get(username=username)

        if nodes % 2 == 1:
            tasks_nodes = set(range(0, math.ceil(nodes / 2)))
            workers_nodes = set(range(0, len(tasks_nodes) - 1))
        else:
            tasks_nodes = set(range(0, math.ceil(nodes / 2)))
            workers_nodes = set(range(0, len(tasks_nodes)))

        number_of_possible_edges = len(tasks_nodes) * len(workers_nodes)
        number_of_edges = math.ceil(number_of_possible_edges * density)

        Task.objects.filter(user=user).delete()
        Worker.objects.filter(user=user).delete()
        Category.objects.filter(user=user).delete()
        Education.objects.filter(user=user).delete()

        tasks_objects = []
        for task_num in tasks_nodes:
            title = f'title_{task_num}'
            description = f'description_{task_num}'
            obj = Task(title=title, description=description, status=Task.Status.OPEN.value, user=user)
            tasks_objects.append(obj)
        Task.objects.bulk_create(tasks_objects)

        workers_objects = []
        for worker_num in workers_nodes:
            first_name = f'worker'
            last_name = f'{worker_num}'
            email = f'worker_email_{worker_num}@max-matching.com'

            obj = Worker(user=user, first_name=first_name, last_name=last_name, email=email)
            workers_objects.append(obj)

        Worker.objects.bulk_create(workers_objects)

        all_tasks = list(Task.objects.filter(user=user, status=Task.Status.OPEN))
        all_workers = list(Worker.objects.filter(user=user, status=Worker.Status.FREE))
        tasks_count = len(all_tasks)

        education = Education.objects.create(user=user, name=f'MWS')
        for idx, task in enumerate(all_tasks):
            category = Category.objects.create(user=user, name=f'Category_{idx}')
            task.educations.add(education)
            task.categories.add(category)

        built_edges_num = 0
        assign_round = 0

        while True:
            if built_edges_num == number_of_edges:
                break

            for idx, worker in enumerate(all_workers):
                task_idx = (assign_round + idx) % tasks_count
                task: Task = all_tasks[task_idx]
                worker: Worker = all_workers[idx]
                for category in task.categories.all():
                    worker.categories.add(category)
                worker.education = education
                worker.save()
                built_edges_num += 1
                print(f'Edge number({built_edges_num}) built successfully: {task.id} <=> {worker.id}')

                if built_edges_num == number_of_edges:
                    break
            assign_round += 1

    @staticmethod
    def random_build_graph(nodes: int, density: float, username: str = 'admin'):
        user: User = User.objects.get(username=username)

        if nodes % 2 == 1:
            tasks_nodes = set(range(0, math.ceil(nodes / 2)))
            workers_nodes = set(range(0, len(tasks_nodes) - 1))
        else:
            tasks_nodes = set(range(0, math.ceil(nodes / 2)))
            workers_nodes = set(range(0, len(tasks_nodes)))

        num_of_edges = math.ceil((len(tasks_nodes) * len(workers_nodes)) * density)

        Task.objects.filter(user=user).delete()
        Worker.objects.filter(user=user).delete()
        Category.objects.filter(user=user).delete()
        Education.objects.filter(user=user).delete()

        tasks_objects = []
        for task_num in tasks_nodes:
            title = f'title_{task_num}'
            description = f'description_{task_num}'
            obj = Task(title=title, description=description, status=Task.Status.OPEN.value, user=user)
            tasks_objects.append(obj)
        Task.objects.bulk_create(tasks_objects)

        workers_objects = []
        for worker_num in workers_nodes:
            first_name = f'worker'
            last_name = f'{worker_num}'
            email = f'worker_email_{worker_num}@max-matching.com'

            obj = Worker(user=user, first_name=first_name, last_name=last_name, email=email)
            workers_objects.append(obj)
        Worker.objects.bulk_create(workers_objects)

        all_tasks = list(Task.objects.filter(user=user, status=Task.Status.OPEN))
        all_workers = list(Worker.objects.filter(user=user, status=Worker.Status.FREE))

        possible_edges = []

        for task in all_tasks:
            for worker in all_workers:
                possible_edges.append((task, worker))

        education = Education.objects.create(user=user, name=f'MWS')
        for idx, task in enumerate(all_tasks):
            category = Category.objects.create(user=user, name=f'Category_{idx}')
            task.educations.add(education)
            task.categories.add(category)

        random.shuffle(possible_edges)
        selected_edges = possible_edges[:num_of_edges]

        for task, worker in selected_edges:
            worker.education = task.educations.first()
            for category in task.categories.all():
                worker.categories.add(category)

            worker.save()

    @staticmethod
    def get_last_matching_result(user):
        execution_history = ExecutionHistory.objects.filter(user=user).order_by('-created_on_datetime').first()
        if not execution_history:
            return {'rows': []}

        edges = execution_history.max_matching.max_matching_edges

        edges_list = []

        for edge in edges:
            e = (edge[0].split('-')[1], edge[1].split('-')[1])
            edges_list.append(e)

        return {'rows': edges_list}

    @staticmethod
    def get_workers_count(user):
        workers_count = Worker.objects.filter(user=user).count()
        return workers_count

    @staticmethod
    def get_tasks_count(user):
        tasks_count = Task.objects.filter(user=user).count()
        return tasks_count

    @staticmethod
    def get_categories_count(user):
        categories_count = Category.objects.filter(user=user).count()
        return categories_count

    @staticmethod
    def get_tasks_per_category(user):
        top_tasks = Category.objects.filter(user=user).annotate(
            num_tasks=Count('task')
        ).filter(
            num_tasks__gt=0
        ).order_by('-num_tasks').values('name', 'num_tasks')[:5]

        return list(top_tasks)

    @staticmethod
    def get_workers_per_category(user):
        top_workers = Category.objects.filter(user=user).annotate(
            num_workers=Count('worker')
        ).filter(

            num_workers__gt=0
        ).order_by('-num_workers').values('name', 'num_workers')[:5]
        return list(top_workers)

    @staticmethod
    def get_top_10_workers(user):
        top_10_workers = Worker.objects.filter(
            user=user
        ).annotate(
            categories_count=Count('categories'),
            full_name=Concat(F('first_name'), Value(' '), F('last_name')),
            education_name=F('education__name')
        ).order_by('categories_count')[:5]

        return list(top_10_workers)

    @staticmethod
    def get_top_10_categories(user):
        top_10_categories = Category.objects.filter(
            user=user,
        ).annotate(
            tasks_count=Count('task', distinct=True),
            workers_count=Count('worker', distinct=True),
        ).order_by(
            '-tasks_count'
        ).values('name', 'tasks_count', 'workers_count')[:10]
        return list(top_10_categories)
