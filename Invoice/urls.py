from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    path("", views.home, name="Home"),
    path("home/", views.home, name="Home"),
    path("newinvoice/", views.newinvoice, name="Newinvoice"),
    path("invoice/", views.invoice, name="Invoice"),
    path("product/", views.product, name="Product"),
    path("customer/", views.customer, name="Customer"),
]
