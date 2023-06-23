from . import views
from django.urls import path

app_name = 'educations'

urlpatterns = [

    path('', views.EducationListView.as_view(), name='list'),
    path('create', views.EducationCreateView.as_view(), name='create'),
    path('<str:id>', views.EducationDetailsView.as_view(), name='details'),
    path('update/<str:id>', views.EducationUpdateView.as_view(), name='update'),
    path('delete/<str:id>', views.EducationDeleteView.as_view(), name='delete'),

]
