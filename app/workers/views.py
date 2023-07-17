from django.urls import reverse
from django.views import generic

from tasks.models import Task
from workers.models import Worker
from django.shortcuts import render
from workers.forms import WorkerForm
from django.http import HttpResponseRedirect


class WorkerListView(generic.ListView):
    model = Worker
    template_name = "workers/list-workers.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerForm
    template_name = "workers/create-worker.html"

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
        return reverse("workers:list")


class WorkerUpdateView(generic.UpdateView):
    model = Worker
    form_class = WorkerForm
    template_name = "workers/update-worker.html"
    context_object_name = 'worker'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('workers:list')


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    template_name = "workers/delete-worker.html"
    context_object_name = 'worker'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("workers:list")


class WorkerDetailsView(generic.DetailView):
    model = Worker
    context_object_name = 'worker'
    template_name = "workers/worker-details.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get(self, request, *args, **kwargs):
        obj: Worker = self.get_object(queryset=self.get_queryset())
        skills = list(obj.categories.all().values_list('name', flat=True))
        suitable_tasks = Task.objects.filter(user=self.request.user).only('id', 'title')

        context = {
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'level': obj.level,
            'status': obj.status,
            'email': obj.email,
            'education': obj.education,
            'skills': skills,
            'suitable_tasks': suitable_tasks
        }
        return render(request, f"{self.template_name}", context=context)
