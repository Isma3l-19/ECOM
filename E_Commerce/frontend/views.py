from django.shortcuts import render
from .models import *

# Create your views here.
# view function for the products
def products(request):
    # get all the products from the database
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})
