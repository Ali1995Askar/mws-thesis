from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from core.services import Services


class HomeView(TemplateView):
    template_name = 'site-pages/index.html'


class FAQView(TemplateView):
    template_name = 'site-pages/f_a_q.html'


def error_404(request, exception):
    return render(request, '404.html')


def error_500(request):
    return render(request, '500.html')


@method_decorator(login_required, name='dispatch')
class PresentationView(UserPassesTestMixin, TemplateView):
    def test_func(self):
        return self.request.user.is_superuser

    template_name = "site-pages/presentation.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")

    @staticmethod
    def post(request, *args, **kwargs):
        data = request.POST

        algorithms = data.getlist('algorithms')
        nodes_count = int(data['nodes_count'])
        graph_density = float(data['graph_density'])
        algorithms.insert(0, 'modified_greedy')

        matching_results, time_results = Services.heuristics_executor(nodes_count, graph_density, algorithms)

        matching_results = sorted(matching_results, key=lambda d: d['algoMatchingValue'], reverse=True)
        time_results = sorted(time_results, key=lambda d: d['algoRunTime'])

        res = {"matchingData": matching_results, "runTimeData": time_results}
        return JsonResponse(data=res, status=200)
