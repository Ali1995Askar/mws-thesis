from . import views
from django.urls import path

app_name = 'auth'

urlpatterns = [

    path('signup', views.SignupView.as_view(), name='signup'),
    path('signin', views.SigninView.as_view(), name='signin'),
   
]
