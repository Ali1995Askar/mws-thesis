from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = 'site-pages/index.html'


class ContactUsView(TemplateView):
    template_name = 'site-pages/contact-us.html'


class AboutUsView(TemplateView):
    template_name = 'site-pages/about-us.html'
