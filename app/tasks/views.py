from tasks.models import Task
from django.urls import reverse
from tasks.forms import TaskForm
from django.views import generic
from django.shortcuts import render
from tasks.selectors import TaskSelectors
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/list_tasks.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user).order_by('created_on_datetime')
        return qs


@method_decorator(login_required, name='dispatch')
class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create_task.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        print(form['deadline'])
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse("tasks:list")


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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
        context = TaskSelectors.get_task_details(task=obj)
        return render(request, f"{self.template_name}", context=context)
