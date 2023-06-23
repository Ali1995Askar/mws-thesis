from . import views
from django.urls import path

app_name = 'positions'

urlpatterns = [

    path('', views.PositionListView.as_view(), name='list'),
    path('create', views.PositionCreateView.as_view(), name='create'),
    path('<str:id>', views.PositionDetailsView.as_view(), name='details'),
    path('update/<str:id>', views.PositionUpdateView.as_view(), name='update'),
    path('delete/<str:id>', views.PositionDeleteView.as_view(), name='delete'),

]
