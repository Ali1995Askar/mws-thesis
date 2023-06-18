from . import views
from django.urls import path

app_name = 'tasks'

urlpatterns = [

    path('', views.TaskListView.as_view(), name='list'),
    path('create', views.TaskCreateView.as_view(), name='create'),
    path('statistics', views.TaskStatisticsView.as_view(), name='statistics'),
    path('<str:id>', views.TaskDetailsView.as_view(), name='details'),
    path('update/<str:id>', views.TaskUpdateView.as_view(), name='update'),
    path('delete/<str:id>', views.TaskDeleteView.as_view(), name='delete'),

]
