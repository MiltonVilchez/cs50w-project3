from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'orders/index.html')

def menu(request):
    
    return render(request, 'orders/menu.html')

def carrito(request):
    return render(request, 'orders/carrito.html')
    
def ordenes(request):
    return render(request, 'orders/ordenes.html')

def register(request):
    return render(request, 'orders/register.html')