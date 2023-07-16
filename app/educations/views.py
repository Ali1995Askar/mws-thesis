from django.urls import reverse
from django.views import generic
from educations.models import Education
from educations.forms import EducationForm
from django.http import HttpResponseRedirect


class EducationListView(generic.ListView):
    model = Education
    template_name = "education/list-educations.html"


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


class EducationUpdateView(generic.UpdateView):
    model = Education
    form_class = EducationForm
    template_name = "education/update-education.html"
    context_object_name = 'education'

    def get_success_url(self):
        reverse('educations:list')


class EducationDeleteView(generic.DeleteView):
    model = Education
    template_name = "education/delete-education.html"
    context_object_name = 'education'

    def get_success_url(self):
        return reverse("educations:list")
