from django.shortcuts import render
from .models import MyModel, Car
# Create your views here.
def home(request):
    data = MyModel.objects.all()
    cars = Car.objects.all()
    return render(request, 'home.html', {'data': data, 'cars': cars})

