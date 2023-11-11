from . import views
from django.urls import path

app_name = 'management'

urlpatterns = [
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('task-assigner', views.AssignTasksView.as_view(), name='task-assigner'),
    path('matching-result', views.MatchingResultView.as_view(), name='matching-result'),
    path('matching-history', views.MatchingHistoryView.as_view(), name='matching-history'),
    
    path('contact-us', views.contact_us_view, name='contact-us'),
]
