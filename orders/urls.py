from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("carrito", views.carrito, name="carrito"),
    path("ordenes", views.ordenes, name="ordenes"),
    path("register", views.register, name="register"),
    path("logout", views.logget_out,name="logout"),
    path("subs", views.subs,name="subs"),
    path("pasta", views.pasta,name="pasta"),
    path("salads", views.salads,name="salads"),
    path("dinners", views.dinners,name="dinners"),
]
