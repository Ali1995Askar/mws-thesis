from django.views import generic
from django.shortcuts import render


class WorkerListView(generic.ListView):
    template_name = "workers/list_workers.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerCreateView(generic.CreateView):
    template_name = "workers/create_worker.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerUpdateView(generic.UpdateView):
    template_name = "workers/update_worker.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerDeleteView(generic.DeleteView):
    template_name = "workers/delete_worker.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerDetailsView(generic.DetailView):
    template_name = "workers/worker_details.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerStatisticsView(generic.DeleteView):
    template_name = "workers/workers_statistics.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
