from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import RegularPizza, SicilianPizza, Topping, Sub, Pasta, Salad, DinnerPlatter, Category, UserOrder, Order, OrderCounter
from django.db.models import Sum
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    order_number=UserOrder.objects.get(user=request.user,status='started').order_number
    context = {
        "user":request.user,
        "Checkout":Order.objects.filter(user=request.user,number=order_number),
        "Checkout_category":Order.objects.filter(user=request.user,number=order_number).values_list('category').distinct(),
        "Total":list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
        "Category": Category.objects.all(),
        "Order_number":order_number
    }

    return render(request, "orders/index.html", context)


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
                "invalid": "Passwords don't match. Try again."
            }
            return render(request, "orders/registration.html", context)
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        if OrderCounter.objects.first() == None:
            counter = OrderCounter.objects.create()

        counter = OrderCounter.objects.first()

        order = UserOrder.objects.create(user=user, order_number=counter.counter)
        order.save()

        counter.counter += 1
        counter.save()
    
        return render(request, "orders/login.html", {"message": "Registration was successful. You can log in now."})
    return render(request, "orders/registration.html")


def login_page(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"invalid": "Invalid Credentials"})


def logout_page(request):
    logout(request)
    return render(request, "orders/login.html", {"logout": "Logged out."})


def pizza(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    regular_pizzas = RegularPizza.objects.all()
    sicilian_pizzas = SicilianPizza.objects.all()
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    context = {
        "regular_pizzas": regular_pizzas,
        "sicilian_pizzas": sicilian_pizzas,
        "Order_number": order_number,
        "Total": list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
        "category1": "Regular Pizza",
        "category2": "Sicilian Pizza"
    }
    return render(request, "orders/pizzas.html", context)


def salad(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    salads = Salad.objects.all()
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    context = {
        "salads": salads,
        "category": "Salads",
        "Order_number": order_number,
        "Total":list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
    }
    return render(request, "orders/salads.html", context)


def dinner_platter(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    dinner_platters = DinnerPlatter.objects.all()
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    context = {
        "dinner_platters": dinner_platters,
        "category": "Dinner Platter",
        "Order_number": order_number,
        "Total":list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
    }
    return render(request, "orders/dinner_platters.html", context)


def pasta(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    pastas = Pasta.objects.all()
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    context = {
        "pastas": pastas,
        "category": "Pasta",
        "Order_number": order_number,
        "Total": list(Order.objects.filter(user=request.user, number=order_number).aggregate(Sum('price')).values())[0] or 0,
    }
    return render(request, "orders/pastas.html", context)


def sub(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    subs = Sub.objects.all()
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    context = {
        "subs": subs,
        "category": "Sub",
        "Order_number": order_number,
        "Total":list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
    }
    return render(request, "orders/subs.html", context)


def topping(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    toppings = Topping.objects.all()
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    context = {
        "toppings": toppings,
        "category": "Toppings",
        "Order_number": order_number,
        "Total": list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
        "Topping_price": 0.00,
        "Topping_count": UserOrder.objects.get(user=request.user,status='started').topping_possibility
    }
    return render(request, "orders/toppings.html", context)


def add(request, category, name, price):
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    topping_allowance = UserOrder.objects.get(user=request.user, status='started')

    context = {
        "Checkout":Order.objects.filter(user=request.user,number=order_number),
        "Checkout_category":Order.objects.filter(user=request.user,number=order_number).values_list('category').distinct(),
        "Total":list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
        "user":request.user,
        "Category": Category.objects.all(),
        "Active_category":category,
        "Topping_price": 0.00,
        "Order_number":order_number
    }

    if (category == 'Regular Pizza' or category == 'Sicilian Pizza'):
        if name == "1 topping":
            topping_allowance.topping_possibility += 1
            topping_allowance.save()
        if name == "2 toppings":
            topping_allowance.topping_possibility += 2
            topping_allowance.save()
        if name == "3 toppings":
            topping_allowance.topping_possibility += 3    
            topping_allowance.save()

    if category == "Toppings" and topping_allowance.topping_possibility == 0:
        return render(request,"index.html", context) 
    if category == "Toppings" and topping_allowance.topping_possibility > 0:
        topping_allowance.topping_possibility -= 1
        topping_allowance.save()

    add = Order(user=request.user, number=order_number, category=category, name=name, price=price)
    add.save()

    context2 = {
        "Checkout": Order.objects.filter(user=request.user,number=order_number),
        "Checkout_category": Order.objects.filter(user=request.user,number=order_number).values_list('category').distinct(),
        "Total": list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0,
        "user": request.user,
        "Category": Category.objects.all(),
        "Active_category": category,
        "Topping_price": 0.00,
        "Order_number": order_number
    }       
    return render(request, "orders/index.html", context2) 


def delete(request, category, name, price):
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    topping_allowance=UserOrder.objects.get(user=request.user,status='started')

    if (category == 'Regular Pizza' or category == 'Sicilian Pizza'):
        if name == "1 topping":
            topping_allowance.topping_possibility -= 1
            topping_allowance.save()
        if name == "2 toppings":
            topping_allowance.topping_possibility -= 2
            topping_allowance.save()
        if name == "3 toppings":
            topping_allowance.topping_possibility -= 3    
            topping_allowance.save()

        topping_allowance.topping_possibility = 0
        topping_allowance.save()

        delete_all_toppings = Order.objects.filter(user=request.user, category="Toppings")
        delete_all_toppings.delete()

    if category == "Toppings":
        topping_allowance.topping_possibility+=1
        topping_allowance.save()

    
    find_order = Order.objects.filter(user=request.user, category=category, name=name, price=price)[0]
    find_order.delete()       

    context = {
        "Checkout": Order.objects.filter(user=request.user,number=order_number),
        "Checkout_category": Order.objects.filter(user=request.user,number=order_number).values_list('category').distinct(),
        "Total": list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0],
        "user": request.user,
        "Category": Category.objects.all(),
        "Active_category": category,
        "Topping_price": 0.00,
        "Order_number": order_number,
        "orders": Order.objects.filter(user=request.user),
        "Total": list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0
    }
    return render(request,"orders/my_orders.html", context)



def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    order_number = UserOrder.objects.get(user=request.user, status='started').order_number
    context = {
        "Order_number": order_number,
        "orders": orders,
        "Total": list(Order.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0] or 0
    }
    return render(request, "orders/my_orders.html", context)