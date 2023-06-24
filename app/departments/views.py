from django.views import generic
from django.shortcuts import render


# Create your views here.

class DepartmentListView(generic.ListView):
    template_name = "department/list-departments.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class DepartmentCreateView(generic.CreateView):
    template_name = "department/create-department.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class DepartmentUpdateView(generic.UpdateView):
    template_name = "department/update-department.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class DepartmentDeleteView(generic.DeleteView):
    template_name = "department/delete-department.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
