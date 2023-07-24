from tasks.models import Task
from django.urls import reverse
from tasks.forms import TaskForm
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from workers.models import Worker


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
        print('ssssssssssssssssssssssssssssssssssssssssssss')
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        print('3333333333333333333333333333333333333333')
        return reverse("tasks:list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update_task.html"
    context_object_name = 'task'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('tasks:list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    context_object_name = 'task'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("tasks:list")


class TaskDetailsView(generic.DetailView):
    model = Task
    context_object_name = 'task'
    template_name = "tasks/task_details.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get(self, request, *args, **kwargs):
        obj: Task = self.get_object(queryset=self.get_queryset())

        suitable_workers = Worker.objects.filter(user=self.request.user).only('id', 'first_name', 'last_name')
        skills = list(obj.categories.all().values_list('name', flat=True))
        educations = list(obj.educations.all().values_list('name', flat=True))
        context = {
            'title': obj.title,
            'description': obj.description,
            'deadline': obj.deadline,
            'status': obj.status,
            'level': obj.level,
            'educations': educations,
            'skills': skills,
            'suitable_workers': suitable_workers
        }
        return render(request, f"{self.template_name}", context=context)
