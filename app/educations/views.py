from django.urls import reverse
from django.views import generic
from educations.models import Education
from educations.forms import EducationForm
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class EducationListView(generic.ListView):
    model = Education
    template_name = "education/list-educations.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user).order_by('created_on_datetime')
        return qs


@method_decorator(login_required, name='dispatch')
class EducationCreateView(generic.CreateView):
    model = Education
    form_class = EducationForm
    template_name = "education/create-education.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("educations:list")


# @method_decorator(login_required, name='dispatch')
class EducationUpdateView(generic.UpdateView):
    model = Education
    form_class = EducationForm
    template_name = "education/update-education.html"
    context_object_name = 'education'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse('educations:list')


@method_decorator(login_required, name='dispatch')
class EducationDeleteView(generic.DeleteView):
    model = Education
    template_name = "education/delete-education.html"
    context_object_name = 'education'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("educations:list")
