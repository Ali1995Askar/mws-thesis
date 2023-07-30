import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic, View
from management.services import Services
from management.selectors import ExecutionHistorySelectors, DashboardSelectors
from tasks.selectors import TaskSelectors
from workers.selectors import WorkerSelectors


# Create your views here.
class DashboardView(View):
    template_name = "management/dashboard.html"

    def get(self, request, *args, **kwargs):
        user = request.user
        workers_count = DashboardSelectors.get_workers_count(user)
        tasks_count = DashboardSelectors.get_tasks_count(user)
        categories_count = DashboardSelectors.get_categories_count(user)

        tasks_per_category = DashboardSelectors.get_tasks_per_category(user)
        workers_per_category = DashboardSelectors.get_workers_per_category(user)
        top_10_workers = DashboardSelectors.get_top_10_workers(user)
        top_10_categories = DashboardSelectors.get_top_10_categories(user)

        context = {
            'workers_count': workers_count,
            'tasks_count': tasks_count,
            'categories_count': categories_count,
            'tasks_per_category': json.dumps(tasks_per_category),
            'workers_per_category': json.dumps(workers_per_category),
            'top_5_workers': top_10_workers,
            'top_10_categories': top_10_categories,
        }
        return render(request, f"{self.template_name}", context=context)


class AssignTasksView(View):
    template_name = "management/task-assigner.html"

    @staticmethod
    def get_context(request):
        tasks_counts_dict = TaskSelectors.get_tasks_count_by_status(request.user)
        workers_counts_dict = WorkerSelectors.get_workers_count_by_status(request.user)
        execution_history_dict = ExecutionHistorySelectors.get_latest_execution_history(request.user)

        context = {
            'open_tasks': tasks_counts_dict['OPEN'],
            'progress_tasks': tasks_counts_dict['PROGRESS'],
            'done_tasks': tasks_counts_dict['DONE'],

            'free_workers': workers_counts_dict['FREE'],
            'occupied_workers': workers_counts_dict['OCCUPIED'],

            'graph_density': execution_history_dict['graph_density'],

            'matching': execution_history_dict['matching'],
            'execution_time': execution_history_dict['execution_time'],
            'used_heuristic_algorithm': execution_history_dict['used_heuristic_algorithm'],

        }

        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, f"{self.template_name}", context=context)

    def post(self, request, *args, **kwargs):
        action = request.POST.get("action", "")
        action_func = Services.get_task_assigner_action_func(action)
        action_func(request=request)

        if action == 'execute_algorithm':
            return redirect(reverse('management:matching-history'))
        else:
            context = self.get_context(request)
            return render(request, f"{self.template_name}", context)


class MatchingHistoryView(generic.ListView):
    template_name = "management/matching-history.html"

    @staticmethod
    def get_context(request):
        context = ExecutionHistorySelectors.get_last_15_execution_history_statistics(user=request.user)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, f"{self.template_name}", context=context)
