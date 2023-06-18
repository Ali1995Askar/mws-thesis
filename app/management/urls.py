from . import views
from django.urls import path

app_name = 'management'

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('matching', views.MatchingView.as_view(), name='matching'),
    path('task-assigner', views.AssignTasksView.as_view(), name='task-assigner'),

]
