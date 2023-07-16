from django.urls import reverse
from django.views import generic
from departments.models import Department
from departments.forms import DepartmentForm
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class DepartmentListView(generic.ListView):
    model = Department
    template_name = "department/list-departments.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class DepartmentUpdateView(generic.UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "department/update-department.html"
    context_object_name = 'department'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        reverse('departments:list')


@method_decorator(login_required, name='dispatch')
class DepartmentDeleteView(generic.DeleteView):
    model = Department
    template_name = "department/delete-department.html"
    context_object_name = 'department'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("departments:list")
