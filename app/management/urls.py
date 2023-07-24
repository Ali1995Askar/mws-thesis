from . import views
from django.urls import path

app_name = 'management'

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('matching-history', views.MatchingHistoryView.as_view(), name='matching-history'),
    path('task-assigner', views.AssignTasksView.as_view(), name='task-assigner'),

]
