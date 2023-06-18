from django.shortcuts import render

# # Create your views here.


from django.shortcuts import render
from django.views import generic


# Create your views here.
class ProfileView(generic.UpdateView):
    template_name = "accounts/profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")


class EditProfileView(generic.UpdateView):
    template_name = "accounts/edit_profile.html"

    def get(self, request, *args, **kwargs):
        return render(request, f"{self.template_name}")
