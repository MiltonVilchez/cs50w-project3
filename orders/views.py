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
    return render(request, 'orders/register.html')