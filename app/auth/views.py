from django.shortcuts import render

# # Create your views here.


from django.shortcuts import render
from django.views import generic


class SignupView(generic.ListView):
    template_name = "auth/signup.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class SigninView(generic.ListView):
    template_name = "auth/signin.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
