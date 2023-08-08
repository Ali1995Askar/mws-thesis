from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'site-pages/index.html'


class FAQView(TemplateView):
    template_name = 'site-pages/f_a_q.html'


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')
