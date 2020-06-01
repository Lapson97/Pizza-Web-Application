from django.db import models

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

