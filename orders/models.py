from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Toppings (models.Model):
    nombre_tooping = models.CharField(max_length=40, blank=True, unique=True)

    def __str__(self):
        return self.nombre_tooping

class DinnerPlates (models.Model):
    name_dinner = models.CharField(max_length=40, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_dinner = models.FloatField(  blank=True)

    def __str__(self):
        return f"{self.nombre_tooping} - {self.tamanio} - {self.price_dinner}"

class Pasta (models.Model):
    name_pasta = models.CharField(max_length=40, blank=True)
    price_pasta = models.FloatField(  blank=True)
    
    def __str__(self):
        return f"{self.name_pasta} - {self.price_pasta}"

class Salads (models.Model):
    name_salads = models.CharField(max_length=40, blank=True)
    price_salads = models.FloatField(  blank=True)

    def __str__(self):
        return f"{self.name_salads} - {self.price_salads}"

class ExtraSubs(models.Model):
    name_extras = models.CharField(max_length=25, blank=True)
    price_extra_sub = models.FloatField(  blank=True)

    def __str__(self):
        return f"{self.name_extras} - {self.price_extra_sub}"

class Subs (models.Model):
    #extra_sub = models.ManyToManyField(ExtraSubs)
    name_subs = models.CharField(max_length=40, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_subs = models.FloatField(  blank=True)

    def __str__(self):
        return f"{self.name_subs} - {self.tamanio} - {self.price_subs}"
    
class RegularPizza(models.Model):
    name_reg_pizza = models.CharField(max_length=30, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_reg_pizza = models.FloatField(  blank=True)
    quantity_top = models.IntegerField(max_length=1, blank=True)
    #toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return f"{self.name_reg_pizza} - {self.tamanio} - {self.price_reg_pizza} - {self.quantity_top}"

class SicilianPizza(models.Model):
    name_sic_pizza = models.CharField(max_length=30, blank=True)
    tamanio = models.CharField(max_length=10, blank=True)
    price_sic_pizza = models.FloatField(  blank=True)
    quantity_top = models.IntegerField(max_length=1, blank=True)
    #toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return f"{self.name_sic_pizza} - {self.tamanio} - {self.price_sic_pizza} - {self.quantity_top}"

class SpecialRegularPizza(models.Model):
    name_special_reg = models.CharField(max_length=40 ,default="Special Regular Pizza")
    tamanio = models.CharField(max_length=10, blank=True)
    price_special_reg = models.FloatField(  blank=True)
    #toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return f"{self.name_special_reg} - {self.tamanio} - {self.price_special_reg}"

class SpecialSicilianPizza(models.Model):
    name_special_sic = models.CharField(max_length=40 ,default="Special Sicilian Pizza")
    tamanio = models.CharField(max_length=10, blank=True)
    price_special_sic = models.FloatField( blank=True)
    #toppings = models.ManyToManyField(Toppings)

    def __str__(self):
        return f"{self.name_special_sic} - {self.tamanio} - {self.price_special_sic}"

class Carrito(models.Model):
    status = models.BooleanField(default=False)
    items = models.CharField(max_length=200, blank=True)
    cantidad = models.IntegerField(default=0, blank=True)
    price_items = models.FloatField(  blank=True)
    fecha_items = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.status} - {self.items} - {self.cantidad} - {self.price_items} - {self.fecha_items} - {self.user}"

class Orders(models.Model):
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.status} - {self.user} - {self.carrito}"