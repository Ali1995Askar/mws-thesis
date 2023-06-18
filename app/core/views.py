from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'site-pages/index.html'


class ContactUsView(TemplateView):
    template_name = 'site-pages/contact-us.html'


class FAQView(TemplateView):
    template_name = 'site-pages/f_a_q.html'
