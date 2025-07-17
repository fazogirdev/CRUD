from django.urls import path
from .views import CarCreateView, CarListView, CarUpdateView
from . import views

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('add/', CarCreateView.as_view(), name='car-create'),
    path('car/<int:pk>/edit/', CarUpdateView.as_view(), name='car-update'),
    path('car/<int:pk>/delete/', views.delete_car, name='car_delete')
]