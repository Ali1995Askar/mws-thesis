from . import views
from django.urls import path

app_name = 'categories'

urlpatterns = [

    path('', views.CategoryListView.as_view(), name='list'),
    path('create', views.CategoryCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.CategoryDeleteView.as_view(), name='delete'),

]
