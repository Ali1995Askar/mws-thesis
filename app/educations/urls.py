from . import views
from django.urls import path

app_name = 'educations'

urlpatterns = [

    path('', views.EducationListView.as_view(), name='list'),
    path('create', views.EducationCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.EducationUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.EducationDeleteView.as_view(), name='delete'),

]
