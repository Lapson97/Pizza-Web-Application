from django.http import HttpResponse
from django.shortcuts import render
from .models import RegularPizza, SicilianPizza, Topping, Sub, Pasta, Salad, DinnerPlatter

# Create your views here.


def index(request):
    context = {
        "regular_pizzas": Topping.objects.all()
    }
    return render(request, "orders/index.html", context)
