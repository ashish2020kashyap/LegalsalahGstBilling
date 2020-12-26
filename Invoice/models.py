from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class Customer(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    customer_name = models.CharField(max_length=200)
    customer_address = models.TextField(max_length=600, blank=True, null=True)
    customer_phone = models.CharField(max_length=14, blank=True, null=True)
    customer_gst = models.CharField(max_length=15, blank=True, null=True)
    def __str__(self):
        return self.customer_name


class Invoice(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    invoice_number = models.IntegerField()
    invoice_date = models.DateField()
    invoice_customer = models.ForeignKey(
        'Customer',
        on_delete=models.SET_NULL,
        null=True
    )
    invoice_json = models.TextField()
    def __str__(self):
        return str(self.invoice_number) + " | " + str(self.invoice_date)


class Product(models.Model):
    type= [
        ('Product', 'Product'),
        ('Service', 'Service'),
    ]
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=200, null=True, choices=type)
    name = models.CharField(max_length=200)
    hsn= models.CharField(max_length=50, null=True, blank=True)
    quantity = models.CharField(max_length=50)
    gst = models.FloatField()
    price = models.FloatField()
    def __str__(self):
        return str(self.name)
