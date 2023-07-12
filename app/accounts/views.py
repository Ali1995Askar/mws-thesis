import json

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth import login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from accounts.forms import SignupForm, SigninForm, ChangePasswordForm, ProfileForm


class SigninView(generic.UpdateView):
    template_name = "accounts/signin.html"

    def get(self, request, *args, **kwargs):
        form = SigninForm
        return render(request, f"{self.template_name}", context={'form': form})

    def post(self, request, *args, **kwargs):
        form = SigninForm(data=request.POST)

        if not form.is_valid():
            context = {'form': form}
            return render(request, f"{self.template_name}", context)

        user = form.get_user()
        login(request, user)
        return redirect(reverse('management:dashboard'))


class SignupView(generic.CreateView):
    template_name = "accounts/signup.html"

    def get(self, request, *args, **kwargs):
        form = SignupForm
        return render(request, f"{self.template_name}", context={'form': form})

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST)

        if not form.is_valid():
            context = {'form': form}
            return render(request, f"{self.template_name}", context)

        user = form.save()
        login(request, user)
        return redirect(reverse('accounts:profile'))


class LogoutView(View):
    template_name = "accounts/logout.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(request)
            return redirect(reverse('home'))
        else:
            return redirect(reverse('accounts:signin'))


class ProfileView(generic.UpdateView):
    template_name = "accounts/profile.html"
    change_password_form = ChangePasswordForm
    change_profile_form = ProfileForm

    context = {
        'change_password_form': change_password_form,
        'change_profile_form': change_profile_form,
    }

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}", context=self.context)

    def post(self, request, *args, **kwargs):
        pass


class ChangePasswordView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        print('getgetgetgetgetgetgetgetgetgetgetget')
        return HttpResponse(json.dumps({'success': False}), mimetype='application/json')

    @staticmethod
    def post(request, *args, **kwargs):
        print('postpostpostpostpost')
        print(request.method)
        form = ChangePasswordForm(request.user, request.POST)
        print(form.data)
        if form.is_valid():

            user = form.save()
            update_session_auth_hash(request, user)  # Update the session with the new password
            return JsonResponse({'message': 'Password changed successfully.'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
