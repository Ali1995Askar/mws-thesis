from . import views
from django.urls import path

app_name = 'management'

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('matching-statistics', views.MatchingStatisticsView.as_view(), name='matching-statistics'),
    path('task-assigner', views.AssignTasksView.as_view(), name='task-assigner'),

]
