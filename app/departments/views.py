from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render

from departments.forms import DepartmentForm
from departments.models import Department


# Create your views here.

class DepartmentListView(generic.ListView):
    model = Department
    template_name = "department/list-departments.html"


class DepartmentCreateView(generic.CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "department/create-department.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("departments:list")


class DepartmentUpdateView(generic.UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "department/update-department.html"

    def get_success_url(self):
        reverse('departments:list')


class DepartmentDeleteView(generic.DeleteView):
    model = Department
    template_name = "department/delete-department.html"
    context_object_name = 'department'

    def get_success_url(self):
        return reverse("departments:list")
