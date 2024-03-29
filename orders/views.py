from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from orders.models import Carrito, Pasta,Orders, Salads, Subs, Toppings, RegularPizza, DinnerPlates, SicilianPizza, SpecialRegularPizza, SpecialSicilianPizza

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        uer = authenticate(username=username, password=password)
        print(f"{username}-{password}-{uer}")
        if uer is not None:
            login(request, uer, backend='django.contrib.auth.backends.ModelBackend')
            request.session['user'] = username
            return HttpResponseRedirect('/menu', request)
        else:
            messages.error(request, "Upss, We have an error. Please check if you entered the correct data")

    if request.user.is_authenticated:
        return HttpResponseRedirect('/menu', request)
    else:
        return render(request, 'orders/index.html')    

def menu(request):
    context = {
        'Toppings':Toppings.objects.all(),
    }
    if request.method == "POST":
        Topp = []
        name = request.POST.get("nametitle")
        cantidad = request.POST.get("Cantidad")
        tamanio = request.POST.get("Radios")
        Topp = request.POST.getlist('Toppings')
        #variables para obtener el precio 
        cant = len(Topp)
        user = request.POST.get("nameuser")
        iduser = User.objects.get(username=user)
        
        items = f"{name}-{tamanio}; Toppings: {Topp}"
        # iduser = User.objects.get(username=user)
        if name == "Regular Pizza":
            if cant > 3:
                messages.error(request, "You can only add 3 toppings :)")
                return HttpResponseRedirect('/menu', context) 

            obj = RegularPizza.objects.get(tamanio=tamanio, quantity_top=cant)
            price = float(cantidad) * obj.price_reg_pizza
            Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cantidad,
                price_items = price,
                user = iduser,
            )
            messages.success(request, f"{items} successfully added!")
        if name == "Sicilian Pizza":
            if cant > 3:
                messages.error(request, "You can only add 3 toppings :)")
                return HttpResponseRedirect('/menu', context) 

            obj = SicilianPizza.objects.get(tamanio=tamanio, quantity_top=cant)
            price = float(cantidad) * obj.price_sic_pizza
            Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cantidad,
                price_items = price,
                user = iduser,
            )
            messages.success(request, f"{items} successfully added!")
        if name == "Special Regular Pizza":
            if cant > 6:
                messages.error(request, "You can only add 6 toppings :)")
                return HttpResponseRedirect('/menu', context) 

            obj = SpecialRegularPizza.objects.get(tamanio=tamanio)
            price = float(cantidad) * obj.price_special_reg
            Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cantidad,
                price_items = price,
                user = iduser,
            )
            messages.success(request, f"{items} successfully added!")
        if name == "Special Sicilian Pizza":
            if cant > 6:
                messages.error(request, "You can only add 6 toppings :)")
                return HttpResponseRedirect('/menu', context) 
                
            obj = SpecialSicilianPizza.objects.get(tamanio=tamanio)
            price = float(cantidad) * obj.price_special_sic
            Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cantidad,
                price_items = price,
                user = iduser,
            )
            messages.success(request, f"{items} successfully added!")

    return render(request, 'orders/menu.html', context)

def carrito(request):
    user = request.session['user']
    iduser = User.objects.get(username=user)
    car = Carrito.objects.filter(status=False, user=iduser.id).values()

    if request.method == "POST":
        Carrito.objects.filter(status=False, user=iduser).update(status=True)
        messages.success(request, "Order confirmed!")
        return HttpResponseRedirect('/ordenes', request)
    context={
        "items": car,
    }
    return render(request, 'orders/carrito.html', context)

def ordenes(request):
    user = request.session['user']
    carrito = []
    iduser = User.objects.get(username=user)
    carrito = Carrito.objects.filter(status=True, user=iduser.id).values()
    context = {
        "carritos":carrito,
    }
    return render(request, 'orders/ordenes.html', context)

def register(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/menu', request)

    if request.method == "POST":
        username = request.POST.get("username")
        name = request.POST.get("Fname")
        lastn = request.POST.get("Lname")
        email = request.POST.get("email")
        contra = request.POST.get("password")
        ccontra = request.POST.get("cpassword")
        if contra == ccontra:
            user = User.objects.create_user(
                username = username,
                first_name = name,
                last_name = lastn,
                email = email,
                password = contra,
            ) 
            user.save();
            messages.success(request, "User created successfully!")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Check your password. They aren't equals")
            return render(request, 'orders/register.html')
    else:
        return render(request, 'orders/register.html')

def subs(request):

    if request.method == "POST":
        cant = request.POST.get("Cantidad")
        tamanio = request.POST.get("Radios")
        name = request.POST.get("nametitle")
        items = f"{name}-{tamanio}"
        user = request.POST.get("nameuser")
        iduser = User.objects.get(username=user)

        obj = Subs.objects.get(name_subs=name, tamanio=tamanio)
        price = float(cant) * obj.price_subs
        Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cant,
                price_items = price,
                user = iduser,
            )
        messages.success(request, f"{items} successfully added!")

    return render(request, 'orders/subs.html')

def pasta(request):
    
    if request.method == "POST":    
        cant = request.POST.get("Cantidad")
        name = request.POST.get("nametitle")
        items = f"{name}"
        user = request.POST.get("nameuser")
        iduser = User.objects.get(username=user)

        obj = Pasta.objects.get(name_pasta=name)
        price = float(cant) * obj.price_pasta
        Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cant,
                price_items = price,
                user = iduser,
            )
        messages.success(request, f"{items} successfully added!")
        
    return render(request, 'orders/pasta.html')    

def salads(request):
    
    if request.method == "POST":
        cant = request.POST.get("Cantidad")
        name = request.POST.get("nametitle")
        items = f"{name}"
        user = request.POST.get("nameuser")
        iduser = User.objects.get(username=user)

        obj = Salads.objects.get(name_salads=name)
        price = float(cant) * obj.price_salads
        Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cant,
                price_items = price,
                user = iduser,
            )
        messages.success(request, f"{items} successfully added!")
        
    return render(request, 'orders/salads.html') 

def dinners(request):
    
    if request.method == "POST":
        cant = request.POST.get("Cantidad")
        name = request.POST.get("nametitle")
        radios = request.POST.get("Radios")
        items = f"{name}-{radios}"
        user = request.POST.get("nameuser")
        iduser = User.objects.get(username=user)

        obj = DinnerPlates.objects.get(name_dinner=name, tamanio=radios)
        price = float(cant) * obj.price_dinner
        Carrito.objects.create(
                status = False,
                items= items,
                cantidad = cant,
                price_items = price,
                user = iduser,
            )
        messages.success(request, f"{items} successfully added!")
        
    return render(request, 'orders/dinners.html') 

def logget_out(request):
    try:   
        logout(request)
        messages.success(request, "You're logged out!")
    except KeyError:
        pass
    return HttpResponseRedirect('/')