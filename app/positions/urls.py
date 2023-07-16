from . import views
from django.urls import path

app_name = 'positions'

urlpatterns = [

    path('', views.PositionListView.as_view(), name='list'),
    path('create', views.PositionCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.PositionUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PositionDeleteView.as_view(), name='delete'),

]
