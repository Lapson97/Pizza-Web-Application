from django.http import HttpResponse
from django.shortcuts import render
from .models import RegularPizza, SicilianPizza, Topping, Sub, Pasta, Salad, DinnerPlatter
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/index.html")
    return render(request, "orders/index.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            context = {
                "message": "Passwords don't match. Try again."
            }
            return render(request, "orders/registration.html", context)
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        context = {
            "message": "Registration was successful. You can log in now."
        }
        return render(request, "orders/index.html", context)
    return render(request, "orders/registration.html")
