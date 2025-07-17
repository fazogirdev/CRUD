from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView

from .models import Car
from .forms import CarForm

from django.urls import reverse_lazy

# Create your views here.

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car-create')

class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'cars'

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'cars/car_update.html'
    success_url = reverse_lazy('car_list')

def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('car_list')
