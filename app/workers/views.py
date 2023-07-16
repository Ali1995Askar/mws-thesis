from django.urls import reverse
from django.views import generic
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
        reverse('workers:list')


class WorkerDeleteView(generic.DeleteView):
    model = Worker
    template_name = "workers/delete-worker.html"
    context_object_name = 'task'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("workers:list")


class WorkerDetailsView(generic.DetailView):
    template_name = "workers/worker-details.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
