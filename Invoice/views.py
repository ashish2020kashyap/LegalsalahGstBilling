from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from random import randint


def home(request):
    context={}
    return render(request, 'invoice/index.html',context)

def newinvoice(request):
    context={}
    return render(request, 'invoice/newinvoice.html',context)

def invoice(request):
    context={}
    return render(request, 'invoice/invoice.html',context)

def product(request):
    context={}
    return render(request, 'invoice/product.html',context)

def customer(request):
    context={}
    return render(request, 'invoice/customer.html',context)



