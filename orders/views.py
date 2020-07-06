from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def cart(request):
	context = {}
	return render(request, 'orders/cart.html', context)

def checkout(request):
    return render(request,'orders/checkout.html')

def manus(request):

    return render(request, "orders/manus.html")
