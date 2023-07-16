from django.urls import reverse
from django.views import generic
from positions.models import Position
from positions.forms import PositionForm
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required, name='dispatch')
class PositionListView(generic.ListView):
    model = Position
    template_name = "position/list-positions.html"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs


@method_decorator(login_required, name='dispatch')
class PositionCreateView(generic.CreateView):
    model = Position
    form_class = PositionForm
    template_name = "position/create-position.html"

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
        return reverse("positions:list")


@method_decorator(login_required, name='dispatch')
class PositionUpdateView(generic.UpdateView):
    model = Position
    form_class = PositionForm
    template_name = "position/update-position.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("positions:list")


@method_decorator(login_required, name='dispatch')
class PositionDeleteView(generic.DeleteView):
    model = Position
    template_name = "position/delete-position.html"
    context_object_name = 'position'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        return qs

    def get_success_url(self):
        return reverse("positions:list")
