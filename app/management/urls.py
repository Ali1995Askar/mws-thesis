from . import views
from django.urls import path

app_name = 'management'

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),

]
