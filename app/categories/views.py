from django.urls import reverse
from django.views import generic
from categories.models import Category
from categories.forms import CategoryForm
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class CategoryListView(generic.ListView):
    model = Category
    template_name = "category/list-categories.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


@method_decorator(login_required, name='dispatch')
class CategoryCreateView(generic.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/create-category.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse("categories:list")


@method_decorator(login_required, name='dispatch')
class CategoryUpdateView(generic.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "category/update-category.html"
    context_object_name = 'category'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        reverse('categories:list')


@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(generic.DeleteView):
    model = Category
    template_name = "category/delete-category.html"
    context_object_name = 'category'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("categories:list")
