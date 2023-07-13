from . import views
from django.urls import path

app_name = 'accounts'

urlpatterns = [

    path('signin', views.SigninView.as_view(), name='signin'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('change-password', views.ChangePasswordView.as_view(), name='change-password'),
    path('edit-profile', views.EditProfileView.as_view(), name='edit-profile'),

]
