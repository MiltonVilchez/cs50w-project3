from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Toppings (models.Model):
    nombre_tooping = models.CharField(max_length=40, blank=True, unique=True)

class DinnerPlates (models.Model):
    name_dinner = models.CharField(max_length=40, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_dinner = models.DecimalField(max_digits=8, decimal_places=4, blank=True)

class Pasta (models.Model):
    name_pasta = models.CharField(max_length=40, blank=True)
    price_pasta = models.DecimalField(max_digits=8, decimal_places=6, blank=True)

class Salads (models.Model):
    name_salads = models.CharField(max_length=40, blank=True)
    price_salads = models.DecimalField(max_digits=5, decimal_places=4, blank=True)

class ExtraSubs(models.Model):
    name_extras = models.CharField(max_length=25, blank=True)
    price_extra_sub = models.DecimalField(max_digits=5, decimal_places=4, blank=True)

class Subs (models.Model):
    #extra_sub = models.ManyToManyField(ExtraSubs)
    name_subs = models.CharField(max_length=40, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_subs = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    
class RegularPizza(models.Model):
    name_reg_pizza = models.CharField(max_length=30, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_reg_pizza = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    quantity_top = models.IntegerField(max_length=1, blank=True)
    #toppings = models.ManyToManyField(Toppings)

class SicilianPizza(models.Model):
    name_sic_pizza = models.CharField(max_length=30, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_sic_pizza = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    quantity_top = models.IntegerField(max_length=1, blank=True)
    #toppings = models.ManyToManyField(Toppings)

class SpecialRegularPizza(models.Model):
    name_special_reg = models.CharField(max_length=40 ,default="Special Regular Pizza")
    tamanio = models.CharField(max_length=10, blank=True)
    price_special_reg = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    #toppings = models.ManyToManyField(Toppings)

class SpecialSicilianPizza(models.Model):
    name_special_sic = models.CharField(max_length=40 ,default="Special Sicilian Pizza")
    tamanio = models.CharField(max_length=10, blank=True)
    price_special_sic = models.DecimalField(max_digits=5, decimal_places=2,blank=True)
    #toppings = models.ManyToManyField(Toppings)

class Carrito(models.Model):
    status = models.BooleanField(default=False)
    items = models.CharField(max_length=200, blank=True)
    cantidad = models.IntegerField(default=0, blank=True)
    price_items = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    fecha_items = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Orders(models.Model):
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.PROTECT)