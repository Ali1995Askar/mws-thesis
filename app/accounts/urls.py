from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [

    path('profile', views.ProfileView.as_view(), name='profile'),
    path('edit-profile', views.EditProfileView.as_view(), name='edit-profile'),
]
