from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'site-pages/index.html'


class FAQView(TemplateView):
    template_name = 'site-pages/f_a_q.html'
