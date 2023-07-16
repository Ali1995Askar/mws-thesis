from tasks.models import Task
from django.urls import reverse
from tasks.forms import TaskForm
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/list_tasks.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create_task.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse("tasks:list")


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
