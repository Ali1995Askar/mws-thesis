from . import views
from django.urls import path

app_name = 'categories'

urlpatterns = [

    path('', views.CategoryListView.as_view(), name='list'),
    path('create', views.CategoryCreateView.as_view(), name='create'),
    path('<str:id>', views.CategoryDetailsView.as_view(), name='details'),
    path('update/<str:id>', views.CategoryUpdateView.as_view(), name='update'),
    path('delete/<str:id>', views.CategoryDeleteView.as_view(), name='delete'),

]
