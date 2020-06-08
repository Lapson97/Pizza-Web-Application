from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class RegularPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"


class SicilianPizza(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"


class Topping(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class Sub(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(
        max_digits=4, decimal_places=2, blank=True, null=True)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"


class Pasta(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price}"


class DinnerPlatter(models.Model):
    name = models.CharField(max_length=64)
    price_small = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.price_small} - {self.price_large}"


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_number = models.IntegerField()
    topping_possibility = models.IntegerField(default=0)
    status = models.CharField(max_length=64, default='started')
    
    def __str__(self):
        return f"{self.user} - {self.order_number} - {self.status} Topping possibility: {self.topping_possibility}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.IntegerField()
    category = models.CharField(max_length=64, null=True)
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        f"{self.name} - ${self.price}"


class OrderCounter(models.Model):
    counter = models.IntegerField(default=1)

    def __str__(self):
        return f"Order no: {self.counter}"