import json

from django.shortcuts import render
from django.views import generic, View


# Create your views here.
class DashboardView(View):
    template_name = "management/dashboard.html"

    def get(self, request, *args, **kwargs):
        workers_count = 10000
        tasks_count = 20000
        categories_count = 1500

        tasks_per_category = {
            'software': 50,
            'marketing': 10,
            'data_analysis': 25,

            'other': 15
        }
        workers_per_category = {
            'django': 111,
            'node-js': 25,
            'aws': 15,
            'devOps': 25,
            'other': 41
        }

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


class MatchingView(generic.ListView):
    template_name = "management/matching.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class AssignTasksView(generic.ListView):
    template_name = "management/task-assigner.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
