from django.shortcuts import render
from django.views import generic


class TaskListView(generic.ListView):
    template_name = "tasks/list_tasks.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class TaskCreateView(generic.CreateView):
    template_name = "tasks/create_task.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class TaskUpdateView(generic.UpdateView):
    template_name = "tasks/update_task.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class TaskDeleteView(generic.DeleteView):
    template_name = "tasks/delete_task.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class TaskDetailsView(generic.DetailView):
    template_name = "tasks/task_details.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class TaskStatisticsView(generic.DeleteView):
    template_name = "tasks/tasks_statistics.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
