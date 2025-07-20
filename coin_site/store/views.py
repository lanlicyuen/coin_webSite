from django.shortcuts import render
from .models import Product

def index(request):
    featured = Product.objects.filter(is_featured=True)
    return render(request, 'store/index.html', {'featured': featured})

def products(request):
    items = Product.objects.all()
    return render(request, 'store/products.html', {'products': items})

def contact(request):
    return render(request, 'store/contact.html')
