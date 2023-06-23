from django.views import generic
from django.shortcuts import render


# Create your views here.

class EducationListView(generic.ListView):
    template_name = "education/list-educations.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class EducationCreateView(generic.CreateView):
    template_name = "education/create-education.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class EducationDetailsView(generic.DetailView):
    template_name = "education/education-details.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class EducationUpdateView(generic.UpdateView):
    template_name = "education/update-education.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class EducationDeleteView(generic.DeleteView):
    template_name = "education/delete-education.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
