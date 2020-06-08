from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_page, name="logout"),
    path("pizza/", views.pizza, name="pizza"),
    path("salad/", views.salad, name="salad"),
    path("dinner_platter/", views.dinner_platter, name="dinner_platter"),
    path("pasta/", views.pasta, name="pasta"),
    path("sub/", views.sub, name="sub"),
    path("topping/", views.topping, name="topping"),
    path("add/<str:category>/<str:name>/<str:price>", views.add, name="add")
]
