from django.urls import reverse
from django.http import JsonResponse
from django.views import generic, View
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
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


@method_decorator(login_required, name='dispatch')
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


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    template_name = "accounts/profile.html"

    def get(self, request, *args, **kwargs):
        change_password_form = ChangePasswordForm(request.user)
        change_profile_form = ProfileForm(instance=request.user.profile)

        context = {
            'change_password_form': change_password_form,
            'change_profile_form': change_profile_form,
        }
        return render(request, f"{self.template_name}", context=context)


@method_decorator(login_required, name='dispatch')
class ChangePasswordView(View):

    @staticmethod
    def post(request, *args, **kwargs):
        form = ChangePasswordForm(request.user, request.POST)

        if not form.is_valid():
            return JsonResponse({'errors': form.errors}, status=400)

        user = form.save()
        update_session_auth_hash(request, user)
        return JsonResponse({'msg': 'Password changed successfully.'})


@method_decorator(login_required, name='dispatch')
class EditProfileView(View):

    @staticmethod
    def post(request, *args, **kwargs):
        form = ProfileForm(request.POST)

        if not form.is_valid():
            return JsonResponse({'errors': form.errors}, status=400)

        profile = request.user.profile
        img = request.FILES.get("img")
        print(img)
        inst = form.save(commit=False)
        profile.logo = img
        profile.name = inst.name
        profile.about = inst.about
        profile.address = inst.address
        profile.phone_number = inst.phone_number
        profile.contact_email = inst.contact_email
        profile.save()

        return JsonResponse({'msg': 'Profile Updated successfully.'})
