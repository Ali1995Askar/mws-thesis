from django.urls import reverse
from django.views import generic
from workers.models import Worker
from django.shortcuts import render
from workers.forms import WorkerForm
from workers.selectors import WorkerSelectors
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class WorkerListView(generic.ListView):
    model = Worker
    template_name = "workers/list-workers.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user).order_by('created_on_datetime')
        return qs


@method_decorator(login_required, name='dispatch')
class WorkerCreateView(generic.CreateView):
    model = Worker
    form_class = WorkerForm
    template_name = "workers/create-worker.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse("workers:list")


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
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
        context = WorkerSelectors.get_worker_details(worker=obj)
        return render(request, f"{self.template_name}", context=context)
