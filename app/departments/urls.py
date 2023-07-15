from . import views
from django.urls import path

app_name = 'departments'

urlpatterns = [

    path('', views.DepartmentListView.as_view(), name='list'),
    path('create', views.DepartmentCreateView.as_view(), name='create'),
    path('update/<str:pk>', views.DepartmentUpdateView.as_view(), name='update'),
    path('delete/<str:pk>', views.DepartmentDeleteView.as_view(), name='delete'),

]
