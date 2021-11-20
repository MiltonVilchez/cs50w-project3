from typing import List
from django import contrib
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from orders.models import Toppings

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
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

        print(f"{name}-{cantidad}-{tamanio}-{Topp}")
    else:
        print("GETMethod")

    return render(request, 'orders/menu.html', context)

def carrito(request):
    return render(request, 'orders/carrito.html')
    
def ordenes(request):
    return render(request, 'orders/ordenes.html')

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
            User.objects.create(
                username = username,
                first_name = name,
                last_name = lastn,
                email = email,
                password = contra,
            )
            messages.success(request, "User created successfully!")
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Check your password. They aren't equals")
            return render(request, 'orders/register.html')
    else:
        return render(request, 'orders/register.html')

def subs(request):

    if request.method == "POST":
        print("POSTMethod")

    return render(request, 'orders/subs.html')

def pasta(request):
    
    if request.method == "POST":
        print("POSTMethod")
        
    return render(request, 'orders/pasta.html')    

def salads(request):
    
    if request.method == "POST":
        print("POSTMethod")
        
    return render(request, 'orders/salads.html') 

def dinners(request):
    
    if request.method == "POST":
        print("POSTMethod")
        
    return render(request, 'orders/dinners.html') 

def logget_out(request):
    logout(request)
    return HttpResponseRedirect('/')