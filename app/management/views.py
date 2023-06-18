from django.shortcuts import render
from django.views import generic


# Create your views here.
class DashboardView(generic.ListView):
    template_name = "management/dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class MatchingView(generic.ListView):
    template_name = "management/matching.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class AssignTasksView(generic.ListView):
    template_name = "management/task-assigner.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
