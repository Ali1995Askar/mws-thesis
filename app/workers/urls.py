from . import views
from django.urls import path

app_name = 'workers'

urlpatterns = [
    path('', views.WorkerListView.as_view(), name='list'),
    path('create', views.WorkerCreateView.as_view(), name='create'),
    path('<str:id>', views.WorkerDetailsView.as_view(), name='details'),
    path('update/<str:id>', views.WorkerUpdateView.as_view(), name='update'),
    path('delete/<str:id>', views.WorkerDeleteView.as_view(), name='delete'),
]
