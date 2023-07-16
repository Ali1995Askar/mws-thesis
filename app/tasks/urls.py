from . import views
from django.urls import path

app_name = 'tasks'

urlpatterns = [

    path('', views.TaskListView.as_view(), name='list'),
    path('create', views.TaskCreateView.as_view(), name='create'),
    path('<str:pk>', views.TaskDetailsView.as_view(), name='details'),
    path('update/<str:pk>', views.TaskUpdateView.as_view(), name='update'),
    path('delete/<str:pk>', views.TaskDeleteView.as_view(), name='delete'),

]
