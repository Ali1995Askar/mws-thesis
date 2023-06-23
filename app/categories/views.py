from django.shortcuts import render
from django.views import generic


class CategoryListView(generic.ListView):
    template_name = "category/list-category.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class CategoryCreateView(generic.CreateView):
    template_name = "category/create-category.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class CategoryDetailsView(generic.DetailView):
    template_name = "category/category-details.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class CategoryUpdateView(generic.UpdateView):
    template_name = "category/update-category.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class CategoryDeleteView(generic.DeleteView):
    template_name = "category/delete-category.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
