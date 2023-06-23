from django.views import generic
from django.shortcuts import render


class WorkerListView(generic.ListView):
    template_name = "workers/list-workers.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerCreateView(generic.CreateView):
    template_name = "workers/create-worker.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerUpdateView(generic.UpdateView):
    template_name = "workers/update-category.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerDeleteView(generic.DeleteView):
    template_name = "workers/delete-category.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerDetailsView(generic.DetailView):
    template_name = "workers/category-details.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class WorkerStatisticsView(generic.DeleteView):
    template_name = "workers/workers-statistics.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
