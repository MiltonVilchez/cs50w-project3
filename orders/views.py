from django import contrib
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

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
    
    return render(request, 'orders/menu.html')

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

def logget_out(request):
    logout(request)
    return HttpResponseRedirect('/')