from django.views import generic
from django.shortcuts import render


# Create your views here.

class PositionListView(generic.ListView):
    template_name = "position/list-positions.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class PositionCreateView(generic.CreateView):
    template_name = "position/create-position.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class PositionDetailsView(generic.DetailView):
    template_name = "position/position-details.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class PositionUpdateView(generic.UpdateView):
    template_name = "position/update-position.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class PositionDeleteView(generic.DeleteView):
    template_name = "position/delete-position.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
