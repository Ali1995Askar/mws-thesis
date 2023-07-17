import json

from django.shortcuts import render
from django.views import generic, View


# Create your views here.
class DashboardView(View):
    template_name = "management/dashboard.html"

    def get(self, request, *args, **kwargs):
        workers_count = self.get_workers_count()
        tasks_count = self.get_tasks_count()
        categories_count = self.get_categories_count()

        tasks_per_category = self.get_tasks_per_category()
        workers_per_category = self.get_workers_per_category()
        top_5_workers = self.get_top_5_workers()
        top_10_categories = self.get_top_10_categories()

        context = {
            'workers_count': workers_count,
            'tasks_count': tasks_count,
            'categories_count': categories_count,
            'tasks_per_category': json.dumps(tasks_per_category),
            'workers_per_category': json.dumps(workers_per_category),
            'top_5_workers': top_5_workers,
            'top_10_categories': top_10_categories,
        }
        return render(request, f"{self.template_name}", context=context)

    @staticmethod
    def get_workers_count():
        return 10000

    @staticmethod
    def get_tasks_count():
        return 20000

    @staticmethod
    def get_categories_count():
        return 1500

    @staticmethod
    def get_tasks_per_category():
        tasks_per_category = {
            'software': 50,
            'marketing': 10,
            'data_analysis': 25,

            'other': 15
        }
        return tasks_per_category

    @staticmethod
    def get_workers_per_category():
        workers_per_category = {
            'django': 111,
            'node-js': 25,
            'aws': 15,
            'devOps': 25,
            'other': 41
        }
        return workers_per_category

    @staticmethod
    def get_top_5_workers():
        top_5_workers = [
            {
                'full_name': 'ali askar',
                'email': 'ali1995askar@gmail.com',
                'education': 'software engineer',
                'level': 'Senior',
                'status': 'OCCUPIED',
            },
            {
                'full_name': 'ali askar',
                'email': 'ali1995askar@gmail.com',
                'education': 'software engineer',
                'level': 'Senior',
                'status': 'FREE',
            }
        ]
        return top_5_workers

    @staticmethod
    def get_top_10_categories():
        top_10_categories = [
            {
                'name': 'Django',
                'number_of_tasks': 500,
                'total_employees': 24,

            },
            {
                'name': 'Asp.net',
                'number_of_tasks': 500,
                'total_employees': 24,

            }
        ]
        return top_10_categories


class MatchingView(generic.ListView):
    template_name = "management/matching.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class AssignTasksView(generic.ListView):
    template_name = "management/task-assigner.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
